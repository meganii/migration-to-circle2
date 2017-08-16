---
title: "Capybaraで非表示要素を検索できない"
date: 2017-06-24T11:39:13+09:00
lastmod: 2017-06-24T11:39:13+09:00
comments: true
category: ['Tech']
tags: ['capybara']
published: true
slug: capybara-cannot-find-invisible-element
img: https://images-fe.ssl-images-amazon.com/images/I/51HQYnwtflL._SL160_.jpg
---

Capybaraで、`style="display: none;"`となっているある要素を取得しようと思ったら、思わぬところでハマった。
`page.screenshot`でスクリーンショットを取っても、`print page.html`でDOMを取得しても、そこにある要素がfindやhas_selector?メソッドから取得できなくて困った。

結論は、`style="display: none;"`のような非表示の要素は、デフォルトでは検索条件にならない。

どうやら下記の`visible`オプションがあるようです。知らなくて、しばらく途方にくれていました。

http://www.rubydoc.info/github/jnicklas/capybara/master/Capybara/Node/Finders#all-instance_method
```
visible (Boolean, Symbol) — Only find elements with the specified visibility:
true - only finds visible elements.
false - finds invisible and visible elements.
:all - same as false; finds visible and invisible elements.
:hidden - only finds invisible elements.
:visible - same as true; only finds visible elements.
```

<!--more-->
{{% googleadsense %}}


## 参考
- [Capybara で非表示要素を find する \- kakakakakku blog](http://kakakakakku.hatenablog.com/entry/2015/05/14/124653)
- [非表示要素はCapybaraのfindで検索対象になるのか \- Qiita](http://qiita.com/upinetree/items/4d4022c90ce32b68c38d)

<a href="https://www.amazon.co.jp/Ruby-Rails-5%E3%82%A2%E3%83%97%E3%83%AA%E3%82%B1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-%E5%B1%B1%E7%94%B0-%E7%A5%A5%E5%AF%9B-ebook/dp/B071YC72X1/ref=as_li_ss_il?_encoding=UTF8&psc=1&refRID=A6GMKK241XNSTEJMR6JY&linkCode=li2&tag=meganii-22&linkId=dd737cff408c7d8eac02572e6079b4d2" target="_blank"><img border="0" src="//ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B071YC72X1&Format=_SL160_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=meganii-22" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=meganii-22&l=li2&o=9&a=B071YC72X1" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
