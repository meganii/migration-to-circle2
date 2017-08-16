---
title: "building machine learning systems with python"
date: 2016-09-18T10:58:35+09:00
comments: true
category: ['Tech']
tags: ['機械学習']
published: true
slug: building-machine-learning-systems-with-python
---

<!--more-->
{{% googleadsense %}}


## 第３章　クラスタリング：　関連のある文書を見つける


ラベル付きデータが入手できない場合。例えば、ラベル付きデータを集めるのにとてもコストがかかる場合など。

 「類似した文書を含むクラスタをいかに素早く見つけ出すことができるか」という問題を考えるためには、文書同士
 の類似度を計算しなければならない。


## クラスタリング

特徴ベクトルを用いてグループ分けを行う方法には、大きく分けると以下２つ存在する。

- フラットクラスタリング(flat clustering)
- 階層的クラスタリング(hierachical clustering)


[2\.3\. Clustering — scikit\-learn 0\.17\.1 documentation](http://scikit-learn.org/stable/modules/clustering.html)



### フラットクラスタリング

クラスタ間の関係性は考慮せずに、データをクラスタに分類する。全てのデータがどこか１つのクラスタに属するように分割すること。前もってクラスタの数を決める必要がある。


### 階層的クラスタリング

クラスタの数を指定する必要はない。
クラスタを階層的構造に組み立てる
類似性の高いデータをクラスタとしてグループ化し、さらにそのクラスタと類似するクラスタをまとめて親クラスタとする。

これを再帰的に繰り返し、クラスタが１つになるまで繰り返す。


## KMeans

フラットクラスタリング



[K\-meansクラスタリングで何かつくる](http://www.slideshare.net/oscillograph/6-51143088)


m.o. num_clustersに、カテゴリとして指定した数を用いる
