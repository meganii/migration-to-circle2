---
title: "文書推薦"
date: 2016-08-12T18:35:30+09:00
comments: true
category: ['Tech']
tags: ['機械学習','Python']
published: true
slug: recommend-engine
img: https://images-fe.ssl-images-amazon.com/images/I/51%2BfZJOKEKL._SL160_.jpg
---


Hugoで関連記事を表示させるためは、ある記事がどの記事と似ているかを機械的に処理する必要があります。では、この判断をどのようにすればいいのでしょうか？

## この記事に書いてあること

- 関連記事を出すために考えること
- 文書推薦のための手法(コンテンツベース、協調フィルタリング)
- 実装方法
- word2doc

<!--more-->
{{% googleadsense %}}


## word2doc

名前は聞いたことがあったが、なんのためにどうやって使うのか全然わからなかった。



## 文書推薦とは？

1. コンテンツベース
2. 協調フィルタリング

コンテンツベースとは、文章の内容を元に判断するアルゴリズムであり、

協調フィルタリングとは、Amazonのレコメンドエンジンのように誰々がオススメするものみたいなイメージを持ちました。



## TF-IDFによる文書推薦

以下の「プログラマのための文書推薦入門」は、分かりやすかったので一読をお勧めします。

[プログラマのための文書推薦入門](http://www.slideshare.net/y-uti/document-recommendation)


{{% slideshare 6jqDpBzvDXsQ5m %}}


あとは、以下のブログで、コードを見ながら雰囲気を掴みました。

[Pythonでcos類似度とTF\-IDFを用いた文章の類似度算出 \- 元理系院生の新入社員がPythonとJavaで色々頑張るブログ](http://emoson.hateblo.jp/entry/2015/02/21/234311)

