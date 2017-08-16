---

title: リモートディスクを利用してMacBookProのDVDドライブからMacBookAirにソフトウェアをインストール
date: 2013-06-25T20:45:00+09:00
category: ['Tech']
tags: ['Mac']
published: true
slug: remote-disk
---

MacBookAirには、CD/DVDドライブがついていない。過去のソフトをどうやって新しく買ったインストールしようかと思って、なんとかMacBookProのDVDドライブを使えないか調べてみると、「リモートディスク」が使えるっぽい。

<a href="http://support.apple.com/kb/HT5287?viewlocale=ja_JP" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://support.apple.com/kb/HT5287?viewlocale=ja_JP" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://support.apple.com/kb/HT5287?viewlocale=ja_JP" target="_blank">DVD or CD sharing：リモートディスクを使う</a><a href="http://b.hatena.ne.jp/entry/http://support.apple.com/kb/HT5287?viewlocale=ja_JP" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://support.apple.com/kb/HT5287?viewlocale=ja_JP" alt="" /></a><br style="clear:both;" /><br>

早速、iWorkをリモートディスクを使ってインストールしてみた。


{{% googleadsense %}}
<br>
<br>
## 1.まずMacBookPro側でリモートディスクを有効にする

システム環境設定の共有から
<p><a href="http://www.flickr.com/photos/35571855%40N06/9132825549/" title="システム環境設定 by meganii, on Flickr" target="_blank"><img class="flickr_photo" src="http://farm6.staticflickr.com/5337/9132825549_538b90ce83.jpg"  alt="システム環境設定" width="400px"/></a><br /><cite class="flickr_photographer"><img src="http://farm7.static.flickr.com/6002/5974401716_35b6041cdc.jpg" width="16" /><a href="http://www.flickr.com/photos/35571855%40N06/9132825549/">システム環境設定</a> Photo by <a href="http://www.flickr.com/photos/35571855%40N06/">meganii</a></cite></p>

DVDまたはCD共有を選択
<p><a href="http://www.flickr.com/photos/35571855%40N06/9135024638/" title="リモートディスク by meganii, on Flickr" target="_blank"><img class="flickr_photo" src="http://farm3.staticflickr.com/2828/9135024638_03421750e2.jpg"  alt="リモートディスク" width="400px"/></a><br /><cite class="flickr_photographer"><img src="http://farm7.static.flickr.com/6002/5974401716_35b6041cdc.jpg" width="16" /><a href="http://www.flickr.com/photos/35571855%40N06/9135024638/">リモートディスク</a> Photo by <a href="http://www.flickr.com/photos/35571855%40N06/">meganii</a></cite></p>


## 2.MacBookProでネットワークを作成

適当にパスワードを作って、ネットワークを作成します。
<p><a href="http://www.flickr.com/photos/35571855@N06/9133002529/" title="Create Network1 by meganii, on Flickr"><img src="http://farm8.staticflickr.com/7352/9133002529_139f7d77db.jpg" width="364" height="66" alt="Create Network1"></a></p>

<p><a href="http://www.flickr.com/photos/35571855%40N06/9133002547/" title="Create Network2 by meganii, on Flickr" target="_blank"><img class="flickr_photo" src="http://farm4.staticflickr.com/3779/9133002547_264b7cb6a4.jpg"  alt="Create Network2" width="400px"/></a><br /><cite class="flickr_photographer"><img src="http://farm7.static.flickr.com/6002/5974401716_35b6041cdc.jpg" width="16" /><a href="http://www.flickr.com/photos/35571855%40N06/9133002547/">Create Network2</a> Photo by <a href="http://www.flickr.com/photos/35571855%40N06/">meganii</a></cite></p>


### ご参考
<a href="http://blog.motta.jp/2013/06/macbookmacbookwifi.html" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://blog.motta.jp/2013/06/macbookmacbookwifi.html" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://blog.motta.jp/2013/06/macbookmacbookwifi.html" target="_blank">旧Macbookから新Macbookへの移行を高速に行う方法(WiFi経由)</a><a href="http://b.hatena.ne.jp/entry/http://blog.motta.jp/2013/06/macbookmacbookwifi.html" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://blog.motta.jp/2013/06/macbookmacbookwifi.html" alt="" /></a><br><span style="color: #808080;font-size: 80%;">アドホックネットワークの作り方 ...</span><br style="clear:both;" /><br>

## 3.MacBookAir側でリモートディスクの使用依頼をMacBookProに送る
先ほど、MacBookProで作成したネットワークに接続すると、リモートディスクから、MacBookProが見えているはずです。

<p><a href="http://www.flickr.com/photos/35571855%40N06/9133002597/" title="RemoteDisk2 by meganii, on Flickr" target="_blank"><img class="flickr_photo" src="http://farm4.staticflickr.com/3811/9133002597_c906d1e466.jpg"  alt="RemoteDisk2" width="400px"/></a><br /><cite class="flickr_photographer"><img src="http://farm7.static.flickr.com/6002/5974401716_35b6041cdc.jpg" width="16" /><a href="http://www.flickr.com/photos/35571855%40N06/9133002597/">RemoteDisk2</a> Photo by <a href="http://www.flickr.com/photos/35571855%40N06/">meganii</a></cite></p>

このMacBookProをクリックして、右上の使用を依頼を押す。
<p><a href="http://www.flickr.com/photos/35571855%40N06/9135222996/" title="RemoteDisk by meganii, on Flickr" target="_blank"><img class="flickr_photo" src="http://farm4.staticflickr.com/3707/9135222996_86c1f006ed.jpg"  alt="RemoteDisk" width="400px"/></a><br /><cite class="flickr_photographer"><img src="http://farm7.static.flickr.com/6002/5974401716_35b6041cdc.jpg" width="16" /><a href="http://www.flickr.com/photos/35571855%40N06/9135222996/">RemoteDisk</a> Photo by <a href="http://www.flickr.com/photos/35571855%40N06/">meganii</a></cite></p>

## 4.MacBookPro側で許可する

これで、MacBookProにCDを入れると、MacBookAir側で認識することができました。


あとは、好きにソフトをインストールするだけです。


## 注意
ただし、以下のタイプのディスクや操作は、DVD または CD 共有でサポートされていないそうです。
- DVD ムービー
- オーディオ CD
- ゲームディスクなど、コピーガード (複製防止機能) がかかっているディスク 
- Microsoft Windows (Boot Camp で使用) または Mac OS X などのオペレーティングシステムのインストールディスク。
- CD または DVD の作成	

音楽CDぐらい取り込ませてくれてもいいのにね。

でも、これで、無駄にDVDドライブを買わずにすみました。もしも、困っていらっしゃる方がいたらぜひお試しください。
