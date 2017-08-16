---
title: "Azureのリモートデスクトップ周りの調査"
date: 2015-11-17T08:04:04+09:00
comments: true
category: ['Tech']
tags: ['RD','Azure']
published: true
slug: remote-desktop-protocol
img: "https://farm6.staticflickr.com/5828/22680623077_383e4a6595_z.jpg" 
---


## Gateway

異なるネットワーク・プロトコルを使用する2つのネットワークを接続する任意のコンピュータ

## Remote Desktop Gateway

- 承認されたユーザが、インターネット接続が可能な任意のコンピュータから企業ネットワーク上のリモートコンピュータに接続できるようにする。
- RDP(Remote Desktop Protocol)とHTTPSプロトコルを利用する

### 利点

- VPN接続なしに、インターネットから企業ネットワークへのリモートデスクトップ接続ができる
- FWを経由してリモートコンピュータに接続可能
- コンピュータ上で実行中の他のプログラムと、ネットワーク環境を共有できる。これにより、企業ネットワークの代わりにISP接続を使用してリモート接続でデータを送受信できる

{{% googleadsense %}}

## 参考
-[ターミナル サービス ゲートウェイ サーバーとは](http://windows.microsoft.com/ja-jp/windows-vista/what-is-a-terminal-services-gateway-server)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/ta8utaUYSzyseC" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/SaSakiKuninobu/azuree4bbaee683b3e3839-ee382b7e383b3e381a8e4bbaee683b3e3838de38383e38388e383afe383bce382af" title="Azure仮想マシンと仮想ネットワーク" target="_blank">Azure仮想マシンと仮想ネットワーク</a> </strong> from <strong><a href="//www.slideshare.net/SaSakiKuninobu" target="_blank">Kuninobu SaSaki</a></strong> </div>
