---
redirect_from:
  - /javascript/2017/10/08/plottools
layout: post
title:  "A plotting toolbox for D3"
date:   2017-10-07 00:00:30 -0500
categories: javascript
emoji: 📊
---

I'm building a set of chart-making tools that don't get between you and D3.

* Here's the repo:
[https://github.com/jakekara/jk-plottools](https://github.com/jakekara/jk-plottools).


_This document is more about the philosophy and high-level functionality of
the tool set. For documentation and demo code, check out the repo._

## Not getting in the way

So, what I mean by not getting between you and D3 is that this tool set
does not reimplement or abstract D3's powerful tools or notions. Instead,
it glues together some of the discrete capabilities of D3 in a manner that
you would most likely use them for basic chart building. Wherever this tool
set creates an instance of a D3 object, such as D3.axisBottom, or even a D3
selection, it exposes that object, so you can use this tool to bootstrap basic
charts quickly, but then modify them as needed.

Basic charts, which I'll generally call "daily graphics", include bars,
lines, scatter plots and maybe some other basic charts that get the job
done most of the time. These are charts that non-technical news staff
members can produce on their own, or they can be output from a Pandas or R
analysis.

### Why bother?

You might ask why bother. There are other ready-made chart tools. I have
tried many, but they tend to be highly opinionated and aren't meant to be
fiddled with outside of their own APIs. I do not like spending my time
learning APIs, such as how to make a vertical line label the Highcharts
way, when I can just make a standard SVG _line_ element, and add it
wherever I want.

* Highcharts is excellent for getting charts built fast, but it is too
opinionated about styling, and the API is too cumbersome.
* [ggD3](https://benjh33.github.io/ggd3/) looks promising but it is no longer
being actively developed.

So, I need a limited set of tools that has a _minimal API_, is
_unopinionated_ about styling and which is still being actively
developed. If you can find one, let me know and I'll happily abandon this
project!

Okay, here's how it all works...

## The base layer: Plotter

Ingredients:

* An SVG element
* Two D3 scales: One for X, one for Y

In order to put any data on an SVG you need to be able to map your data --
dollars, population, car crashes -- to coordinates on the page.

You create a new plotter object by calling its constructor, and then
calling methods to give it an SVG element on the DOM to draw in, and two
scales, for X and Y.

Any D3.scale will work -- D3.scaleLinear, D3.scaleTime. Since I'm not
trying to recreate or abstract any D3 components. You must set the scale's
domain based on your min and max data values, but plotter takes care of the
domain, which is based on the SVG dimensions. Since plotter remaps the
domain each time it redraws, this tool set gives you responsive graphics
_almost_ for free.

***On "Almost" free responsiveness:*** _Right now you have to call the
   draw method to redraw, but I will make that automatic._ 

## Adding drawables 

Once you have a plotter, you add any number of "drawables" -- objects that
can draw themselves when tied to a plotter. Calling the plotter's draw
method iterates through the drawables in order that they were added
(first-in-first-out) and calls their draw methods, so you can redraw at
any time.

_I have implemented axes, scatter and line drawables. A bar drawable will
be added next._ 

The plotter stores some basic information and objects all of the drawables
need access to, such as the SVG, and a dictionary of its margin
dimensions. Drawables, such as the axes drawable, may mutate the margins to
fit their various components. When that happens, they must call the
plotter's draw function so all of the other drawables can redraw based on
these updated settings.

The process of adding a drawable to a plotter involves creating a new
drawable by calling its constructor and adding the drawable with the
plotter's addDrawable method. 

### The axes drawable

Ingredients:

* A plotter

Seriously, you don't need to supply any additional data or functionaliy to
draw an axis. Since you've already created a plotter with an X and Y scale,
the axes object needs only to be created and added to the plotter.

Since it exposes the axis it creates, you can modify it using D3 or JS to
your heart's content before you draw the entire visualization with the
plotter's draw function.

This drawable adds a left and bottom axis, based on the plotter's scale and
SVG dimensions.

_Note: I do not support top and right axes at this time, and that is the
most opinionated piece of this code base so far._

All of the positioning to make the axes fit within the SVG are
handled internally. As needed, this drawable will modify the plotter's
margins and redraw the visualization automatically, triggering all other
drawables to be redrawn. Since all drawables can access the plotter's
margins, they will be redrawn with the axes dimensions and position taken
into account.

Most of my daily graphics have axes, but you may well want to skip this
step if you're making a sparkline for instance.

### Scatter, line drawables

Ingredients:

* A plotter
* A data array
* Two functions that return X and Y values from the array

Adding a scatter or line drawable are identical processes. You provide some
array of data and a function that returns X values and a function that
returns Y values.

## Status and planned use

Currently, this project is just in the form of several JavaScript files you
can include with script tags. They are not bundled or minified yet. I plan
to add a few more features and then use this library to unify styles within
a web-based in-house chart making tool, as well as for generating web
charts with PANDAS.

## Free as in freedom

This entire thing is re-usable under GPL 3.
