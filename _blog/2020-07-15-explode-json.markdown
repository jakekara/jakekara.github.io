---
redirect_from:
  - /JSON/2020/07/15/explode-json
layout: post
title: explode-json — serializing JSON to a file structure
date: '2020-07-15 10:00:00 -0500'
categories: JSON
emoji: 🧨
---

I'm working on a tool to serialize JSON to a folder hierarchy.

Here's the Python tool on [GitHub](https://github.com/jakekara/explode-json/). It's still a proof of concept.

Collections, such as lists and arrays, are represented as folders, and their
elements are represented as text files. Array element file names are numeric,
corresponding to their array index, and object element file names correspond to
their key.

Currently this tool works in one direction, and does not merge the folder
package back into a single JSON document, but that's coming.

I also intend to support extending this so that you can selectively determine
which entities to split into separate files. This will require some kind of a
relative link to any entity that's been separated out. This will be something
like [JSON-LD](https://w3c.github.io/json-ld-syntax/), but with relative paths.

One way I may support extending this system is to accept a custom entity
processing function. Another way might be to accept a more narrow function that
accepts an entity and returns a boolean if it should be separated out. However,
I can image the logic of whether the parent entity might be required in order to
make a decision, so I'll have to give that some more thought.