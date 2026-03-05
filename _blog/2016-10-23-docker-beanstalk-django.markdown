---
redirect_from:
  - /docker/2016/10/23/docker-beanstalk-django
layout: post
title:  "Deploying Django news apps on AWS"
date:   2016-10-23 12:00:00 -0400
categories: docker
emoji: 🗞
---

$ docker run -p 8080:80 jkara/occupation:latest

Run that command and you'll be hosting your own local version of [This
Django app I built](http://occupation.trendct.org/) to compare wages for
the same occupation across different states. (While it's running visit
localhost:8080 from a browser).

I've deployed Django apps on AWS three different ways now, and I wanted to
put down some of my thoughts on each approach. I know, this is poorly organized.

### Approach 1. A "raw" EC2 container

The first time I used AWS, I just wanted to spin up a VPS, and EC2 was the
most like other VPS hosting I'd used in the past. It's just a virtual
server, I SSHed into, configured to match my dev environment, and then
deployed my app. Meh.

### Approach 2. A Docker container on Beanstalk

Building my app locally in Docker allowed me to push it to a Docker repo
and then upload a Dockerrun.aws.json file to Beanstalk to deploy my
app. This is already better than solution 1, since it doesn't require the
fiddling around with making the virtual server match my dev environment.

That's how I built this occupational wage comparison app.

One distinct bonus of using Docker is that I can just share the image with
colleagues and let them run it locally, without deploying it.

Another nicety of using Docker is that development process feels especially
clean, since it's isolated from your dev host. 

In my case, I built a base container that included Apache and with mod_wsgi
and a specific directory where the app would live. When I ran the docker
image, I used the -v flag to mount the local volume where I was developing
my app. This way I didn't have to build the image every time I changed the
app. I use the base image for every Docker/Django app I write, and I use a
Makefile to simplify that process.

AWS does offer some pre-baked base Docker images, but by the time I figured
that out I had already built my own. My base image works pretty much
exactly the same way, but I'm sure Amazon's is better.

### Approach 3. Lambda

One word: [Zappa](https://github.com/Miserlou/Zappa).

Zappa is a deploy tool for Python apps on Lambda. It gives you a bunch of
features Lambda should probably just give you out of the box.

To build and deploy an app, you just write your Django app and use zappa to do
all the packaging and deploying to Lambda. The tutorial on the link above
is good.


### The winner: Lambda/Zappa

Overall, I prefer the Lambda approach, and I think it makes the most sense
for medium-sized news organizations that push a lot of apps. Here's why:

1. Zappa works great, right out of the box.

2. Lambda represents a significant cost savings. It
doesn't use any compute time when there is no traffic to the site, unlike
an EC2 instance which has some baseline cost. This is important for a small
news non-profit like the one where I work. I write a lot of apps, and I
want to be able to deploy them all independently and leave them
running. With Lambda, I don't have to worry about the cumulative costs as
much.

3. It feels like the least bloated, most logical way to to do this
thing. After all, my end goal is just to get a Django app living on the web
somewhere. I don't really want to configure a server, even if it is inside
a Docker container and I only have to do it once. With Lambda, all you are
uploading is your Python code.

### Design considerations: Externalizing state and serving static files

News apps are different from most types of web apps. Many of them them
don't have to manage users, and they may not have any state that needs to
persist beyond the baked-in data that you're presenting. I news see apps in
the following categories:

1. Client-only, frozen-state - These are apps that can be written
completely in client-side code, JavaScript and HTML. They may have data but
it's a small enough amount of data that you can just send all of it
(usually as a JSON object) to the client. Hosting these just means serving
up the files somewhere, that's it. Yay.

2. Client-server, frozen state - These are like Client-only apps but
there's too much data to send in a browser request. In many cases, the user
will never need all of the data. The occupation app at the top of this
story is one of these kinds of apps. It has a big database that needs to be
queried either on page load, through AJAX or both. But the database doesn't
ever need to change once the app is deployed. There are no users to manage,
no blog posts or anything.

3. Persistent state - These are like 2, but they have users. An example
might a project that has a blog compontent, where your colleagues need to
store data in a database. That database need to persist no matter whether
your app instance is killed.

In case of type 2 "frozen-state" apps, Docker might be better than
Lambda for one reason: You can store your database as sqlite3 right in your
Docker container and deploy it. That's what I did with the occupation
app. Of course this doesn't work for type 3 "Persistent-state" apps,
because the database would be immutable, and any blog posts your colleagues
write would vanish whenever the container was killed. They wouldn't like
that.

In all of these cases, it's possible to just externalize data to an RDS
database or some other managed database service. That's what I'm doing in a
project I'll be deploying in November.

Just like a database that never needs to be changed, static files can also
be baked into a Docker container. But with Lambda that isn't really
possible, as far as I know. Static files need to be externalized, and I
like S3 for that. [Here's a guide
I](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/)
that I follow for that.