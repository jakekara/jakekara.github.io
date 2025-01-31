---
layout: post
title: synology-email-ip-changes
date: "2025-01-29 10:00:00 -0400"
categories: bash
emoji: 📠
---

Here's a shell script I use to make my Synology email me
whenever my home IP address changes.

Synology's Task Scheduler can run a script on a schedule,
with an option to email you if the task fails (exits with non-zero
code).

So what this script does specifically is check my public IP using
[ipinfo.io/io](https://ipinfo.io/ip), and if the IP is different
from the last time it checked, it prints the new IP and exits
with an error code, causing the Synology to send me the entire
output, which includes the new IP.

```bash
set -e 
touch ip.txt

IP=$(curl -s ipinfo.io/ip)
OLD_IP=$(cat ip.txt)

if [ "$IP" = "$OLD_IP" ]; then
    echo "IP ADDRESS UNCHANGED: $IP"
else
    echo "IP ADDRESS CHANGED: $IP (Was $OLD_IP)"
    echo $IP > ip.txt
    exit 1
fi
```
