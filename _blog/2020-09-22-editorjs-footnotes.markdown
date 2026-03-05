---
redirect_from:
  - /js/2020/09/22/editorjs-footnotes
layout: post
title: editor.js footnote plugin
date: "2020-09-22 16:45:00 -0400"
categories: js
emoji: 🦶
---

I wrote a plugin for editor.js to support footnotes.

- Github: [https://github.com/jakekara/editorjs-footnotes](https://github.com/jakekara/editorjs-footnotes)
- Package: [https://www.npmjs.com/package/editorjs-footnotes](https://github.com/jakekara/editorjs-footnotes)

[Editor.js](https://editorjs.io/) is a really great framework for a modern web-based text editor. It's very similar to the editing experience in [notion.so](https://www.notion.so).

Both tools envision a body of text as a set of individual blocks. Typically these blocks are paragraphs of text, but they can be anything, such as embedded video content, todo lists — in notion, they can even be other pages.

This is a very handy model for building custom text editors quickly. As a developer, you can build a custom block type, as well as add customization options to that block type.

My footnote plugin creates a Footnote block type and a FootnoteMaker inline tool, which allows you to select text in a body paragraph and create a subordinate footnote block. It takes care of generating an arbitrary footnote ID for purposes of linking.

This is one component in a larger project I'm working on to build a scholarly text-editor with support for multimedia content.
