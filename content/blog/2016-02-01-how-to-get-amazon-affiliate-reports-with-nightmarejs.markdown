---
title: "Nightmare.jsでAmazonアフィリエイトのレポートを取得する"
date: 2016-02-01T22:52:47+09:00
comments: true
category: ['Tech']
tags: ['Nightmare','JavaScript']
published: true
slug: how-to-get-amazon-affiliate-reports-with-nightmarejs
img: 'https://images-na.ssl-images-amazon.com/images/I/61DHJGf1uSL._SL160_.jpg'
---

この本を読んで、Ruby, Capybaraから取得することはできていたが、そもそもCapybaraは、PhantomJS/PoltergeistというJavaScriptライブラリのラッパーであり、JavaScriptから直接操作するにはどんな方法があり、どんな書き方になるのかを知りたかったので、調べてみました。これを機会に、JavaScriptを書けるようになりたいとも願いつつ。。。

{{% amazon_ B00TO6KMEK %}}

{{% googleadsense %}}


## Nightmareとは？

Nightmare.jsは、ブラウザの挙動を自動化できるJavaScriptライブラリです。以前は、PhantomJSのラッパーだったみたいだが、現在は内部的にElectronを利用するようになった。

[segmentio/nightmare: A high-level browser automation library.](https://github.com/segmentio/nightmare)

```
npm install nightmare
```



## Amazon アフィリエイトの前日のレポートを取得する

まずは、完成品をどうぞ。

```
var Nightmare = require('nightmare');
var vo = require('vo');

vo(function* () {
  var nightmare = Nightmare({ show: false });
  var link = yield nightmare
	  .goto('https://affiliate.amazon.co.jp/')
		.type('input#username', 'USERID')
		.type('input#password', 'PASSWORD')
		.click('#signin > input[type="image"]')
		.wait('#mini-report')
		.evaluate(function () {
			return document.querySelector('#mini-report > div.line-item-total > div.data').textContent;
		});
	yield nightmare.end();
  return link;
})(function (err, result) {
  if (err) return console.log(err);
  console.log(result);
});
```

## サンプルコードを動かす

```
npm install nightmare vo
node --harmony yahoo.js
```

JavaScript初心者な自分にとっては、まず下記のサンプルコードが動かせなかったし、何が原因かわからなかった。よくよくJavaScriptの背景と現状を追ってみると、'function* ', 'yield'などのコードを含むのは、ES2015(ES6)のバージョンの書き方であり、Node.jsのバージョンが古いと動かせないことがわかった。

Node.jsのバージョンをv5.5.0に上げて、再実行したところ、Electronが立ち上がり、yahoo.comに検索しに行くのを確認できる。

```
var Nightmare = require('nightmare');
var vo = require('vo');

vo(function* () {
  var nightmare = Nightmare({ show: true });
  var link = yield nightmare
    .goto('http://yahoo.com')
    .type('input[title="Search"]', 'github nightmare')
    .click('.searchsubmit')
    .wait('.ac-21th')
    .evaluate(function () {
      return document.getElementsByClassName('ac-21th')[0].href;
    });
  yield nightmare.end();
  return link;
})(function (err, result) {
  if (err) return console.log(err);
  console.log(result);
});
```

### Genaratar function* って？

ここ数日の自分の理解だと、「非同期処理を同期的に記述する」ための記述方法であるという理解。`yield`によって処理を途中で止めることができる。
(もう少し理解がまとまったら、追記したい)


## 参考

- [Nightmareがv2(Electronベース)になり、使いやすく感動したのでLIGブログのPV/UUデータ取得を自動化してみた。 - Qiita](http://qiita.com/n0bisuke/items/8a7a52321380e5cf0379)
- [ChatOps + NightmareでメトリクスグラフとBIレポートをSlackに投げるようにした - Glide Note - グライドノート](http://blog.glidenote.com/blog/2015/10/01/nightmare-screenshots/)
- [Nightmare.jsでQiitaのコントリビューション数をスクレイピング - Qiita](http://qiita.com/n0bisuke/items/75b238ec88c96aa0dee8)
- [Web scraping with Nightmare.js | azurelogic.com](https://azurelogic.com/posts/web-scraping-with-nightmare-js/) (PhantomJSの時の例)

## 参考図書

{{% amazon_ 4883379930 %}}
{{% amazon_ B00TO6KMEK %}}
{{% amazon_ 4798131113 %}}