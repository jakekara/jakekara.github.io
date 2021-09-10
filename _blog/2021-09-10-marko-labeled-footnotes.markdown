---
layout: post
title: marko labeled footnotes
date: "2021-09-10 12:01:00 -0500"
categories: python
emoji: 📑
---

Here's a little extension for string-labeled footnotes in Marko.

Here's the repo: [https://github.com/jakekara/marko-labeled-footnotes](https://github.com/jakekara/marko-labeled-footnotes)

Marko is a Python Markdown editor — not to be confused with a JS tool with the same name. I'm using it in a site builder that parses Markdown files, and I wanted to extend the basic footnote plugin so that it uses string labels instead of only sequential numeric footnote labels.

You can use `[^label-text]` or `[^label-id=label-text]` where label-id is unique to the document.
