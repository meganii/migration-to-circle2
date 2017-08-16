---

title: "[コツコツ勉強]よくわからないままJavaScriptを使っている自分へ"
date: 2014-11-28T23:32:00+09:00
comments: true
category: ['Tech']
tags: ['javascript']
published: true 
slug: javascript
img: "https://images-na.ssl-images-amazon.com/images/I/51c9uCrhHgL._SL160_.jpg"
---




jQuery、AngularJSとかサンプルを触ってみるけど、いまいちJavaScript自身がわかっていないので全然ピンと来ないので、巷でうわさの「サイ本」を読んでみる。

<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873115736/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/51c9uCrhHgL._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873115736/meganii-22/ref=nosim/" rel="nofollow" target="_blank">JavaScript 第6版</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">David Flanagan オライリージャパン 2012-08-10    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=JavaScript&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazon</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/0f1c1106.d5997202.117c2ed9.4ab7d4d2/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FJavaScript%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>



{{% googleadsense %}}


## 学んだ点


- スコープ
- 関数
- オブジェクト

### スコープ

関数スコープ・・・変数は、その変数が定義された関数と、その関数に入れ子にされている関数痛からアクセスできる。


### 関数

- JavaScriptでは、関数はオブジェクト
- 変数には関数そのものをいれることができる。
- 関数の入れ子ができる
- クロージャー
- 無名関数

グローバル変数をむやみに増やさないために、関数でラップしているイメージ。

### オブジェクト

- 不変な基本型と、可変なオブジェクト参照
- プロトタイプ (すべてのJavaScriptオブジェクトにはもうひとつ別のオブジェクトが関連付けられる)
- 暗黙の参照
	- メモリの使用量を節約する
	- メンバの追加・変更をインスタンスがリアルタイムに反映できる





<p><a href="https://www.flickr.com/photos/35571855@N06/15904453412" title="2014年11月29日11時09分37秒000by meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8626/15904453412_16fcf9d124_z.jpg" alt="2014年11月29日11時09分37秒000"></a></p>



<p><a href="https://www.flickr.com/photos/35571855@N06/15904454052" title="2014年11月29日11時09分37秒by meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7581/15904454052_ea152fb630_z.jpg" alt="2014年11月29日11時09分37秒"></a></p>

## 参考
- [JavaScript 徹底入門のための資料＆書籍まとめ - 酒と泪とRubyとRailsと](http://morizyun.github.io/blog/javascript-learning-tech-yourself_01/)
- [jQueryのソースコードを読むための参考サイト２０選 - DQNEO起業日記](http://dqn.sakusakutto.jp/2012/05/jquery-sourcecode-reading.html)
- [[JavaScript]　猿でもわかるクロージャ超入門　まとめ - DQNEO起業日記](http://dqn.sakusakutto.jp/2009/01/javascript_5.html)


## 感想

受験のときに、手にした「化学の新研究」並の万能感を得られました。
何かを学ぶときには、ネットの情報をちまちま読むよりは、ちゃんとした書籍を読んだ方がいいなと思いました。

<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873115736/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/51c9uCrhHgL._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873115736/meganii-22/ref=nosim/" rel="nofollow" target="_blank">JavaScript 第6版</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">David Flanagan オライリージャパン 2012-08-10    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=JavaScript&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazon</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/0f1c1106.d5997202.117c2ed9.4ab7d4d2/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FJavaScript%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>



<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4385260923/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/51TUx2LGZPL._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4385260923/meganii-22/ref=nosim/" rel="nofollow" target="_blank">化学の新研究―理系大学受験</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">卜部 吉庸 三省堂 2013-01-22    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=%89%BB%8Aw%82%CC%90V%8C%A4%8B%86&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazon</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/0f1c1106.d5997202.117c2ed9.4ab7d4d2/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E5%258C%2596%25E5%25AD%25A6%25E3%2581%25AE%25E6%2596%25B0%25E7%25A0%2594%25E7%25A9%25B6%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>
