---
title: "Lets's Encryptの証明書期限切れへの対応と、ドメイン紐付けの適正化"
date: 2016-07-09T08:06:50+09:00
lastmod: 2017-01-11T22:17:50+09:00
comments: true
category: ['Tech']
tags: ['https', 'SSL', 'Lets Encrypt']
published: true
slug: invalid-ssl-certificate
img: "/images/le-logo-standard.png"
---

[![https://gyazo.com/aa727ee506684862329b98313fcce28a](https://i.gyazo.com/aa727ee506684862329b98313fcce28a.png)](https://gyazo.com/aa727ee506684862329b98313fcce28a)


この[meganii.com](https://meganii.com)は、Lets's Encryptで証明書を発行しています。しばらくは、仕組みがよく分かっていないので手動で更新しようと、3ヶ月に一回は更新するようにしていたのですが、ついに昨日、証明書の期限切れでアクセス出来ない状態になりました。。。(なんというお間抜けな話)

慌てて、certbotを実行させ、更新しようとしたのですが、前回の更新が上手くいっていなかったみたいでrenewできませんでした。

古い証明書を消して、新規で発行すればできたのでそのメモを残しておきます。

<!--more-->
{{% googleadsense %}}

## 前提

- CentOS release 6.8 (Final)
- Web Server: nginx


## 失敗その1 なぜかhttpdが起動している

```
$ sudo service nginx stop

$ ./certbot-auto renew --dry-run
Requesting root privileges to run certbot...
  /home/xxxxx/.local/share/letsencrypt/bin/letsencrypt renew --dry-run
  /home/xxxxx/.local/share/letsencrypt/lib/python2.6/site-packages/cryptography/__init__.py:26: DeprecationWarning: Python 2.6 is no longer supported by the Python core team, please upgrade your Python. A future version of cryptography will drop support for Python 2.6
  DeprecationWarning

-------------------------------------------------------------------------------
Processing /etc/letsencrypt/renewal/meganii.com.conf
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
The program httpd (process ID 15164) is already listening on TCP port 80. This
will prevent us from binding to that port. Please stop the httpd program
temporarily and then try again. For automated renewal, you may want to use a
script that stops and starts your webserver. You can find an example at
https://letsencrypt.org/howitworks/#writing-your-own-renewal-script.
Alternatively you can use the webroot plugin to renew without needing to stop
and start your webserver.
-------------------------------------------------------------------------------
2016-07-08 22:51:05,774:WARNING:certbot.renewal:Attempting to renew cert from /etc/letsencrypt/renewal/meganii.com.conf produced an unexpected error: At least one of the (possibly) required ports is already taken.. Skipping.

** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates below have not been saved.)

All renewal attempts failed. The following certs could not be renewed:
  /etc/letsencrypt/live/meganii.com/fullchain.pem (failure)
   DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates above have not been saved.)
1 renew failure(s), 0 parse failure(s)

IMPORTANT NOTES:
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
```

上記履歴は、一部抜粋しています。

80番portが開いているため、エラーとなっていました。httpdは、止めたはずと思っていたのですが何かのキッカケで起動状態にあったみたいです。
`sudo service httpd stop`を実行して、サービスを止めます。


## 失敗その2 なぜか前回更新時に、異なるドメインと紐付いてしまっていた

後は、単純に`certbot-auto renew`を実行すればよいはずが、なぜかドメインが違うと怒られてしまいました。(おそらく前回更新したときに変なことをしたのだと思います)

```
$ ./certbot-auto renew --dry-run
Requesting root privileges to run certbot...
  /home/xxxxx/.local/share/letsencrypt/bin/letsencrypt renew --dry-run
  /home/xxxxx/.local/share/letsencrypt/lib/python2.6/site-packages/cryptography/__init__.py:26: DeprecationWarning: Python 2.6 is no longer supported by the Python core team, please upgrade your Python. A future version of cryptography will drop support for Python 2.6
  DeprecationWarning

-------------------------------------------------------------------------------
Processing /etc/letsencrypt/renewal/meganii.com.conf
-------------------------------------------------------------------------------
2016-07-08 23:04:54,638:WARNING:certbot.renewal:Attempting to renew cert from /etc/letsencrypt/renewal/meganii.com.conf produced an unexpected error: Failed authorization procedure. xxxxxxxxxx.com (tls-sni-01): urn:acme:error:connection :: The server could not connect to the client to verify the domain :: Failed to connect to 192.64.147.141:443 for TLS-SNI-01 challenge. Skipping.

** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates below have not been saved.)

The following certs could not be renewed:
  /etc/letsencrypt/live/meganii.com/fullchain.pem (failure)
** DRY RUN: simulating 'certbot renew' close to cert expiry
**          (The test certificates above have not been saved.)
1 renew failure(s), 0 parse failure(s)

IMPORTANT NOTES:
 - The following errors were reported by the server:

   Domain: recommented.com
   Type:   connection
   Detail: Failed to connect to 192.64.147.141:443 for TLS-SNI-01
   challenge

   To fix these errors, please make sure that your domain name was
   entered correctly and the DNS A record(s) for that domain
   contain(s) the right IP address. Additionally, please check that
   your computer has a publicly routable IP address and that no
   firewalls are preventing the server from communicating with the
   client. If you're using the webroot plugin, you should also verify
   that you are serving files from the webroot path you provided.
```

## 解決方法

管理者権限で、以下のフォルダに格納されているエラーに関係していそうなフォルダを削除します。

- `/etc/letsencrypt/live/`
- `/etc/letsencrypt/archive/`
- `/etc/letsencrypt/renewal/`

例えば、`/etc/letsencrypt/live/`だと、meganii.com以外に、meganii.com-0001なんていうのもできていました。

```
$ su
$ cd /etc/letsencrypt/live/
rm -rf meganii.com/
rm -rf meganii.com-0001/
rm -rf xxxxxxx.com/
```

一通り消し終わった後、以下の通り、新規発行を行いました。

## 新規発行

以下の通り、最終的にうまく発行できました。

```
$ ./certbot-auto certonly --standalone -d meganii.com
Requesting root privileges to run certbot...
  /home/xxxxx/.local/share/letsencrypt/bin/letsencrypt certonly --standalone -d meganii.com
  /home/xxxxx/.local/share/letsencrypt/lib/python2.6/site-packages/cryptography/__init__.py:26: DeprecationWarning: Python 2.6 is no longer supported by the Python core team, please upgrade your Python. A future version of cryptography will drop support for Python 2.6
  DeprecationWarning
Version: 1.1-20080819
Version: 1.1-20080819

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/meganii.com/fullchain.pem. Your cert will
   expire on 2016-10-06. To obtain a new or tweaked version of this
   certificate in the future, simply run certbot-auto again. To
   non-interactively renew *all* of your certificates, run
   "certbot-auto renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

$ sudo service nginx restart
nginx を停止中:                                            [失敗]
nginx を起動中:                                            [  OK  ]
```
 ※　xxxxxの部分は、差し替え


## 参考

[Certbot](https://certbot.eff.org/#centosrhel6-nginx)


## 所感

前回やったことは、このブログに書いたはず。でも、そういやアクセスできないじゃないか。と思いましたが、ローカルにMarkdownファイルがあるので安心して参照できました。下手にDBを持ってないので、こういうときに便利だなと実感しました。

自動化しとかないとなぁ・・・。
