---
title: "音声認識エンジンJuliusをインストールする"
date: 2016-12-21T21:52:28+09:00
lastmod: 2016-12-21T21:52:28+09:00
comments: true
category: ['Tech']
tags: ['julius']
published: true
slug: install-julius
img: https://images-fe.ssl-images-amazon.com/images/I/510B8-IOdUL._SL160_.jpg
---

音声で認識できる

## 音声認識エンジン

- Apple - Siri
- Google -
- Microsoft - Bing API
- Julius


<!--more-->
{{% googleadsense %}}


## Juliusとは


## Juliusのインストール

Juliusで音声から文字起こしする(ディクテーション)をする場合は、最小限のモデル（不特定話者音響モデル + 汎用言語モデル）も必要になってきます。以下の手順でJulius本体と、モデルをインストールします。


1. 下記URLから最新版のJulius(4.4.2)をダウンロード

[Releases · julius\-speech/julius](https://github.com/julius-speech/julius/releases)
https://github.com/julius-speech/julius/archive/v4.4.2.tar.gz

2. ダウンロードしたファイルを解凍し、`make install`

```
$ cd julius-4.4.2
$ ./configure
$ make
$ make install
```

3. インストールを確認

問題なくインストールされていたら、以下のコマンドを実行すればJuliusのバージョンが表示される。

```
$ julius -version
JuliusLib rev.4.4.2 (fast)

Engine specification:
 -  Base setup   : fast
 -  Supported LM : DFA, N-gram, Word
 -  Extension    :
 -  Compiled by  : gcc -g -O2

Library configuration: version 4.4.2
 - Audio input
    primary A/D-in driver   : coreaudio (MacOSX CoreAudio)
    available drivers       :
    wavefile formats        : RAW and WAV only
    max. length of an input : 320000 samples, 150 words
 - Language Model
    class N-gram support    : yes
    MBR weight support      : yes
    word id unit            : short (2 bytes)
 - Acoustic Model
    multi-path treatment    : autodetect
 - External library
    file decompression by   : zlib library
 - Process hangling
    fork on adinnet input   : no
 - built-in SIMD instruction set for DNN
    SSE AVX FMA
    FMA is available maximum on this cpu, use it

Try `-help' for more information.
```

4. `Git Large File Storage`のインストール

次の手順でダウンロードするリポジトリが2GBぐらいあるため、git-lfs(Git Large File Storage)をインストールしないと途中でgit cloneが失敗する(と記載があった)ので、まずは以下のコマンドを実行して`Git Large File Storage`をインストールする。

```
$ brew install git-lfs
```


5. ディクテーションキットのダウンロード

[julius\-speech/dictation\-kit: Japanese dictation kit using Julius](https://github.com/julius-speech/dictation-kit)



## 参考

[Juliusによる音声認識 \| Raspberry Pi 研究室 \| Feijoa\.jp](http://feijoa.jp/laboratory/raspberrypi/julius/)



<div class="booklink-box"><div class="booklink-image"><a href=https://www.amazon.co.jp/%E3%83%95%E3%83%AA%E3%83%BC%E3%82%BD%E3%83%95%E3%83%88%E3%81%A7%E3%81%A4%E3%81%8F%E3%82%8B%E9%9F%B3%E5%A3%B0%E8%AA%8D%E8%AD%98%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%EF%BC%8D%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E8%AA%8D%E8%AD%98%E3%83%BB%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AE%E5%88%9D%E6%AD%A9%E3%81%8B%E3%82%89%E5%AF%BE%E8%A9%B1%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%BE%E3%81%A7%EF%BC%8D-%E8%8D%92%E6%9C%A8-%E9%9B%85%E5%BC%98/dp/4627847114%3FSubscriptionId%3DAKIAI6MZOKQQCKBKJBLQ%26tag%3Dmeganii-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4627847114><img src="https://images-fe.ssl-images-amazon.com/images/I/510B8-IOdUL._SL160_.jpg" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4627847114/meganii-22/">フリーソフトでつくる音声認識システム－パターン認識・機械学習の初歩から対話システムまで－</a></div><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/asin/4627847114/meganii-22//">Amazonで買う</a></div><div class="shoplinkrakuten"><a href="http://hb.afl.rakuten.co.jp/hgc/10b944e1.69649a36.10b944e2.c5d6d56c/?pc=http://search.rakuten.co.jp/search/mall?sitem=Julius&m=http://m.rakuten.co.jp/">楽天で買う</a></div><div class="shoplinkyahoo"><a href="http://ck.jp.ap.valuecommerce.com/servlet/referral?sid=3067752&pid=884189678&vc_url=http://search.shopping.yahoo.co.jp/search?p=Julius">Yahoo!で買う</a></div></div></div>
