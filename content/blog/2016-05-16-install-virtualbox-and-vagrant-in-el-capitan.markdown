---
title: "MacでVirtualbox、Vagrantをインストールするときにいつまで経っても検証が終わらない場合の対処法としてコマンドラインからインストールする"
date: 2016-05-16T20:50:35+09:00
lastmode: 2017-02-22T07:23:35+09:00
comments: true
category: ['Tech']
tags: ['El Capitan','Mac']
published: true
slug: install-virtualbox-and-vagrant-in-el-capitan
img: "https://farm8.staticflickr.com/7385/26774309130_925fdae08f_t.jpg"
---

久々に、vagrantを触ろうと思い、どうせならバージョンアップしてから使おうと思い、Virtualboxから入れ直そうとしたらちょっとハマった時の話です。

<!--more-->
{{% googleadsense %}}


## 環境

- El Capitan Version 10.11.4

※ VirtualboxとVagrantのバージョンはメモしていませんでした

## 事象

dmgファイルをダウンロードして、Vagrant.pkgやVirtualbox.pkgをダブルクリックしたところ、以下のようにチェックが終わらない現象になった。

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/35571855@N06/26774309130/in/dateposted-public/" title="never ending verifying..."><img src="https://farm8.staticflickr.com/7385/26774309130_925fdae08f.jpg" width="500" height="178" alt="never ending verifying..."></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


## 原因

[virtualbox.org • View topic - [INSTALL] Verifying "VirtualBox.pkg"... never clears -- El Cap 10.11.4](https://forums.virtualbox.org/viewtopic.php?f=8&t=77122)を見ると、System Integrity Protection(SIP)絡みでインストールが弾かれるみたい。

System Integrity Protection(SIP)については、以下のページが参考になった。
[OS X 10.11 El CapitanのSystem Integrity Protection(SIP)についてちょっと詳しく](http://rcmdnk.github.io/blog/2015/10/10/computer-mac/)


## 対処方法

対処方法として、「1.SIPを無効化する」か、「2.`sudo installer`でインストールする」方法がありそう。

ここでは、「2.`sudo installer`でインストールする」の方法で、[VirtualBoxのインストール(MacOS X El Capitan) - Qiita](http://qiita.com/tniizawa/items/33eb015296ea171ed25f)を参考にして、CUIでインストールしました。

## 手順

### 1.マウント

```
hdiutil mount VirtualBox-5.0.18-106667-OSX.dmg
```

### 2.パッケージインストール

```
sudo installer -pkg /Volumes/Vagrant/Vagrant.pkg -target /Volumes/Macintosh\ HD
```

### 3.アンマウント

```
hdiutil mount VirtualBox-5.0.18-106667-OSX.dmg
```

## 結論

上記の手順でインストールすれば、すんなりとインストールすることができました。El Capitanにしてから、ちょくちょくこのSIPに悩まされるのでもうちょっと理解するようにしたい。

{{% amazon_ B00F418SQ8 %}}
{{% amazon_ 4873116651 %}}
