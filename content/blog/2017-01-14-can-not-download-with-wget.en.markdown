---
title: "Cannot download with wget"
date: 2017-01-14T14:14:02+09:00
lastmod: 2017-01-14T14:14:02+09:00
comments: true
category: ['Tech']
tags: ['MeCab','Linux']
published: true
slug: can-not-download-with-wget
img:
---

I faced trouble that Circle CI had build error. I search solution and deal with it.

[MeCab: Yet Another Part\-of\-Speech and Morphological Analyzer](http://taku910.github.io/mecab/)

<!--more-->
{{% googleadsense %}}

## Problem

I faced trouble when changing download link.

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

## Solution

I'm able to download with tagging URL by `""`. But download file name is strange, so I set `-O` option.

```
wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE"
```
