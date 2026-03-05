---
redirect_from:
  - /javascript/2017/04/16/toposplit
layout: post
title:  "Split big topojson files into a grid of files"
date:   2017-04-16 10:00:30 -0500
categories: javascript
emoji: 🗺
---

I made a script to split a giant topojson file into a ton of smaller ones.

Here's the code: [https://github.com/jakekara/toposplit](https://github.com/jakekara/toposplit)

#### Why?

I needed to make a block-level map of the entire state of
Connecticut. Here's [a demo of the final
product](https://jakekara.github.io/block-zoom-ct/). Click a town to zoom
in. It loads only the topojson file for the grid it needs, on the fly,
rather than loading the entire state's worth of blocks at once.

#### mapshaper comes close but...

Census blocks are tiny -- there are 65,000+ in Connecticut, and Connecticut
is a tiny state. That means a topojson file, even simplified, of all the
Census blocks in the state is 30+ MB. Waaay too big.

So I decided to split the state into a grid, make little topojson files for
each grid, and load them on the fly.

Mapshaper has the ability to split a topojson file into layers based on a
grid, but I needed to split those layers out into separate files so I wrote
toposplit.

There's some documentation in the repo, but I suggest running the demo
script and seeing how that works to see how I actually used
it. Instructions for running the demo are in the EXAMPLE section of the
README.

The demo downloads a giant shapefile, splits it up into little ones...






