---
redirect_from:
  - /docker/2020/05/13/mongo-docker-startup
layout: post
title: Tripping up on Mongo Docker's use of ENTRYPOINT and CMD
date: '2020-05-13 06:00:00 -0500'
categories: docker
emoji: 🐳
---

When using the official Mongo Docker image, I ran into a problem that had me scratching my head for a while.

### The problem 
When I ran:

<pre><code>
    $ docker run --network app-net -p 27017:27017 mongo
</code></pre>

I was able to connect to the DB from my host (or another container on the "app-net" network).

However, when I ran:

<pre><code>
    $ docker run --network app-net -p 27017:27017 mongo /bin/sh -c "mongod"
</code></pre>

The server appeared to start up and listen for connections, but the service was unreachable from the host or other containers.

When I wanted to add extra initialization steps, like fetching and restoring a database, I thought that as long as I used the command <code>mongod</code> to invoke the server, I'd be good. Nope...

### Understanding the problem

It turns out that the [official Dockerfile](https://github.com/docker-library/mongo) uses a combination of <code>ENTRYPOINT</code> and <code>CMD</code>. This causes the value of <code>CMD</code>, which is <code>["mongod"]</code> to be passed as an argument array to the value of <code>ENTRYPOINT</code>, which in this case is a [helper script](https://github.com/docker-library/mongo/blob/master/docker-entrypoint.sh). So, when using <code>docker run</code> with no command, the <code>ENTRYPOINT</code> script runs with the argument <code>mongod</code>. What ends up being run is the equivalent of <code>docker-entrypoint.sh mongo<code>. 

### The solution

The solution for me was to make sure I call <code>docker-entrypoint.sh mongod</code> when I'm ready to launch the server process, whether from the command line or in the Dockerfile.

### Takeaway

The use of <code>ENTRYPOINT</code> for this purpose is entirely in line with [recommended practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#entrypoint), but it wasn't obvious to me right away what was going on without looking at the Dockerfile.

In this way, working with Docker images isn't as straightforward as using a software library, where all you have to learn is the interface and can ignore the implementation details. Sometimes you have to get more under the hood.