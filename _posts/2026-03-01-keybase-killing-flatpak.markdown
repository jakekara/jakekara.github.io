---
layout: post
title: "Flatpak apps mysteriously failing to launch"
date: "2026-03-01 06:00:00 -0500"
categories: bash
emoji: 🤯
---

Finally figured out the mystery of intermittent apps failing to launch on my Fedora/KDE system.

Every so often after a reboot, my browser and other apps, like Slack, seemed to stop launching. Usually rebooting seemed
to fix the problem, so I never dug into it.

The problem turned out to be `/keybase` — a FUSE (filesystem in userspace) mount left behind by Keybase. When the Keybase service crashes or exits uncleanly, [the FUSE mount stays behind](https://github.com/keybase/client/issues/26864). Any process that tries to `ls /` — would hang indefinitely waiting on that dead mount.

Unmounting with `sudo umount -l /keybase` immediately fixed the issue. I don't use the keybase app very much so the simplest thing for me to do was to [disable the app from running](https://github.com/keybase/client/issues/26864#issuecomment-2786643414) at startup.

What made this so confusing is that Keybase had nothing to do with what I was actually trying to do. It wasn't installed via Flatpak, I wasn't using it, and the errors I was seeing (Flatpak bwrap errors, failed pidfiles) pointed nowhere near it. I thought it was related to browser-based apps, like Slack, but that was just a correlation -- the apps I typically launch right at startup.  The hang was also intermittent — most reboots cleared the stale mount automatically, masking the real cause for months.