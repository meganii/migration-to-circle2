---
title: "正規化とは何か？"
date: 2015-08-07T08:46:00+09:00
comments: true
category: ['Tech']
tags: ['DB']
published: true
img: "https://images-na.ssl-images-amazon.com/images/I/51vol70XHoL._SL160_.jpg"
slug: normalization
---

達人に学ぶDB設計を読んだときのメモ。

{{% googleadsense %}}


## 第１正規形　スカラ値(Scalar value)

「１つのセルの中には１つの値しか含まない」

関数従属性(functional dependency)

`Y = f(X)` : 入力Xに対して出力Yを決めるための式

このとき、**YはXに従属する**という。

この関係をデータベースで表すと、`{X} -> {Y} `となる。


Xの値を決めれば、Yの値が１つに決まる。
(XおよびYは１つの列ではなく、複数の列の組み合わせであっても構わない)

**i.e. 正規化とは、テーブルのすべての列が関数従属性を満たすように整理していくこと。**


## 第２正規形

**会社コード**, 会社名, **社員ID**, 社員名, 年数, 部署コード, 部署名

{会社コード} -> {会社名}

主キーの一部である「会社コード」に従属している。
主キーの一部の列に対して従属する列がある場合、この関係を**部分関数従属**と呼ぶ。

## 正規化のポイント

- 正規化とは、更新時の不都合・不整合を排除するために行う
- 正規化は、従属性を見抜くことで可能となる

テーブルの形式だけ見ててもわからない。どの列がどのキーに従属しているかは、業務ロジック(ビジネスロジック)で決まる。

部分関数従属
推移的関数従属


## 参考
<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/4798124702/meganii-22/" target="_blank" ><img src="https://images-na.ssl-images-amazon.com/images/I/51vol70XHoL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4798124702/meganii-22/" target="_blank" >達人に学ぶDB設計 徹底指南書 初級者で終わりたくないあなたへ</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">ミック 翔泳社 2012-03-16    </div><div class="booklink-link2"><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/asin/4798124702/meganii-22/" target="_blank" >Amazon</a></div><div class="shoplinkkindle"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B00EE1XPAI/meganii-22/" target="_blank" >Kindle</a></div><div class="shoplinkrakuten"><a href="http://hb.afl.rakuten.co.jp/hgc/13e181b2.b5761023.13e181b3.cbc7b217/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F11582464%2F%3Fscid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2Fev%2Fbook%2F" target="_blank" >楽天ブックス</a></div>                  	  	  	  <div class="shoplinktoshokan"><a href="http://calil.jp/book/4798124702" target="_blank" >図書館</a></div></div></div><div class="booklink-footer"></div></div>
