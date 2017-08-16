---
title: "wgetでダウンロード失敗したときの対処法"
date: 2017-01-14T14:14:02+09:00
lastmod: 2017-01-14T14:14:02+09:00
comments: true
category: ['Tech']
tags: ['MeCab','Linux']
published: true
slug: can-not-download-with-wget
---

Circle CIからMeCab本体と、MeCab用の辞書をダウンロードしていましたが、ファイルダウンロード先のURLが変わったみたいである時期からビルドが失敗するようになったので調べて対処しました。

[MeCab: Yet Another Part\-of\-Speech and Morphological Analyzer](http://taku910.github.io/mecab/)

<!--more-->
{{% googleadsense %}}

## 問題

以下の通り、リンク先を変えたところエラーが発生しました。

```diff
-  wget https://mecab.googlecode.com/files/mecab-0.996.tar.gz
+  wget https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
```

```bash
$ wget https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
$ --2017-01-14 14:26:57--  https://drive.google.com/uc?export=download
drive.google.com をDNSに問いあわせています... 2404:6800:4004:80e::200e, 216.58.197.206
drive.google.com|2404:6800:4004:80e::200e|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 400 Bad Request
2017-01-14 14:26:58 エラー 400: Bad Request。
```

## 結論

`""`でURLを囲ってあげることでダウンロードできました。それだけだと変なファイル名になってしまうので、`-O`オプションでファイル名を指定しました。

```
wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE"
```

## 参考

- [Mecabのインストール方法 \- Qiita](http://qiita.com/katsuyuki/items/65f79d44f5e9a0397d31)
