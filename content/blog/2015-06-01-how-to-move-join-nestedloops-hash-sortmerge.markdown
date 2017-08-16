---

title: "[SQL実践入門]結合のアルゴリズム Nested Loops, Hash, Sort Merge"
date: 2015-06-01T00:48:00+09:00
comments: true
category: ['Tech']
tags: ['DB']
published: true
img: "https://images-na.ssl-images-amazon.com/images/I/51pl3HrLCjL._SL160_.jpg"
slug: how-to-move-join-nestedloops-hash-sortmerge
---

データベースの結合のイメージがいまいち掴めていなかったため、「SQL実践入門」を読んで、結合のアルゴリズムをまとめておく。

{{% amazon_ 4774173010 %}}

## 結合の種類

結合の種類としては、以下の3種類が存在する。

- Nested Loops
- Hash
- SortMerge



{{% googleadsense %}}

## Nested Loops

入れ子のループを使うアルゴリズム。

<p><a href="https://www.flickr.com/photos/35571855@N06/18118597038" title="NestedLoopsby meganii, on Flickr"><img class="img-responsive" src="https://farm1.staticflickr.com/294/18118597038_a9a1db08b8_z.jpg" alt="NestedLoops"></a></p>

外側のループの対象となるテーブル(Table_A)を駆動表(driving table)もしくは、外部表(outer table)と呼ぶ。

### 結合の流れ
1. 駆動表の1行に対して、内部表を1行ずつスキャンして、結合条件にマッチするものを返却する。
2. 駆動表の全ての行に対して繰り返す。



Table_A、Table_Bの結合対象の行数をそれぞれR(A)、R(B)とすると、アクセスする行数は`R(A)×R(B)`となる。


### どちらのテーブルを駆動表にするか？

一見、どちらのテーブルを駆動表にしてもアクセス行数は、`R(A)×R(B)`と`R(B)×R(A)`で変わらないように思われるが、駆動表の選択はNested Loopsの性能において重要な意味を持つ。

⇛「駆動表が小さいほど、Nested Loopsの性能は良い」

ここで重要な点は、内部表の列にインデックスが存在すること。

内部表の結合キーの列にインデックスが存在する場合、そのインデックスをたどることによって、DBMSは駆動表の1行に対して内部表を馬鹿正直にループする必要がなくなる。

<p><a href="https://www.flickr.com/photos/35571855@N06/18303911782" title="NestedLoopsIndexby meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8842/18303911782_97376982a1_z.jpg" alt="NestedLoopsIndex"></a></p>

理想的なケースとして、駆動表のレコード1行に対して内部表のレコードが1行に対応していれば、内部表のインデックスをたどることでループすることなく1行を特定できる。その結果、アクセス行数は、`R(A)×2`となる。


### 内部表のループをどれだけスキップできるかがポイント
<p><a href="https://www.flickr.com/photos/35571855@N06/18121300118" title="InnerLoopby meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8894/18121300118_82c4ba9c0b_z.jpg" alt="InnerLoop"></a></p>

- 内部表が結合キーで一意だと内部ループを完全にスキップ可能
- 内部表が結合キーで一意にならないと内部ループが残る


### SQLチューニングの基本

1. 駆動表の小さなNested Loops
2. 内部表の結合キーにインデックス




## Hash

<p><a href="https://www.flickr.com/photos/35571855@N06/18425291321" title="Hashby meganii, on Flickr"><img class="img-responsive" src="https://farm1.staticflickr.com/393/18425291321_b260f13b13_z.jpg" alt="Hash"></a></p>

- 結合テーブルからハッシュテーブルを作成するため、Nested Loopsと比べるとメモリを多く消費する
- メモリ内にハッシュテーブルが収まらないとストレージを使用して、遅延が発生する　⇛　 **「Temp落ち」**
- 出力となるハッシュ値は、入力値の順序性を保存しないため、等値結合でしか使用できない





### Hash Joinが有効なケース

- Nested Loopsで適切な駆動表(相対的に十分に小さいテーブル)が存在しない場合
- 駆動表として小さいテーブルは指定できるが、内部表のヒット件数が多い場合
- Nested Loopsの内部表にインデックスが存在しない場合



## SortMerge

<p><a href="https://www.flickr.com/photos/35571855@N06/18397300676" title="Sort Mergeby meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8887/18397300676_ac502d01a6_z.jpg" alt="Sort Merge"></a></p>

- 対象テーブルをどちらもソートする必要があるため、Nested Loopsよりも多くのメモリを消費する
- Hashと違い、等値結合だけでなく、不等式(<.>, <=, >=)を使った結合にも利用できる


## 参考図書

{{% amazon_ 4774173010 %}}







