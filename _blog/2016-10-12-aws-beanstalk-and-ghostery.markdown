---
redirect_from:
  - /AWS/2016/10/12/aws-beanstalk-and-ghostery
layout: post
title:  "Ghostery doesn't like AWS Beanstalk"
date:   2016-10-12 18:30:00 -0400
categories: AWS
emoji: 👻
---

Ghostery blocks assets from crazy AWS beanstalk endpoints.

Other malware/adware/tracker blockers probably do the same. 

I spent half a day pulling my hair out over this, so I'm posting an
admission of my own stupidity as a public service.

If your css and JS assets aren't loading when you're testing a Beanstalk
service, just turn off Ghostery. That's it.