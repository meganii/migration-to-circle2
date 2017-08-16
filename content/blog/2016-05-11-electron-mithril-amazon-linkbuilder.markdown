---
title: "Electronがv1.0.0になったのでMithril.jsと合わせてAmazonアフィリエイトリンクビルダーを作った"
date: 2016-05-11T22:05:30+09:00
comments: true
category: ['Tech']
tags: ['electron', 'mithril.js', 'JavaScript']
published: true
slug: electron-mithril-amazon-linkbuilder
img: "https://farm8.staticflickr.com/7085/26951293955_748076b816_q.jpg"
---

Electronが[Electron 1.0](http://electron.atom.io/blog/2016/05/11/electron-1-0)になったということで、以前作ったAmazon LinkbuilderをMithril.jsで置き換えてみました。(Electron v1.0.0がなったことはあまり関係ありません。。。)

{{% googleadsense %}}

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/35571855@N06/26951293955/in/dateposted-public/" title="Electron-LinkBuilder"><img src="https://farm8.staticflickr.com/7085/26951293955_748076b816_z.jpg" width="640" height="441" alt="Electron-LinkBuilder"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

以前の記事「[ElectronでAmazonアフィリエイトリンクビルダーを作った - SIS Lab](https://meganii.com/blog/2016/02/20/electron-amazon-link-builder/)」で、Electronと素のJavaScriptでAmazonアフィリエイトリンクビルダーを作成しました。

Amazonから商品を検索するAmazon Product Advertising APIの使い方と、そのJavaScriptラッパーの`node-apac`の使い方は、この記事を参照してください。


## Mithril.js

Electron + Mithril.jsの組み合わせは、[Electron + Mithril.jsでFlickrアプリを作成する - SIS Lab](https://meganii.com/blog/2016/02/28/electron-mithriljs-flickr-app/) のときに試しました。使うAPIもコアとなるのは5つ、全部合わせても10数個とシンプルなため、個人的には、VirtualDOM入門にはとっつきやすいと感じました。世間的には、React.jsなんでしょうけどね。

素のJavaScriptを、書き直しました。Model, Controller, ViewModel, Viewの使い方がまだイマイチ分かっていませんが、動くところまではいきました。


## 作成したプログラム

[meganii/electron-amazon-linkbuilder: Amazon Affiliate Link Builder built on Electron with Mithril.js](https://github.com/meganii/electron-amazon-linkbuilder)



package.json を以下の通り、1.0.0以上を指定すればよいみたい。(おそらくなので、あまり分かっていない)

```diff
},
 "homepage": "https://github.com/meganii/electron-amazon-linkbuilder#readme",
 "devDependencies": {
-    "electron-prebuilt": "^0.36.0",
+    "electron-prebuilt": "^1.0.0",
   "mithril": "^0.2.4",
   "config": "^1.20.0",
   "apac": "1.5.0"
```

## 参考

(さっそく、作ったAmazonアフィリエイトリンクビルダーで商品リンクを作りました笑)

<div class="booklink-box"><div class="booklink-image"><a href=http://www.amazon.co.jp/JavaScript-Ninja%E3%81%AE%E6%A5%B5%E6%84%8F-%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E9%96%8B%E7%99%BA%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E7%9F%A5%E8%AD%98%E3%81%A8%E3%82%B3%E3%83%BC%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0-Programmers-SELECTION/dp/4798128457%3FSubscriptionId%3DAKIAI6MZOKQQCKBKJBLQ%26tag%3Dmeganii-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4798128457><img src="https://images-na.ssl-images-amazon.com/images/I/51wsFoSKrKL._SL160_.jpg" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4798128457/meganii-22/">JavaScript Ninjaの極意 ライブラリ開発のための知識とコーディング (Programmer's SELECTION)</a></div><div class=shoplinkrakuten><a href="http://hb.afl.rakuten.co.jp/hgc/g00q0725.il1o2897.g00q0725.il1o3b57/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F12337610%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Frms%2Fmsv%2FItem%3Fn%3D12337610%26surl%3Dbook">楽天で買う</a></div></div></div>

<div class="booklink-box"><div class="booklink-image"><a href=http://www.amazon.co.jp/JavaScript-%E7%AC%AC6%E7%89%88-David-Flanagan/dp/4873115736%3FSubscriptionId%3DAKIAI6MZOKQQCKBKJBLQ%26tag%3Dmeganii-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4873115736><img src="https://images-na.ssl-images-amazon.com/images/I/51c9uCrhHgL._SL160_.jpg" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4873115736/meganii-22/">JavaScript 第6版</a></div><div class=shoplinkrakuten><a href="http://hb.afl.rakuten.co.jp/hgc/g00q0725.il1o2897.g00q0725.il1o3b57/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F11846204%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Frms%2Fmsv%2FItem%3Fn%3D11846204%26surl%3Dbook">楽天で買う</a></div></div></div>
