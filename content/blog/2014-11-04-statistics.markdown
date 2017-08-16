---
title: "[こつこつ勉強]統計学入門#1" 
date: 2014-11-04T23:02:00+09:00
comments: true
category: ['Study']
tags: ['統計学']
published: true
slug: statistics
img: "https://images-na.ssl-images-amazon.com/images/I/41OfaN1i6qL._SL160_.jpg"
---

統計、統計と言われても全然ぴんと来ないので、こつこつ勉強し始めようかと思います。


ネットを見てると、以下の本がおすすめされてたので、まずはざっと読んでみることにします。

<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4478820090/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/41OfaN1i6qL._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4478820090/meganii-22/ref=nosim/" rel="nofollow" target="_blank">完全独習 統計学入門</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">小島 寛之 ダイヤモンド社 2006-09-29    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=%93%9D%8Cv%8Aw&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazonで購入</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/0f1c1106.d5997202.117c2ed9.4ab7d4d2/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E7%25B5%25B1%25E8%25A8%2588%25E5%25AD%25A6%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場で購入</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>


<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4274065707/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/51EFK1XNQ5L._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4274065707/meganii-22/ref=nosim/" rel="nofollow" target="_blank">マンガでわかる統計学</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">高橋 信,トレンドプロ オーム社 2004-07    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=%93%9D%8Cv%8Aw&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazonで購入</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/0f1c1106.d5997202.117c2ed9.4ab7d4d2/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E7%25B5%25B1%25E8%25A8%2588%25E5%25AD%25A6%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場で購入</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>



{{% googleadsense %}}



## 度数分布表を作成する

縮約・・・データとして並んでいるたくさんの数字を何かの基準で、整理整頓して意味のある情報だけを抽出する。

頭に入れておく言葉

- 階級
- 階級値
- 度数
- 相対度数
- 累積度数


<p><a href="https://www.flickr.com/photos/35571855@N06/15707333451" title="度数分布表by meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7512/15707333451_7026845e13_z.jpg" alt="度数分布表"></a></p>


## 平均値とは何か？

改めて、算術平均、相乗平均(幾何平均)、二乗平均、調和平均という平均を確認した。

<p><a href="https://www.flickr.com/photos/35571855@N06/15524045407" title="平均値とは？by meganii, on Flickr"><img class="img-responsive" src="https://farm4.staticflickr.com/3938/15524045407_04b3a12d02_z.jpg" alt="平均値とは？"></a></p>

## 標準偏差

標準偏差(Standard Deviation) S.D. 広がり・散らばりを評価する。


<p><a href="https://www.flickr.com/photos/35571855@N06/15523827278" title="2014年11月03日21時22分06秒by meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7489/15523827278_a590568a2c_z.jpg" alt="2014年11月03日21時22分06秒"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/15524390470" title="標準正規分布by meganii, on Flickr"><img class="img-responsive" src="https://farm6.staticflickr.com/5607/15524390470_9711a10520_z.jpg" alt="標準正規分布"></a></p>

## シャープレシオ

金融の世界の指標として頭にいれておきたい。

<p><a href="https://www.flickr.com/photos/35571855@N06/15685513756" title="シャープレシオby meganii, on Flickr"><img class="img-responsive" src="https://farm6.staticflickr.com/5601/15685513756_7b331fde50_z.jpg" alt="シャープレシオ"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/15524390180" title="S.D.by meganii, on Flickr"><img class="img-responsive" src="https://farm4.staticflickr.com/3954/15524390180_48bf1fbb57_z.jpg" alt="S.D."></a></p>

## 母平均
<p><a href="https://www.flickr.com/photos/35571855@N06/15709234435" title="2014年11月03日21時21分53秒by meganii, on Flickr"><img class="img-responsive" src="https://farm4.staticflickr.com/3955/15709234435_4fcb18fa42_z.jpg" alt="2014年11月03日21時21分53秒"></a></p>

