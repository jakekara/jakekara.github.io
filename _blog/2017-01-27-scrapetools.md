---
redirect_from:
  - /python/2017/01/27/scrapetools
layout: post
title:  "scrapetools.py - for pulling down all linked files from a page"
date:   2017-01-27 4:22:30 -0500
categories: python
emoji: 🕸
---

I wrote some Python functions to help download every file linked to on a web page.

Here's [the repo](https://github.com/jakekara/scrapetools.py)

It's called scrape_tools.py, and it has a modest four methods:

* makedir(directory) - create a directory if it doesn't exist. usefule for setting up
  your output directory structure programmatically.

* get(url) - wraps requests.get() call and raises an exception when response
  status != 200. Otherwise returns content.

* download_bin(url,output_file) - downloads a file, again using requests,
  and saves it to output_file (which is path string, not file handle).

* def get_files(html, base_url=lambda x: x, match_term=".csv", fname=lambda
  x: x) - get all files linked to in html, containing the term match_term,
  which defaults to ".csv". base_url is a method that takes a url and
  generates a base url, and fname is function takes a url and generates a
  local filename to save the file as on the local machine. Both of these
  methods have default values that do nothing.

#### example: seec.py

The example
[seec.py](https://github.com/jakekara/scrapetools.py/blob/master/seec.py)
demonstrates how to use the file download all of the CSV files linked to on
the [Connecticut State Elections Enforcement Commission's disbursement and
receipt data
page](http://seec.ct.gov/eCrisHome/eCRIS_Search/PreviousYears).

