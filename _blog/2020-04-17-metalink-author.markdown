---
redirect_from:
  - /python/2020/04/17/metalink-author
layout: post
title:  "metalink-author-py"
date:   2020-04-17 13:00:00 -0500
categories: python
emoji: 🗃
---

I wrote a Python library for building files in the Metalink XML format.

* [Here it is on GitHub](https://github.com/jakekara/metalink-author-py)

Metalink is a format for describing where files can be downloaded. I got into it because I was working on a project that involved creating jobs for download managers. MetaLink is supported by a number of common download managers, including Curl and [aria2C](https://aria2.github.io/manual/en/html/aria2c.html)! The RFC is available here: [https://tools.ietf.org/html/rfc5854](https://tools.ietf.org/html/rfc5854).

This library isn't finished. It does not support the full Metalink format, but it's easily extensible by adding classes for each property supported in the RFC. I've only implemented the ones I needed for the project that I built this tool for. 

More info in the [README](https://github.com/jakekara/metalink-author-py).