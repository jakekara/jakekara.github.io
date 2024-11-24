---
layout: project
title: Police Shootings Database, The Washington Post
description: "I worked on a major re-engineering of the backend for the Washington Post Police Shootings Database."
image: FatalForce
alt: The Washington Post Police Shootings Database
tags: 
    - Django
    - Journalism
    - Python
---

The Washington Post's [Police Shootings Database](https://www.washingtonpost.com/graphics/investigations/police-shootings-database/) is a nearly decade-old, Pulitzer-prize winning journalism project in which researchers
compile details of officer-involved, fatal shootings.

{% include imgset.html slug="FatalForce" alt="The Police Shootings database interface" %}

The project is powered by an internal Django application deployed on
our cloud infrastructure. It provides an interface for
researchers to enter evidence of officer-involved shootings, including source URLs that are
automatically archived to preserve research evidence. The system also automates the process of publishing [the open
data](https://github.com/washingtonpost/data-police-shootings) to GitHub.

My team re-engineered the backend system to be more reliable, extensible, and scalable.

I worked on both the application development and the deployment of the system, as well as helping to shape the product scope.

One of my key contributions was building a comprehensive
test suite to prevent any data from being mutated during
migration from the old system to the new system. This avoided
bugs that could have led to errors in published data.

## More links

* [Pulitzer Prize-winning Fatal Force Database updated with federal IDs of police departments involved in fatal shootings](https://www.washingtonpost.com/pr/2022/12/06/pulitzer-prize-winning-fatal-force-database-updated-with-federal-ids-police-departments-involved-fatal-shootings/)
* [Inside the Washington Post’s police shootings database: An oral history](https://medium.com/thewashingtonpost/inside-the-washington-post-s-police-shootings-database-an-oral-history-413121889529)