---
layout: post
title: Human-readable NWS weather reports via the CLI
date: "2024-07-18 20:01:00 -0400"
categories: python
emoji: 😎
---

I made a CLI tool for human-readable NWS weather reports.

Here's the repo: [https://codeberg.org/jakekara/nws-weather-cli](https://codeberg.org/jakekara/nws-weather-cli)

Start up and usage docs are in the repo.

You can use it to get weather reports in different formats. A setup wizard 
and config file allow you to add as many locations as you like. Here's 
an example of getting hourly weather data in Jackson, Wyoming.

```shell
nws --location jackson detailed
Tonight
Mostly clear, with a low around 59. Northwest wind around 6 mph.

Friday
Sunny, with a high near 82. Northwest wind around 6 mph.

Friday Night
Mostly clear, with a low around 59. West wind 1 to 5 mph.
```

You can also get the forecast discussion data, which is where
meteorologists describe and support their forecast. Pretty interesting stuff.
These discussions can be very long, so I like to pass it into `less`
with `nws discussion | less`