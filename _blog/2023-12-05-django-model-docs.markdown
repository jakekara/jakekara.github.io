---
layout: post
title: documenting django models
date: "2023-12-05 10:30:00 -0500"
categories: python
emoji: 📑
---

I wrote this Django tool for generating documentation of Django models.

Here's the repo: [https://github.com/jakekara/django-model-docs](https://github.com/jakekara/django-model-docs)

There are a lot of tools out there to generate documentation for
Python code, particularly the API that code exposes. But a team
I work on at The Washington Post needed a way to document the
data model we were building using the Django ORM. We needed tables
that described each field, so we could share it within and across
teams to make sure that the model accurately represented the domain.

This project spins that code out into a standalone package that
can be installed via pip and executed via a Django management 
command.

It will generate Markdown docs for any installed app's models, and it uses
docstrings and `help_text` to fill in the table, so it encourages
self-documenting code best practices.

In addition to the management command, it exposes an extensible
API, so you can change the way your app, models, or fields are 
documented.
