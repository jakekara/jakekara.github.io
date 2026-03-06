---
redirect_from:
  - /local-ai/2026/03/06/local-ollama-inference-on-framework-13-igpu
layout: post
title: "Running local LLMs in Ollama through the iGPU on a Framework 13"
date: "2026-03-05 06:00:00 -0500"
categories: local-ai
emoji: 🤖
toot: "I got local Ollama LLMs working through the iGPU on my Framework 13, it was kind of a pain."
---

I recently got local LLM inference working on my Framework laptop 13's iGPU. Here's what worked.

## Background

I bought a new mainboard for my Framework 13 and maxed it out with memory because it's my daily driver. It has AMD's Ryzen AI HX370 and 96GB of DDR5. I thought it would be good for local LLMs right out of the box, because it has AI in the name
of the CPU, but it's not. I couldn't even get it to do much of anything.

I also couldn't find anyone who'd documented this for gfx1150, so here's my experience in case it helps any fellow travelers. Oh, and gfx1150 is what I learned is the shorthand for my specific GPU/CPU, shared memory platform. That helped look for posts about support for the platform. 

## Methodology and soapbox

There's so much I don't know about running LLMs locally, so how did I figure this out? I used
Kagi Assistant to research my specific hardware and see if anyone had written how to get this going.
Then I gave that research to Claude to turn into a guide. Then I kept talking to Claude as I 
worked through that guide, asking questions, describing issues I was running into. This is an
AI-assisted approach to my normal process of debugging where I keep process notes that pretty much
always pay dividends later when I forget something, or force me to understand it better by the
act of writing it down. 

For the record, I hate using Claude, and I hate that it's so useful. I avoid big tech as much as I can, and I also don't believe AI is always the tool for the job. But I do
find it very useful for coding and coding-adjacent tasks like devops.

So I am really hoping that I can replicate more and more of the work locally. Probably not on this machine, but I'm willing to invest in a bigger setup once I understand more about how to do this,
and what I should look for.

## Approach

The short version: BIOS change, Vulkan instead of ROCm, and a few systemd quirks. The whole thing took an afternoon, mostly spent on wrong turns.


## Step 1: Give the iGPU actual memory

Out of the box, the BIOS only allocates 512MB to the iGPU. You can check with `sudo dmesg | grep -i vram`. Mine said 512M, which is useless for inference.

Reboot, hit F2, choose **Setup Utility** (not the other three options — I tried), then **Advanced -> iGPU Memory Size**. There are three tiers: 0.5GB, 16GB, and 32GB. I went with 32GB, feeling that I 
almost never make a dent in my 96GB.

After reboot, `dmesg` confirmed 32768M of VRAM. Good start.

## Step 2: The ROCm dead end

Here's where I lost time. ROCm was already working on my system — `rocminfo` showed gfx1150, everything looked correct. So I installed Ollama, started a model, and... it fell back to CPU.

I observed this by running a query and then `ollama ps` in another terminal window. It said "100% CPU."

Setting `HSA_OVERRIDE_GFX_VERSION` didn't help.

I think this might have something to do with Ollama using its own ROCm version but I'm not sure.
It looks like this issue JUST closed as "completed", so maybe it will be moot in the future:
[https://github.com/ollama/ollama/issues/9999](https://github.com/ollama/ollama/issues/9999)

## Step 3: Vulkan worked

The fix is one environment variable: `OLLAMA_VULKAN=1`. But getting that variable to Ollama was its own small adventure.

Ollama runs as a systemd service, which means environment variables in your shell config (`~/.zshrc`, `~/.bashrc`) never reach it. You need to set them through systemd:

```
sudo systemctl edit ollama.service
```

This opens an editor with a comment block. Here's the gotcha: **write above the comments, not below them.** Anything below gets discarded. I learned this the hard way.

```ini
[Service]
Environment="OLLAMA_VULKAN=1"
Environment="OLLAMA_CONTEXT_LENGTH=120000"
Environment="OLLAMA_FLASH_ATTENTION=1"
```

(NOTE: I put similar lines in .zshrc in case I want to quickly invoke ollama manually instead of as a
service. This turns out to be handy when comparing CPU and GPU performance.)

Then reload and restart:

```
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Run `ollama ps` while a model is generating and you should see **100% GPU** in the processor column. With Vulkan, Ollama sees about 63GB of addressable GPU memory — more than enough for any 32B model.

## Step 4: Aider for agentic coding

I'm using Aider as the coding interface on top of Ollama. The config step is easy to miss.

Aider's default context window is 2048 tokens, which is too small for real work. It just straight
up didn't do anything useful. I couldn't get it to write a file that contains "hello, world!"

I will probably have a full post just on aider once I work through some issues with it.

Create `~/.aider.model.settings.yml`:

```yaml
- name: ollama/qwen2.5-coder:32b-instruct
  extra_params:
    num_ctx: 32768
```

Then just point Aider at Ollama:

```
aider --model ollama/qwen2.5-coder:32b-instruct
```

The model name has to match `ollama list` exactly.

## How fast is it?

I benchmarked `qwen3:32b` on GPU vs CPU. GPU (Vulkan) runs at about 3.84 tokens/second, CPU at 3.15 — roughly 22% faster. I used `ollama run --verbose` to get performance info.

Here's what Claude said about that:

> Not a dramatic gap, because Vulkan has overhead that a native ROCm backend wouldn't, and DDR5-5600 gives the CPU unusually fast memory bandwidth to begin with.

> The more interesting finding was a subtle quality difference. The same model, same weights, same prompt — but GPU output was noticeably better. The emoji-for-each-state test made it obvious: GPU picked contextually relevant emojis while CPU recycled the same generic ones across many states.

> This makes sense if you think about it. GPU inference runs in FP16/BF16 while CPU uses more aggressively quantized integer formats. The rounding errors are tiny per operation, but billions of multiplications compound into slightly different probability distributions. Since generation is sampled, not deterministic, even a small shift in probabilities changes which tokens win — and those choices cascade.

## The setup in a nutshell

1. Set iGPU memory to 32GB in BIOS (F2 → Setup Utility → Advanced)
2. Install Ollama, set `OLLAMA_VULKAN=1` via `systemctl edit` (not your shell config)
3. Skip ROCm for Ollama — it bundles its own, and it doesn't support gfx1150
4. Configure Aider's context window in `~/.aider.model.settings.yml`
5. Verify with `ollama ps` — look for 100% GPU

The 32B models are the sweet spot for 32GB of iGPU allocation. Fully on-GPU, no split inference, and fast enough to be useful for agentic coding workflows. Hopefully this saves you the afternoon I spent figuring it out.