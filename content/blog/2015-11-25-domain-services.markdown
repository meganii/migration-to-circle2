---
title: "ドメインサービスとは？"
date: 2015-11-25T20:34:53+09:00
comments: true
category: ['tech']
tags: ['domain','DDD']
published: true
slug: domain-services
img: "https://images-na.ssl-images-amazon.com/images/I/619Gh1s721L._SL160_.jpg"
---



## ドメインサービスとは？

Windows Communication Foundation(WCF), Silverlight周りで出てくるドメインサービスとは一体なにものだろうか。ドメイン駆動設計(DDD)の文脈から読み解いてみる。


「サービス」と聞くと、粒度の粗いコンポーネント(リモートクライアントから複雑な業務システムを利用できるようにするもの)を想像するかもしれないが、ドメインサービスは違う。
また、アプリケーションサービスも頭に思い浮かぶかもしれないが、それも違う。

アプリケーションサービスには、ビジネスロジックを組み込みたくないが、ドメインサービスにはビジネスロジックを組み込んでおきたい。


>時には単純に「物」や「値」にはできないこともある。

- ドメインにおける重要なプロセスや変換処理が、エンティティや値オブジェクトの自然な責務でない場合、その操作は、サービスとして宣言される独立したインターフェースとしてモデルに追加すること
- モデルの言語を用いてインターフェースを定義し、操作名が必ずユビキタス言語の1部になるようにすること
- サービスには状態を持たせないこと


{{% googleadsense %}}



## ある操作が既存のエンティティや値オブジェクトに属するものでないとみなせる条件は？

- 重要なビジネスロジックを実行する
- ドメインオブジェクトを、ひとつの構成から別の構成に変換する
- 複数のドメインオブジェクトからの入力にもとづいて値を算出する

e.g. 何かの操作で複数の集約(合成)が必要になる。  
     何かのメソッドをエンティティや値に持たせるのが単に不格好


やりすぎ注意！ やり過ぎると、*ドメインモデル貧血症* になる。


<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00UX9VJGW/meganii-22/" target="_blank" ><img src="https://images-na.ssl-images-amazon.com/images/I/619Gh1s721L._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00UX9VJGW/meganii-22/" target="_blank" >実践ドメイン駆動設計[Kindle版]</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">ヴァーン・ヴァーノン 翔泳社 2015-03-19    </div><div class="booklink-link2"><div class="shoplinkkindle"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B00UX9VJGW/meganii-22/" target="_blank" >Kindle</a></div><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/479813161X/meganii-22/" target="_blank" >Amazon[書籍版]</a></div>                              	  	  	      </div></div><div class="booklink-footer"></div></div>
