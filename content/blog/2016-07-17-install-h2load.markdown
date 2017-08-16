---
title: "http/2ベンチマークツール「h2load」をインストール"
date: 2016-07-17T20:19:21+09:00
comments: true
category: ['Tech']
tags: ['h2load','h2o']
published: true
slug: install-h2load
img: https://farm6.staticflickr.com/5624/21367186743_cbcb0e5268_m.jpg
---

![4 Good Reasons for Using HTTP/2](https://farm6.staticflickr.com/5624/21367186743_cbcb0e5268_z.jpg?zz=1 "4 Good Reasons for Using HTTP/2")

[4 Good Reasons for Using HTTP/2 / Tsahi Levent-Levi](https://www.flickr.com/photos/86979666@N00/21367186743/ "4 Good Reasons for Using HTTP/2 / Tsahi Levent-Levi")

<!--more-->
{{% googleadsense %}}

今、このブログは静的サイトジェネレータ`hugo`で作成したhtmlファイルを、`nginx`で公開しています。また、別のサイトは、`nginx`+`wordpress`で運営しています。

今気になっているのは、`h2o`と呼ばれているWebサーバです。`nginx`から`h2o`に変えた場合、どのぐらい早くなるのか？そもそも、今の段階でどのぐらいのリクエストを捌けているのか？という疑問を解消するために、まずはベンチマークを取ろうと、ベンチマークツールを整備しました。


## 各種ベンチマークツール

- ab
- wrk
- h2load

真っ先に思い浮かぶのは、`ab`コマンドです。昔もapacheとnginxの比較をしようとしたときに使いました。[abコマンド実行時のエラーを回避する \- SIS Lab](https://meganii.com/blog/2013/05/27/benchmark-apache/)

`ab`コマンドよりも、モダンなのは、`wrk`らしいです。[HTTP ベンチマークツール wrk についてメモ \| Siguniang's Blog](https://siguniang.wordpress.com/2015/06/21/notes-on-wrk-http-benchmarking-tool/)
[GitHub \- wg/wrk: Modern HTTP benchmarking tool](https://github.com/wg/wrk)


`wrk`も便利そうなのですが、http/2プロトコルに対応していません。

[Webサーバのベンチマークツールはh2loadが便利 \- 人間とウェブの未来](http://hb.matsumoto-r.jp/entry/2016/01/14/114048)
[h2load を使おう \- あどけない話](http://d.hatena.ne.jp/kazu-yamamoto/20151225/1451287148)

上記のサイトを参考に`h2load`が便利そうなので、インストールしてみます。brewともyumでもインストールはできないみたいなので、自前でビルドします。


## `h2load`のインストール

まず、ローカルのMacにインストールを試してみたのですが、うまくビルドまで辿り着きませんでした。次に、VirtualBoxのCentOS6.4に入れてみようとしたのですが、同じく行き詰まり、結局Ubuntuの環境を作ってインストールしました。

メモ書きと共に残しておきますが、的はずれなことを書いているかもしれないので注意してください。


## Ubuntu Server 14.04を vagrantで構築

[Discover Vagrant Boxes \| Atlas by HashiCorp](https://atlas.hashicorp.com/boxes/search)でUbuntu Server 14.04を探して、vagrantからプロビジョニングします。

Official Ubuntu Server 14.04 LTS (Trusty Tahr) builds

```
vagrant init ubuntu/trusty64; vagrant up --provider virtualbox
```

### ビルドに必要なパッケージのインストールと、spdylayのビルド
```
mkdir -p /usr/local/src
cd /usr/local/src
git clone https://github.com/tatsuhiro-t/spdylay #spdylayが必要なため

#必要なパッケージをインストール
sudo apt-get install autoconf automake autotools-dev libtool pkg-config zlib1g-dev libcunit1-dev libssl-dev libxml2-dev libevent-dev
cd spdylay/
autoreconf -i
automake
autoconf
./configure
make
make install
```

### nghttp2をビルド
```
cd /usr/local/src/
git clone https://github.com/nghttp2/nghttp2     #h2loadはnghttp2に同梱されているため
cd nghttp2/
autoreconf -i
automake
autoconf
./configure
make
make install
```

これでh2loadが利用可能になりましたが、`h2load`コマンドを叩くと以下のエラーが起きました。

```
h2load: error while loading shared libraries: libspdylay.so.7: cannot open shared object file: No such file or directory
```

これを解決するには、`ldconfig`コマンドを実行します。
```
ldconfig
```

### インストール完了

```
h2load -n100000 -c100 -m100 https://meganii.com/
starting benchmark...
spawning thread #0: 100 total client(s). 100000 total requests
TLS Protocol: TLSv1.2
Cipher: ECDHE-RSA-AES128-GCM-SHA256
Application protocol: h2
progress: 10% done
progress: 20% done
progress: 30% done
progress: 40% done
progress: 50% done
progress: 60% done
progress: 70% done
progress: 80% done
progress: 90% done
progress: 100% done

finished in 1057.51s, 94.56 req/s, 5.97MB/s
requests: 100000 total, 100000 started, 100000 done, 98534 succeeded, 1466 failed, 0 errored, 0 timeout
status codes: 98534 2xx, 0 3xx, 0 4xx, 1466 5xx
traffic: 6.16GB (6617383053) total, 1.56MB (1634036) headers (space savings 90.77%), 6.16GB (6610382710) data
                     min         max         mean         sd        +/- sd
time for request:      2.05s     305.07s      99.06s      53.36s    68.82%
time for connect:   209.74ms       1.72s       1.23s    360.78ms    54.00%
time to 1st byte:      1.02s       3.18s       1.70s    565.46ms    55.00%
```


## まとめ

ただ単純にhttp/2プロトコルに対応したベンチマークツールを入れたいだけだったのに、かなり苦労しました。
