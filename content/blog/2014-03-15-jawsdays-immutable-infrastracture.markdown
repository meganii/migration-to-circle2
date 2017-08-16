---

title: Immutable Infrastructure - JAWS DAYS 2014
date: 2014-03-15T12:44:00+09:00
category: ['Tech']
tags: ['aws']
published: true
slug: jawsdays-immutable-infrastracture
---

JAWS DAYS 2014参加レポート第1弾です。

## Immutable Infrastructure @naoya_ito
<a href="http://d.hatena.ne.jp/naoya/20140315/1394851727" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://d.hatena.ne.jp/naoya/20140315/1394851727" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://d.hatena.ne.jp/naoya/20140315/1394851727" target="_blank">JAWS DAYS 2014、Immutable Infrastructure について - naoyaのはてなダイアリー</a><a href="http://b.hatena.ne.jp/entry/http://d.hatena.ne.jp/naoya/20140315/1394851727" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://d.hatena.ne.jp/naoya/20140315/1394851727" alt="" /></a><br style="clear:both;" /><br>



{{% googleadsense %}}
<script async class="speakerdeck-embed" data-id="eb0795108e17013146041a945ae20cc0" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>


## そもそもImmutable Infrastructureって？
Disposable Componetnsって呼ばれたりしていて、不変な、状態を持たない、廃棄可能なっていう意味を持つ。

サーバの状態って、日々のチューニングなどで常に変化している。ケースとしてはまれかもしれないが、半年後にそんな状態のサーバにRailsアプリをもう一度デプロイするときはひどく怖いはす。

どんな変化を行なったかを管理する必要がある。


## でもどうやってサーバの管理をする？
今まで手順書で管理をしていた。しかし、手作業になるためどうしてもオペレーションミスが出てしまう。

**「状態管理が面倒なら、状態を管理しなければいいじゃない」**



## Blue, Green Deployment
ELB, EIPを切り替えることで切り替えるのも行われている。それをもっと大規模にやる例だと思えばよい。


### Herokuでは同じことをやっている
git push する度に新しい環境(コンテナ)を作り、古い環境を捨てる。

上書きすると、環境が上書きされ変な状態になる場合がある。
無停止で切り替えることができる

### Travis CI
Jenkins as a Serviceみたいなもの。

テストをするときに、既存の環境があることでテストが通るというケースはよくある。まっさらな状態にテストを乗せて動かすことで、防ぐことができる。

### Amazonでは1時間で1,000回デプロイ
ビジネスのサイクルを早く回す。プロトタイプを早く回すという実利的なメリットがある。


## Infrastructure as Code
最近になってChefなどの Configuration Management Toolが出来てきたのは、Aamazon Web Serviceが盛り上がってきているから。


## 冪等性
ある操作を何回やっても結果が同じになること。Chefを何度も実行した際に、毎回状況が変わるのであれば使い元にならない。とはいえ、やっぱり環境の状態管理は難しい。

### そこで、環境の状態管理はしない！
- 必要になったときに新しく作る
- 1回作ったものには変更を加えない

- Stateless な状況を作る。


新しい環境をオンデマンドで即座に生成できる技術
⇛　VMよりもコンテナが重要になってきた！

VMは、ハイパーバイザ、OS、などと起動していくためどうしても時間がかかる。
一方、Linuxのコンテナは、Apacheと同じようなプロセスであるため、即座に起動できる。

プログラマブルにしたもの　⇛　Docker

#### Docker
Linuxコンテナを手軽かつプログラマブルに扱えるようにする


#### Jenkins + Docker
コンテナの環境に依存してしまう　⇛　抽象レイヤー Docker
アプリケーションがポータブルになる


Ruby
 - Foreman
 - Rack
 - Bunder 

npm, package.json

Buildpacks 



アプリケーションがポータブルになると・・・

アプリケーション
git pushすればOK ⇛　

- ステートレスなWebとURIのもｔらす制約ににている

状態を伝えるのは難しい。状態がなければ、指し示すことが可能になる



**上書きデプロイから、コンテナベースのデプロイへ**


## 課題
- コンテナ/ Dockerだけでは足りない
- ステートフルなサーバをどうするか？
　ストレージ、キャッシュなど
  Webアプリなどでもステートレスなものがある　⇛　ログなど
　ステートフルなものを外に逃す実装・・・fluentd

既存インフラの一部を動的にしたいというニーズはある。ユーザは、コンテナベースのデプロイのメリットを体感してきている。




