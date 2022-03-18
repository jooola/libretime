---
title: Reverse proxy
sidebar_position: 30
---

This guide walk you though the steps required to setup a reverse proxy in front of LibreTime.

Setting a reverse proxy in front of LibreTime is recommended, it prevents LibreTime to be
open to the Internet, adds security by enabling `https` and can hide private ports or urls
from the public.

Using a single place to manage your `ssl/tls` certificates simplify
their management and will be less prone to errors.

<!-- In some deployments, the LibreTime server is deployed behind a reverse proxy,
for example in containerization use-cases such as Docker and LXC. LibreTime
makes extensive use of its API for some site features, which causes
[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
to occur. By default, CORS requests are blocked by your browser and the origins
need to be added to the **Allowed CORS URLs** block in
[**General Settings**](../../user-manual/settings.md). These origins should include any
domains that are used externally to connect to your reverse proxy that you
want handled by LibreTime. These URLS can also be set during the first run configuration
that's displayed when you first install LibreTime

### Reverse proxy basics

A reverse proxy allows the LibreTime server to not be connected to the open internet. In
this configuration, it's rather behind another server that proxies traffic to it from
users. This provides some advantages in the containerization space, as this means that
the containers can be on their own internal network, protected from outside access.

A reverse proxy also allows SSL to be terminated in a single location for multiple sites.
This means that all your traffic to the proxy from clients is encrypted, but the reverse
proxy's traffic to the containers on the internal network isn't. All the SSL certificates
live on the reverse proxy and can be renewed there instead of on the individual
containers. -->

## Prerequisites

For common setups it is recommended to use 2 domains, one for LibreTime (`radio.example.com`) and one for Icecast (`stream.example.com`).

To enable `https`, you also need a ssl/tls certificate, you can get a certificate from Let's Encrypt by using [Certbot](https://certbot.eff.org/).

You need to identify the location of the services that should be exposed to the public:

- the LibreTime web server (usually `localhost:8080`, for documentation clarity we use `libretime:8080`),
- the Icecast server (usually `localhost:8000`, for documentation clarity we use `icecast:8000`).

:::info

If LibreTime is running on the same host as the reverse proxy, you need to change the LibreTime web server default listening port `80` because the reverse proxy needs to listen on the `80`and `443` ports.

:::

:::caution

Be sure that your firewalls and network configurations allows communications from the reverse proxy to the services.

You can use `ping` to check for network communications, `telnet` to check for open ports and finally `curl` or `wget` to check for http communications.

:::

## Install a reverse proxy

### Apache

### Nginx

On `localhost`, run the following:

```bash
cat << EOF | sudo tee /etc/nginx/sites-available/libretime.conf
server {
    listen 80;
    server_name libretime.example.com;
    location / {
        rewrite ^ https://$server_name$request_uri? permanent;
    }
}
server {
    listen 443 ssl;
    server_name libretime.example.com;
    ssl_certificate /etc/letsencrypt/live/libretime.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/libretime.example.com/privkey.pem;
    add_header Strict-Transport-Security "max-age=15552000;";
    add_header X-Frame-Options "SAMEORIGIN";
    client_max_body_size 512M;
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass http://192.168.1.10/;
    }
}
EOF
```

This Nginx configuration ensures that all traffic uses SSL to the reverse proxy, and
traffic is proxied to `192.168.1.10`.

### HAProxy

## Icecast

Once it has installed, replace `<hostname>localhost</hostname>` in `/etc/icecast2/icecast.xml` with the following:

```xml
<hostname>icecast.example.com</hostname>
```

This is the hostname that people listening to your stream will connect to and what
LibreTime will use to stream out to them. You will then need to restart Icecast using `sudo systemctl restart icecast2`.

Next, the SSL certificate needs to be generated and the site activated.

```
sudo apt install certbot
sudo systemctl stop nginx
sudo certbot certonly -d libretime.example.com -a standalone
sudo systemctl start nginx
```

You can now go to `https://libretime.example.com` and go
through the installer. On `General Settings`, you need to change the Webserver Port to
`443` and add the following CORS URLs:

```
https://libretime.example.com
http://libretime.example.com
https://localhost
http://localhost
```

Finally, the configuration file needs updating. Under `[general]`, `force_ssl`
needs to be set to true:

```ini
[general]
...
force_ssl = true
```

## Mixed encrypted and unencrypted content

Whether your certificate is self-signed or not, you will see browser security warnings whenever a https:// page is delivering unencrypted content, such as the stream from an Icecast server. In Firefox, an exclamation mark icon is displayed in the address bar of the **Listen** pop-up.
