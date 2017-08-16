---
title: "lets encrypt certbot"
date: 2016-05-15T21:02:12+09:00
comments: true
category: ['Tech']
tags: ['https', 'SSL', 'Lets Encrypt']
published: true
slug: lets-encrypt-certbot
---

[Lets's Encryptでブログの常時SSL化にチャレンジ - SIS Lab](https://meganii.com/blog/2016/01/17/lets-encrypt-always-on-ssl/)の方法で新しいドメインを認証しようとすると、モジュールが古いから新しいモジュールを利用してねと怒られました。

<!--more-->
{{% googleadsense %}}

改めて、[Getting Started - Let's Encrypt - Free SSL/TLS Certificates](https://letsencrypt.org/getting-started/)を見ながら、クライアントソフトを入れなおして、再度発行を行いました。

## クライアントソフトをインストール

```
git clone https://github.com/certbot/certbot
cd certbot
./certbot-auto --help
```

certbotになったみたいです。裏で、botちゃんが動いて証明書を発行していることを想像しました。

## 証明書発行

```
sudo service nginx stop # webサーバを止める
certbot certonly --standalone -d meganii.com
```

これで、問題なく証明書を発行できました。cronなどで、定期的に更新している人は、設定を変えないといけない可能性があるので注意してください。
