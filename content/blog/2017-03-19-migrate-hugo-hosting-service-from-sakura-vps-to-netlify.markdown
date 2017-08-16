---
title: "Hugoで生成した静的サイトのホスト先をさくらVPSからNetlifyに変更する"
date: 2017-03-19T19:46:06+09:00
lastmod: 2017-07-23T21:46:06+09:00
comments: true
category: ['Tech']
tags: ['Netlify','Hugo']
published: true
slug: migrate-hugo-hosting-service-from-sakura-vps-to-netlify
img: "/images/2017/03/netlify-64x.png"
---

現在(2017/3月)、Hugoで生成した静的サイトをホストするためにさくらVPSを利用しています。さくらVPSは２年近く使ってきましたが、そろそろ更新時期した(1年まとめて契約しているため)。自分が契約したタイプはデイスクがHDDのままSSDに変更できないタイプだったので、新規契約し直すか、Conoha VPSに切り替えるか、それともVPS自体を契約しないとするか迷っています。

良い機会であるため、静的サイトのホスティングをVPSではなくクラウドサービスを利用しようと検討しました。

## 移行先検討

- GitHub Pages
- Netlify

自分の中では`Github Pages`か`Netlify`の2択でした。静的サイトのコンテンツはGitHubにコミットしているため、最初は、`Github Pages`にしようとしていました。しかし、現状HTTP/2に対応していないことからあまり気乗りしませんでした。もともとVPSを利用していたときには、[Lets's Encryptでブログの常時SSL化にチャレンジ](https://www.meganii.com/blog/2016/01/17/lets-encrypt-always-on-ssl/)のように、常時SSLに対応したり、h2oをインストールしてなんとかHTTP/2に対応した経緯もあり、せっかくなら対応できると嬉しいです。

その点、`Netlify`を試してみたら「これで決まり！」と思うぐらい良かったのでまずはNetlifyで運用してみます。

![Netlify](/images/2017/03/netlify.png)

[Netlify: All\-in\-one platform for automating modern web projects](https://www.netlify.com/)

<!--more-->
{{% googleadsense %}}

Netlifyを気に入ったポイントは以下の点です。

- 簡単に、独自ドメイン(Custom Domain)が設定できる
- 簡単に、SSL対応できる
- 簡単に、グローバルCDNを導入できる
- HTTP/2サポート
- Hugoビルドまで面倒みてくる
- CIツールからの連携も可能

## Netlifyとは？

> Write frontend code. Push it. We handle the rest.

Netlifyとは、「フロントエンドのコードを書いたら、Pushすれば後はお任せ」という通り、フロントエンドのデプロイ・ビルド・ホスティングを全て面倒をみてくれるプラットフォームです。

> Deploy modern static websites with our automated platform. Add best practices like SSL, CDN distribution, caching and continuous deployment with a single click.



## カスタムドメインの設定方法

Netlifyにデプロイ後のURL`meganii.netlify.com`を`www.meganii.com`で運用したい場合の例です。

`www.meganii.com`にCNAMEを設定して、`meganii.netlify.com`に向けます。


### お名前.comでの設定

[![https://gyazo.com/eaf25edb2d5651e71390d1628ba251e7](https://i.gyazo.com/eaf25edb2d5651e71390d1628ba251e7.png)](https://gyazo.com/eaf25edb2d5651e71390d1628ba251e7)

[![https://gyazo.com/4e99fdafdd37adab30566e53e9178386](https://i.gyazo.com/4e99fdafdd37adab30566e53e9178386.png)](https://gyazo.com/4e99fdafdd37adab30566e53e9178386)

[![https://gyazo.com/e3c5bb60261f013da52681701f5dfdb2](https://i.gyazo.com/e3c5bb60261f013da52681701f5dfdb2.png)](https://gyazo.com/e3c5bb60261f013da52681701f5dfdb2)




### app.netlify.comでの設定

Custom domainを設定して、その後、HTTPSを有効にします。

[![https://gyazo.com/41f8e3a985be8d5269d65bd37acc77ac](https://i.gyazo.com/41f8e3a985be8d5269d65bd37acc77ac.png)](https://gyazo.com/41f8e3a985be8d5269d65bd37acc77ac)

[![https://gyazo.com/2c7a4eb88b49fb741985881b76ec3a42](https://i.gyazo.com/2c7a4eb88b49fb741985881b76ec3a42.png)](https://gyazo.com/2c7a4eb88b49fb741985881b76ec3a42)


## リダイレクト処理

カスタムドメインを設定しても、元々の`*.netlify.com`にはアクセスできてしまうので、Google的には重複コンテンツと見なされるのではないか？とちょっと心配になったので、以下の通りリダイレクトを`_redirects`ファイルに設定しました。

注意点は、`public`フォルダ直下に配置しないといけない点です。(最初、rootに置けばよいだけど思っていましたが、よくよく考えればその通りですね)

`_redirects`ファイルにRedirect処理を書くことができます。

[Go Static Without Losing Your Server \| Netlify](https://www.netlify.com/blog/2016/03/10/go-static-without-losing-your-server/)


> However, if you’re 100% sure that you’ll always want to redirect, even when the URL matches a static file, you can append an exclamation mark to the rule:
```
/app/*  /app/index.html  200!
```

```_redirects
https://meganii.netlify.com/* https://meganii.com/:splat 301!
http://meganii.netlify.com/* https://meganii.com/:splat 301!
```

`:splat`は、ワイルドカードのように使うみたいです。

```
/news/*  /blog/:splat
```

上記の設定だと、以下の通りリダイレクトされます。

`/news/2004/01/10/my-story` to `/blog/2004/01/10/my-story`

## NetlifyでHugoを使うときの注意点

デフォルトだと、HugoのVersionは`1.7`ですが、`hugo_0.19`というbuild commandを利用することで、`1.9`のバージョンを利用できます。

## _headers

~~`_headers`は、無料プランでは利用できないみたいです。~~

2017/07/23 追記

[HTTP/2 Server Push on Netlify \| Netlify](https://www.netlify.com/blog/2017/07/18/http/2-server-push-on-netlify/)の提供によって、無料プランでもheadersが利用できるようになりました。



## ビルドにNetlify以外のCIツールを利用する場合

NetlifyのAPIを利用することで、Manual Deployが可能なため、CIツールからデプロイすることが可能です。
CircleCIの場合は、以下の通り`circle.yml`に記載します。

```
deployment:
  master:
    branch: master
    commands:
      - npm install netlify-cli
      - hugo -t hugo-zen
      - node_modules/.bin/netlify deploy -t "$netlify_token"
```

## 参考

- [高機能ホスティングサービスNetlifyについて調べて使ってみた \- Qiita](http://qiita.com/TakahiRoyte/items/b7c4d1581df1a17a93fb)
- [Netlifyは最強の静的ウェブサイトホスティングサービスかもしれない \- yoshidashingo](http://yoshidashingo.hatenablog.com/entry/2016/08/22/193821)
- [Netlifyを使ってブログをHTTPS化する \| Aimless](http://aimless.jp/blog/archives/2016-11-18-enable-https-by-netlify/)
- [Hugo on Netlify \- tips & tricks \- Hugo Discussion](https://discuss.gohugo.io/t/hugo-on-netlify/1505/13)
