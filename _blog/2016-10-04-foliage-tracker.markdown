---
redirect_from:
  - /javascript/2016/10/04/foliage-tracker
layout: post
title:  "Visualizing foliage"
date:   2016-10-03 19:57:30 -0400
categories: javascript
emoji: 🍁
---

I made a thing to compare foliage in two locations over four years.

You can see [the demo here](https://jakekara.github.io/foliage-viz/) and on
[TrendCT.org here](http://projects.ctmirror.org/content/trend/2016/10/foliage/).

The code is [here](https://github.com/jakekara/foliage-viz).

It uses d3. It works like this:

1. Load in a spreadsheet containing a color for each
day, which my colleague Andrew Ba Tran [generated using R](https://github.com/trendct-data/ct-leaf-colors-analysis).
The color is meant to be a representative of the foliage color for that day, or
at least the most-dominant color.

2. Generate a bar for each year, filled with individual div elements that each
represent a day, and are colored according to the file in step 1.

3. Add a slider to allow you to slide through the days of the year. On each day,
it shows all four pictures side by side, and theoretically gives you some sense
of how brilliant the foliage has historically been on a given day. At least
that's sort of the over-intellectualized justification for it. It's really just
fun and I don't walk away from a coding challenge.

### moment.js

I used [moment.js](http://momentjs.com/) to do a few things. It seems to be a
really nice library.

I used it to map each value from 1 to 366 (leap years) on the slider to an
actual date, like this:

{% highlight javascript %}
var day = moment("2016 " + this.value,"YYYY DDD").format("DD")
var month = moment("2016 " + this.value,"YYYY DDD").format("MM")
FOL.load_date (loc_id, month, day, 2015); // , 2020);
{% endhighlight %}

When the app is bootstrapping, moment.js to get the current date and use it to
load the thumbnails for the current day (of the past years).

{% highlight javascript %}
FOL.load_date(loc_id,
	moment().format("MM"),
	moment().format("DD"),
	2015);
{% endhighlight %}

### jekyll

This was the first project I used jekyll for, and it was a perfect application.

I didn't just design the interactives; but the whole page layout, since our site
[trendct.org](//trendct.org), doesn't have a full-width template for projects
like this that have a lot of components.

A great freebie is that all I have to do is enable the project page in the repo
settings and I have a live demo of my app.

I got so hooked on Jekyll that I built this blog with it.

### Failures

Visually, the interactive could be better; I'll admit that. Deadlines.



