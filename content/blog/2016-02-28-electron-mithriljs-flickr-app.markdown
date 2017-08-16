---
title: "Electron + Mithril.jsでFlickrアプリを作成する"
date: 2016-02-28T22:13:24+09:00
comments: true
category: ['Tech']
tags: ['electron','Mithril.js']
published: true
slug: electron-mithriljs-flickr-app
img: "http://www.oreilly.co.jp/books/images/picture978-4-87311-744-7.gif"
---

{{% googleadsense %}}

<p><a href="https://www.flickr.com/photos/35571855@N06/24974002959" title="Electron_Flickrby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1537/24974002959_ef392cebb9_z.jpg" alt="Electron_Flickr"></a></p>


以前、Angular.jsで作成したFlickrアプリを、Electron + Mithril.jsで焼き直した。

Angular.jsは重厚長大な感があり、個人で使う分にはちょっと過剰すぎる気がする。どうせなら、VirtualDOMの概念も合わせて学びたかったので、まずReact.jsのチュートリアルをしたのだが、JavaScript初心者が使う分には、ES6, Babel, JSXなどなど、新しく学ぶ概念が多すぎる気がして挫折した。

他に何かシンプルなフレームワークはないか、探していたところ、ElectronとMithril.jsの組み合わせの記事をQiitaで見かけたので試してみた。

- [Electron と Mithril でソースリーディングを助けるアプリをつくってみた - Qiita](http://qiita.com/hakomo/items/d472605578e0a3f602b4)
- [Electron + Mithrilで、ふつうのデスクトップアプリを作る - Qiita](http://qiita.com/shibukawa/items/e1836a8c98413448f746)





結論から言うと、自分にとってはこのぐらいがまずちょうどいいので使ってみようと思った。Railsを覚えるのは辛いけど、まずはSinatraを使うぐらいのノリ。それでいて、素のJavaScirpt操作や、jQueryを使ってのDOM操作をしなくても良いのは気持ちが良い。

## Mithril.js

[Mithril　http://mithril-ja.js.org/ ](http://mithril-ja.js.org/)

- シンプルなAPI
- 軽い
- VirtualDOM
- コンポーネント指向

## コード index.html

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Electron Flickr</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
  </head>
  <body>
    <div id="root" class="container">
      <h1>Flickr</h1>
      <div id="link"></div>
      <div id="result"></div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/mithril/0.2.2-rc.1/mithril.min.js"></script>
    <script>

      const API_KEY = "YOUR_FLICKR_KEY";
      const USER_ID = "YOUR_USER_ID";

      var photos = m.prop([]); //default value
      var textContext = m.prop();

      var linkComponent = {
        controller: function() {
          textContext("");
        },
        view: function(ctrl) {
          return m("textarea", {name: "linktextarea", class: "form-control", rows: 5}, textContext());
        }
      }

      var resultComponent = {
        controller: function() {
          this.createLink = function(index) {
            var item = photos().photos.photo[index];

            var link = '<p><a href="https://www.flickr.com/photos/' + item.owner + '/' + item.id + '" title="' + item.title + 'by meganii, on Flickr"><img class="img-responsive" src="https://farm' + item.farm + '.staticflickr.com/' + item.server +'/' + item.id + '_' + item.secret + '_z.jpg" alt="' + item.title + '"></a></p>\n';

            textContext(textContext() + link);
          };

          m.request({
            dataType: "jsonp",
            callbackKey: "jsoncallback",
            url: "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=" + API_KEY + "&user_id=" + USER_ID+ "&sort=date-posted-desc&format=json"
          }).then(photos);
        },

        view: function(ctrl) {
          return m("ul",[
              photos().photos.photo.map(function(item, index) {
                 return m("li", [
                   m("input[type=checkbox]", {onclick: m.withAttr("value", ctrl.createLink), value: index } ),
                   m("img", {src: "https://farm" + item.farm + ".staticflickr.com/" + item.server + "/" + item.id + "_" + item.secret + "_z.jpg"})
                 ])
              })
          ])
        }
      }

      m.mount(result, resultComponent);
      m.mount(link, linkComponent);

    </script>
  </body>
</html>
```

## Flickr API

Flickrへリクエストを投げる時に少し躓いたのでメモ。

Flickrは、jsonp形式のため、単純に、以下のようにリクエストを送るのでは上手くいかない。

```
m.request({method: "GET", url: "/path/to/resource"})
```

以下のように、`dataType: "jsonp"`, 'callbackKey'を指定する。

```
m.request({
    dataType: "jsonp",
    callbackKey: "jsoncallback",
    url: "http://api.flickr.com/services/feeds/photos_public.gne?tags=monkey&tagmode=any&format=json"
});
```


ようやく、よく分からないAngular.jsから、比較的見通しが立ってきたElectron + Mithril.jsに切り替えることができた。


## 目標「自分専用Markdownエディターを作る」

最終的には、自分専用Markdownデスクトップアプリを、Electronで作成することが目標だ。Kobitoは便利で使ってるのだけど、そのままEvernoteに連携して欲しかったり、リンク作成の機能がまとまってると嬉しい。


実装したい機能は、こんな感じ。Kobitoをベースに自分専用の機能を盛り込みたい。

- Markdownエディター(オートプレビュー)
- Flickr連携(アップロード、リンク作成)
- Evernote連携(自動保存)
- Amazonリンク作成
- ASP一括検索
- git push

<div class="booklink-box"><div class="booklink-image"><a href=http://www.amazon.co.jp/Effective-JavaScript-David-Herman/dp/4798131113%3FSubscriptionId%3DAKIAI6MZOKQQCKBKJBLQ%26tag%3Dmeganii-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4798131113><img src="https://images-na.ssl-images-amazon.com/images/I/51nSK4pE-RL._SL160_.jpg" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4798131113/meganii-22/">Effective JavaScript</a></div><div class=shoplinkrakuten><a href="http://hb.afl.rakuten.co.jp/hgc/g00q0725.il1o2897.g00q0725.il1o3b57/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F12215141%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Frms%2Fmsv%2FItem%3Fn%3D12215141%26surl%3Dbook">楽天で買う</a></div></div></div>
