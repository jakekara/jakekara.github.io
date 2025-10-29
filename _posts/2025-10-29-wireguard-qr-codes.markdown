---
layout: post
title: Generating QR codes to configure Wireguard Clients
date: "2025-10-28 10:00:00 -0400"
categories: bash
emoji: 🔌
---

Here's how I generate QR codes to set up client devices (phones and laptops) for my home WireGuard VPN.

This blog post assumes you already have a WireGuard network set up and doesn't get into how to do that. It's just about configure clients easily.

### Generate a key pair

In this section we're going to generate cryptographic credentials and a config file that can be used to set up a WireGuard client. We're going to package them up in a QR code so you can just scan the entire config into a phone.

> **Warning:** Please note that the files we generate here are sensitive -- they're passwords essentially. So you should make sure you're working in a private space, especially before displaying the QR code on your screen, and you should delete these files when you're done with them.

I'm assuming you're on Linux or MacOS, but this might work in windows PowerShell. Maybe someone with Windows can tell me.

```
wg genkey | tee user_privatekey | wg pubkey > user_publickey
```

This will result in two files being generated: `user_privatekey` and `user_publickey`, each with one half of the key pair.

Now make a file called `wgconfig.ini`, that looks like this. Replace the ALL\_CAPS values with their actual values.

```ini
[Interface]
PrivateKey = USER_PRIVATE_KEY
Address = 10.0.1.7/32  # Ensure this IP is unique and within your subnet
DNS = 192.168.0.110 # Optional DNS server.

[Peer]
PublicKey = USER_PUBLIC_KEY
Endpoint = HOME_NETWORK_IP_ADDRESS:HOME_NETWORK_WIREGUARD_PORT
AllowedIPs = 0.0.0.0/0  # All traffic routed through WireGuard
```

Your Address, DNS, and AllowedIPs may need to be adjusted based on how your wireguard network is configured. The main takeaway from the example config above is where to put the public and private key you just generated.

You could give this .ini file to someone who want to allow to access your network, but if we're setting up a phone, the setup is even easier if we turn it into a QR code.

Do that with this command. If you don't have `qrencode` installed, your package manager will probably offer to install it for you.

```shell
qrencode -o wireguard_qr.png < wgconfig.ini
```

This will make a file called `wireguard_qr.png` that we can scan on our phone's Wireguard client if it supports QR codes. WG Tunnel for Anrdoid does.

### Set up the router

Before we set up the phone, we need to add a peer with the public key we just generated. Make sure you use the public key from the `user_public_key` file, and make `Allowed Addresses` match the `Interface.Address` from the .ini file.

### Set up the phone

Finally, open up your Wireguard client. I use WG Tunnel, which supports scanning a QR code. In WG Tunnel, tap the `+` icon and chose "Add from QR code", then scan the PNG from your computer screen. That's it! Save the new tunnel and you're ready to connect.