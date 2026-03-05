---
redirect_from:
  - /python/2016/12/11/png-explorations
layout: post
title:  "Apple screenshot PNGs contain non-standard chunk"
date:   2016-12-11 19:50:30 -0400
categories: python
emoji: 🧀
---

I did some idle poking around in the PNG file format, and found something weird.

Here's [the gist](https://gist.github.com/jakekara/8e667b7d31350692f7439cb5d0324d05).

I read up just enough on the .PNG standard to get a sense of how the data
is structured. The first few bytes in the file are the same on every PNG,
followed by a series of "chunks" that are structured the same way.

Each chunk has a chunk type, which is one of set of predefined chunks, such
as IHDR for the image header, and IDAT for the image data. I wrote a simple
loop to run through each chunk and print out the chunk type and its length
in bytes.

Oddly enough, the .PNG I was using to test out my code had a chunk type
that wasn't documented: iDOT. Here's the out (note that because there are
so many IDAT chunks in a given file, I just print the number and combined
size at the end, or else the terminal output would just be way too long.):


  {% highlight bash %}
     Valid PNG signature
     ====================
     chunk_length: 13
     chunk_type:  IHDR
     width:  2818
     height:  2328
     bit_depth:  8
     colour_type:  6c
     compression_method:  0
     filter_method:  0
     interlace_method:  0
     ====================
     chunk_length: 2728
     chunk_type:  iCCP
     ====================
     chunk_length: 9
     chunk_type:  pHYs
     ====================
     chunk_length: 415
     chunk_type:  iTXt
     ====================
     chunk_length: 28
     chunk_type:  iDOT
     ====================
     chunk_length: 0
     chunk_type:  IEND
     ====================
     Found a total of 642 IDAT chunks consuming 10512756 bytes.
{% endhighlight %}