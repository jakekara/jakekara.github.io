---
layout: post
title: ct-election-runner
date: "2024-08-08 10:00:00 -0400"
categories: python
emoji: 🇺🇸
---

I built this about a decade ago to capture Connecticut election data.

[https://github.com/jakekara/ct-election-runner](https://github.com/jakekara/ct-election-runner)

The Secretary of the State's office [in 2016](https://www.pewtrusts.org/en/research-and-analysis/articles/2016/06/08/connecticut-upgrades-election-night-reporting-to-provide-live-results)
debuted its election-night reporting system. I was in Hartford, working for the [Connecticut Mirror](https://ctmirror.org) at the time, as a data editor, and I attended a press conference when they announced the new system. I asked if there would be a public API for the system, and no one in the room knew what an "API" even was.

It turns out there is an API, it's just not documented, and I was able
to reverse engineer it and use it to power real-time election results pages for every election in the state of Connecticut without an AP subscription, like most news orgs use.

It was pretty exciting on election night, when the system I had been building with data that was all zeroed out started filling in with real data.

Every now and then I run the code to kick the tires and see if it still works, and I commit the election results to that github repo.
