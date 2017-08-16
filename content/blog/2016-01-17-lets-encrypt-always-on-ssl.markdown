---
title: "Lets's Encryptでブログの常時SSL化にチャレンジ"
date: 2016-01-17T22:44:45+09:00
comments: true
category: ['Tech']
tags: ['https', 'SSL', 'Lets Encrypt']
published: true
slug: lets-encrypt-always-on-ssl
img: "https://images-na.ssl-images-amazon.com/images/I/511NShYrT8L._SL160_.jpg"
---

管理画面とか、APIのエンドポイントを作るためになんとなく、httpsにしておきたいと常々思ってたので、無料で証明書を発行できるLets's Encryptを利用して、これを機にブログも常時SSL化を目指した。

基本的には、提供されるLet's Encryptのコマンドを叩いて、画面の指示に従っていけば、証明書を発行することが出来た。こんなことなら、もっと早く着手すればよかったと思うぐらいである。その中でもハマった点は、Pythonのバージョンと、443のポートの開け忘れで、手順も含めて、忘れないようにメモしておく。


Lets's Encryptの使い方は、以下のサイトを参考にした。

- [How It Works - Let's Encrypt - Free SSL/TLS Certificates](https://letsencrypt.org/howitworks/)
- [Let's Encrypt の使い方 - Let's Encrypt 総合ポータル](https://letsencrypt.jp/usage/)
- [無料SSL証明書の Let’s Encrypt が公開されたので実際に試してみた | Webセキュリティの小部屋](http://www.websec-room.com/2015/12/04/2380)


{{% googleadsense %}}


## 環境

- CentOS6.4


## ハマったところ

### Pythonのバージョン

CentOS 6で標準インストールされているPythonのバージョンは、`2.6.6`と、Let’s Encryptのコマンドが要求するバージョンより古いため、実行すると以下のようなエラーが発生した。

`--debug`のオプションを付けることで、無理やり実行させることも出来るみたいだが、おとなしくバージョンを上げて対応した。

```
./letsencrypt-auto --help
WARNING: Python 2.6 support is very experimental at present...
if you would like to work on improving it, please ensure you have backups
and then run this script again with the --debug flag!
```

意外と、yumからpython27の情報がなかった。(みんなビルドしてるみたい)そのなかでも、欲しい情報が以下のページに載っていたので、参考にして、Python27をインストールした。

[CentOS6 で Let's Encrypt #letsencrypt - @bayashi Diary](http://bayashi.net/diary/2015/1124)

```
yum install centos-release-SCL
yum install python27 python27-python-tools
scl enable python27 bash
```


### SSLのポート(443)を空けていないため通信出来ない

以下のエラーが出た。これは、443ポートを開けていないため、エラーになっている模様。

```
./letsencrypt-auto certonly -a standalone -d meganii.com
Updating letsencrypt and virtual environment dependencies......
Requesting root privileges to run with virtualenv: /root/.local/share/letsencrypt/bin/letsencrypt certonly -a standalone -d meganii.com
Version: 1.1-20080819
Version: 1.1-20080819
Failed authorization procedure. meganii.com (tls-sni-01): urn:acme:error:connection :: The server could not connect to the client to verify the domain :: Failed to connect to host for DVSNI challenge, meganii.com (tls-sni-01): urn:acme:error:connection :: The server could not connect to the client to verify the domain :: Failed to connect to host for DVSNI challenge

IMPORTANT NOTES:
 - The following errors were reported by the server:

   Domain: meganii.com
   Type:   urn:acme:error:connection
   Detail: Failed to connect to host for DVSNI challenge
```

443のポートを開けるようにiptablesに設定を追加した。(以下は、ansibleのコマンド)

### /etc/sysconfig/iptables

```
- name: add iptables rule for https
  lineinfile: dest=/etc/sysconfig/iptables regexp="{{ https_port }}" line="-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport {{ https_port }} -j ACCEPT" insertbefore="^# add end" state=present

- name: iptables restart
  command: /etc/init.d/iptables restart
```

[【Let’s Encrypt】エラー表示「The server could not connect to the client to verify the domain」 | 鯖缶備忘録](http://blog.ctwnet.com/black/?p=231)




## 作業内容

ハマった点を先に記載し、作業順序とは逆転したのだが、作業内容は以下のとおり。

### 1. リポジトリからダウンロード

```
git clone https://github.com/letsencrypt/letsencrypt
```

### 2. テスト

以下のコマンドを実行すると、環境のチェックがされ、問題なければヘルプの情報が表示される。自分のCentOSの環境だと、Pythonのバージョンが古いため、警告が出た。

```
./letsencrypt-auto --help
```

#### エラーメッセージ

```
./letsencrypt-auto --help
WARNING: Python 2.6 support is very experimental at present...
if you would like to work on improving it, please ensure you have backups
and then run this script again with the --debug flag!
```

上記の「ハマった点 Python27」のインストール手順で、Python27をインストールした。


以下root権限で作業してます。

```
yum install centos-release-SCL
yum install python27 python27-python-tools
scl enable python27 bash
python -V
Python 2.7.5
```

Pythonのバージョンが上がったことを確認した後、再度以下のコマンドを実施すると、警告は出るがヘルプが出るようになった。(`scl enable`の動きと、Pythonのバージョンについては要確認)

```
./letsencrypt-auto --help
```


### 3. Let's Encryptクライアントの実行

次に、以下のコマンドを実行する。 `--email {自分のemailアドレス}`、`-d {対象ドメイン}`という指定方法である。

```
./letsencrypt-auto certonly --standalone --email email@mail.com -d meganii.com
```

途中でWebサーバを停止させるように指示があるため、nginx(Webサーバ)を停止させ、再度同じコマンドを実行する。
(このタイミングで、ポート443を空けておらず、いくらnginxを再起動させても、正常に動作しなかった)

```
service nginx stop
```

```
./letsencrypt-auto certonly --standalone --email email@mail.com -d meganii.com

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at
   /etc/letsencrypt/live/meganii.com/fullchain.pem. Your cert will
   expire on 2016-04-14. To obtain a new version of the certificate in
   the future, simply run Let's Encrypt again.
 - If you like Let's Encrypt, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le
```

これで、`/etc/letsencrypt/live/meganii.com/`の下に以下のファイルが作られる。これらの証明書を利用して、Nginxの設定を行う。

```
cert.pem       #サーバ証明書
chain.pem      #中間証明書
fullchain.pem  #サーバ証明書＋中間証明書
privkey.pem    #サーバ秘密鍵
```

## 4. nginxの設定

nginxの設定は、以下のブログを参考にした。

[Let's EncryptでHTTPSサーバを建てたついでにSSL LabsでA+評価をめざす - sonickun.log](http://sonickun.hatenablog.com/entry/2015/12/19/212517)


上記ブログの手順をもとに、DH鍵を生成する。

```
openssl dhparam -out dhparam.pem 2048
openssl dhparam -text -in dhparam.pem -noout
```


### default.confの設定

最終的に、下記の設定でNginxを走らせた。

```
#
# The default server
#

server {
  listen       80 default_server;
  server_name  meganii.com;
  return       301 https://meganii.com$request_uri;
}

server {

    listen 443 ssl http2;
    listen [::]:443 ssl http2;

    server_name  meganii.com;

    ssl_certificate      /etc/letsencrypt/live/meganii.com/fullchain.pem;
    ssl_certificate_key  /etc/letsencrypt/live/meganii.com/privkey.pem;

    ssl_session_timeout  10m;

    ssl_prefer_server_ciphers  on;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers "EECDH+ECDSA+AESGCM EECDH+aRSA+AESGCM EECDH+ECDSA+SHA384 EECDH+ECDSA+SHA256 EECDH+aRSA+SHA384 EECDH+aRSA+SHA256 EECDH+aRSA+RC4 EECDH EDH+aRSA RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DSS !RC4";

    ssl_dhparam /etc/nginx/ssl/dhparam.pem;

    add_header Strict-Transport-Security "max-age=15768000; includeSubdomains";

    #charset koi8-r;

    #access_log  logs/host.access.log  main;

    location / {
        root   /home/web/www/meganii.com;
        index  index.html index.htm;
    }

    error_page  404              /404.html;
    location = /404.html {
        root   /usr/share/nginx/html;
    }

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    gzip on;
    gzip_disable "msie6";

    gzip_comp_level 6;
    gzip_min_length  1100;
    gzip_buffers 16 8k;
    gzip_proxied any;
    gzip_types       text/plain application/xml text/css text/js text/xml application/x-javascript text/javascript application/javascript application/json    application/xml+rss;
}
```

下記は、httpでアクセスしてきた場合、httpsにリダイレクトする設定である。rewriteする方法もあるが、公式ページに "This is a wrong"と書いてあるので、推奨する方法を採用した。

```
server {
    listen       80;
    server_name  www.example.org  example.org;
    if ($http_host = example.org) {
        rewrite  (.*)  http://www.example.org$1;
    }
    ...
}
This is a wrong, cumbersome, and ineffective way. The right way is to define a separate server for example.org:
```

[Converting rewrite rules](http://nginx.org/en/docs/http/converting_rewrite_rules.html)


## 参考

- [Let's Encrypt の使い方 - Let's Encrypt 総合ポータル](https://letsencrypt.jp/usage/)
- [無料SSL証明書の Let’s Encrypt が公開されたので実際に試してみた | Webセキュリティの小部屋](http://www.websec-room.com/2015/12/04/2380)
- [CentOS6 で Let's Encrypt #letsencrypt - @bayashi Diary](http://bayashi.net/diary/2015/1124)
- [Let's EncryptでHTTPSサーバを建てたついでにSSL LabsでA+評価をめざす - sonickun.log](http://sonickun.hatenablog.com/entry/2015/12/19/212517)

<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774178667/meganii-22/" target="_blank" ><img src="https://images-na.ssl-images-amazon.com/images/I/511NShYrT8L._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774178667/meganii-22/" target="_blank" >nginx実践入門 (WEB+DB PRESS plus)</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">久保 達彦,道井 俊介 技術評論社 2016-01-16    </div><div class="booklink-link2"><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774178667/meganii-22/" target="_blank" >Amazon</a></div><div class="shoplinkkindle"><a href="http://www.amazon.co.jp/gp/search?keywords=nginx%8E%C0%91H%93%FC%96%E5%20%28WEB%2BDB%20PRESS%20plus%29&__mk_ja_JP=%83J%83%5E%83J%83i&url=node%3D2275256051&tag=meganii-22" target="_blank" >Kindle</a></div><div class="shoplinkrakuten"><a href="http://hb.afl.rakuten.co.jp/hgc/13e181b2.b5761023.13e181b3.cbc7b217/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F13530382%2F%3Fscid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2Fev%2Fbook%2F" target="_blank" >楽天ブックス</a></div>                  	  	  	      </div></div><div class="booklink-footer"></div></div>
