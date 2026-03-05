---
redirect_from:
  - /python/2017/01/27/api-hammer
layout: post
title:  "API keychain to bypass rate limits"
date:   2017-01-24 4:14:30 -0500
categories: python
emoji: 🔨
---

I wrote an API keychain to use multiple keys on the same API, getting around daily max-call rate limits.

Here's [the repo](https://github.com/jakekara/api-hammer)

I called it API hammer. It's a proof-of-concept keychain module for
handling multiple keys on the same API, potentially bypassing rate
limits. Keeps track of requests per day, and when the limit is exhausted,
uses another api key.


#### usage

{% highlight python %}
# import the module
import apihammer

# create a 'connection'
# service corresponds to keys.json file "service" field
conn = apihammer.connection(service="noaa")

# get a valid api key (non-exhausted)
k = conn.api_key()

# make your API call...
your_api_call_function(k)

{% endhighlight %}

#### keys.json

By default, apihammer uses a file called keys.json for an api keychain
file. Each time you call the api_key() method, apihammer updates the
keychain file. When the calls_per_day is reached for an api key, it is now
considered exhausted for that day.

You will want to copy keys.json.example to keys.json like so:

{% highlight bash %}
$ cp keys.json.example keys.json
{% endhighlight %}

and modify the settings appropriately.

The structure of keys.json is an array of objects. You must specify a
"service" property, a "key" (the api key itself) property. uname is not yet
used, but it is intendend to help you keep track of which email address
your key is associated with. "calls_per_day" must be set to the max calls
the API allows per day.

apihammer will add fields "calls" and "last_call" for its bookkeeping
purposes.

#### calls per second

apihammer can throttle the api_key() function if one calls:

{% highlight python %}
conn.set_calls_per_second(5)
{% endhighlight %}

All this will do is force the api_key() method to sleep for 1/5 of a second
before returning. Since your API request method should be dependent upon
the return value of api_key(), this will cause your code to obey the API's
calls-per-second rate limiting.

#### Refactor remnants, proof of concept code

There is some left-over code in apihammer from when I initially thought I
might also use the module to make the api calls, but I realized that's not
the best design. There are some methods that aren't used. I wanted to get
the code out fast. Along those lines, I haven't exhaustively tested this.

Since this code hasn't been tested much, please consider it a proof of
concept.

#### Be nice

If some data provider is good enough to provide an API you should generally
respect the nature of their rate limiting and not try to get around it. But
sometimes you have to be a jerk.
