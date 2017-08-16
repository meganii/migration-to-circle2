---

title: "[SQL実践入門]内部結合と外部結合のイメージ"
date: 2015-06-10T07:58:00+09:00
comments: true
category: ['Tech']
tags: ['DB']
published: true
img: "https://images-na.ssl-images-amazon.com/images/I/51pl3HrLCjL._SL160_.jpg"
slug: inner-join-outer-join
---


内部結合と外部結合の「内部」と「外部」はどこから来ているのかクロス結合を元に説明している箇所を抜き出してまとめる。



<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774173010/meganii-22/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/51pl3HrLCjL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774173010/meganii-22/" rel="nofollow" target="_blank">SQL実践入門──高速でわかりやすいクエリの書き方 (WEB+DB PRESS plus)</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">ミック 技術評論社 2015-04-11    </div><div class="booklink-link2"><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774173010/meganii-22/" rel="nofollow" target="_blank">Amazon</a></div><div class="shoplinkkindle"><a href="http://www.amazon.co.jp/gp/search?keywords=SQL%8E%C0%91H%93%FC%96%E5%84%9F%84%9F%8D%82%91%AC%82%C5%82%ED%82%A9%82%E8%82%E2%82%B7%82%A2%83N%83G%83%8A%82%CC%8F%91%82%AB%95%FB%20%28WEB%2BDB%20PRESS%20plus%29&__mk_ja_JP=%83J%83%5E%83J%83i&url=node%3D2275256051&tag=meganii-22" rel="nofollow" target="_blank">Kindle</a></div><div class="shoplinkrakuten"><a href="http://hb.afl.rakuten.co.jp/hgc/13e181b2.b5761023.13e181b3.cbc7b217/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F13190627%2F%3Fscid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2Fev%2Fbook%2F" rel="nofollow" target="_blank">楽天ブックス</a></div>                  	  	  	      </div></div><div class="booklink-footer"></div></div>




{{% googleadsense %}}

<p><a href="https://www.flickr.com/photos/35571855@N06/18055701993" title="Venn diagramby meganii, on Flickr"><img class="img-responsive" src="https://farm1.staticflickr.com/535/18055701993_40ac4eafb9_z.jpg" alt="Venn diagram"></a></p>




## クロス結合(Cross Join) すべての結合の母体

数学的には、直積、デカルト積と呼ばれる演算である。
結合対象となる2つの手0ブルのレコードから可能なすべての組み合わせ網羅を行う演算。

## 内部結合(Inner Join)

### 何の内部？
内部とは「直積の部分集合」

相関サブクエリとして書き換え可能だが、基本的に結合で記述できる限りは結合を選択するのがよい。

### Why？

内部結合を相関サブクエリとして書き換えた場合、結果行数だけ相関サブクエリを実行するためコストが高くなる。



## 外部結合(Outer Join)

### 何の外部か？

外部とは、直積の部分集合にならないという意味である。

外部結合の結果には、マスタ側のテーブルだけに存在するキーがあった場合、そのキーを削除せずに、結果に保存するように動作する。

キーの値をすべて網羅するレイアウトのレポートを作成する場合に多用される。



## 感想

数年前は、外部結合の意味が全然分からず、Oracleでいうと(+)をつけておけばとりあえずいいんでしょうという理解しかなかったので、今思うと恐ろしい。


## 参考
<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774173010/meganii-22/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/51pl3HrLCjL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774173010/meganii-22/" rel="nofollow" target="_blank">SQL実践入門──高速でわかりやすいクエリの書き方 (WEB+DB PRESS plus)</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">ミック 技術評論社 2015-04-11    </div><div class="booklink-link2"><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/asin/4774173010/meganii-22/" rel="nofollow" target="_blank">Amazon</a></div><div class="shoplinkkindle"><a href="http://www.amazon.co.jp/gp/search?keywords=SQL%8E%C0%91H%93%FC%96%E5%84%9F%84%9F%8D%82%91%AC%82%C5%82%ED%82%A9%82%E8%82%E2%82%B7%82%A2%83N%83G%83%8A%82%CC%8F%91%82%AB%95%FB%20%28WEB%2BDB%20PRESS%20plus%29&__mk_ja_JP=%83J%83%5E%83J%83i&url=node%3D2275256051&tag=meganii-22" rel="nofollow" target="_blank">Kindle</a></div><div class="shoplinkrakuten"><a href="http://hb.afl.rakuten.co.jp/hgc/13e181b2.b5761023.13e181b3.cbc7b217/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F13190627%2F%3Fscid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2Fev%2Fbook%2F" rel="nofollow" target="_blank">楽天ブックス</a></div>                  	  	  	      </div></div><div class="booklink-footer"></div></div>



