---
redirect_from:
  - /python/2016/10/08/brute-forcing-url-shorteners
layout: post
title:  "Brute forcing URL shorteners"
date:   2016-10-08 22:57:30 -0400
categories: python
emoji: 💪
---

I experimented in brute-forcing URL shortening services.

[Here's](https://github.com/jakekara/python-get-shorty) the repo (Python).

[Here's a
.tsv](https://github.com/jakekara/python-get-shorty/blob/master/sample_output/two-chars.tsv)
of all the two-character bit.ly links and the URLs they forward to.

It works like this:

1. Generate the valid URLs
2. Send an HTTP request with the request library

There have been a decent number of
[stories](https://www.schneier.com/blog/archives/2016/04/security_risks_11.html)
lately about the security risks posed by URL shorteners because they can be trivially brute forced. A lot of shortened links are probably meant to be public, such as URLs shortened for sharing on social media, but I guess some services, like OneDrive, use short URLs for documents.

### disabling rediects

Since I only wanted to find the full URLs that were being redirected to,
and not actually download their content, I set the requets allow_redirects
option to False.

{% highlight python %}
r = requests.get(url, allow_redirects=False)
{% endhighlight %}


