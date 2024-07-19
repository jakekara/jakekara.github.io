---
layout: post
title: Scan and print QR code backups from the CLI
date: "2024-07-18 10:01:00 -0400"
categories: python
emoji: 🔑
---

I made this CLI tool for scanning QR codes and printing them out.

Here's the repo: [https://github.com/jakekara/totp-qr-backup/](https://github.com/jakekara/totp-qr-backup/)

This program uses your webcam. Each time you scan a two-factor
QR code, it saves the data from the code in a folder. This is designed
for you to copy the entire contents of your phone's QR code vault
in an efficient manner. Once that's done, you can export the saved data
to a printable PDF and stick it in a drawer or a fire safe somewhere
and delete the local files.

The risk of having these codes stolen from a physical location in 
coordination with also stealing my passwords is extremely small for me, but
for some users with different threat models, this may not be the case.

The far greater risk for me was losing my phone and not having all my
two-factor codes backed up somewhere. Now that I have them all printed out,
if my phone breaks or is stolen/lost, I can just install a QR vault on
a new phone and quickly scan these codes back in.