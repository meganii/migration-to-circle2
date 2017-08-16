---

title: "UTF-8-MACとは何か？〜Jekyllのカテゴリ(タグ)ページで濁点を含むページが表示されない〜"
date: 2014-11-29T23:01:00+09:00
comments: true
category: ['Tech']
tags: ['jekyll','文字コード']
published: true 
slug: jekyll-tags-unread-because-of-utf-8-mac
img: "https://farm9.staticflickr.com/8582/15904473402_eeaa56b76f_z.jpg"
---


Macでファイル作成し、その後、rsyncでさくらVPS(CentOS)に転送しているのだが、濁点を含むファイルだけが表示されない。

例えば、「リファクタリング」など。
http://meganii.com/blog/tag/リファクタリング/




{{% googleadsense %}}

## 原因

Mac OSXが作成した濁点、半濁点を含むファイル名を、CentOS側では異なる文字と認識しているのが原因みたい。

一般的に、UTF-8と表現される場合、NFC(Normalization Form C)でエンコードされたものを指す。

一方、Mac OSXでは、NFD(Normalization Form D)で符号化したUTF-8が用いられ、iconvではこれをUTF-8-MACと呼んでいる。

同じUTF-8でも、NFCとNFDという解釈の違いが存在するため、この現象が起きる。




例えば、「が」を例にすると、

NFCだと、「が」と1文字で表現されるところが、
NFDだと、分解されて「か」と「゜」で表現される。

<p><a href="https://www.flickr.com/photos/35571855@N06/15904473402" title="nfdndcby meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8582/15904473402_eeaa56b76f_z.jpg" alt="nfdndc"></a></p>



## 解決策

- rsyncのバージョンを3.0に上げる
- オプション`--iconv=UTF-8-MAC,UTF-8`をつけて実行

※ オプション`iconv`は、バージョン3.0からしか利用出来ない

これによって、`UTF-8-MAC`を`UTF-8`に変換して、サーバに転送する。

### rsyncアップロード

Homebrewでインストール。

```bash
brew tap homebrew/dupes
brew install libiconv
brew install rsync
```

### Rakefileの変更

```diff
 desc "deploy_to_sakura"
 task :deploy_to_sakura do
   sh "jekyll build"
-  sh 'rsync -e -avz --delete _site/ meganii@11.111.111.111:/home/meganii/jekyll
+  sh 'rsync --iconv=UTF-8-MAC,UTF-8 -e -avz --delete _site/ meganii@11.111.111.111/home/meganii/jekyll
 end
```

## 手書きメモ
<p><a href="https://www.flickr.com/photos/35571855@N06/15719329297" title="2014年11月29日22時34分48秒000by meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7482/15719329297_f662ce2376_z.jpg" alt="2014年11月29日22時34分48秒000"></a></p>



## 参考

<a href="http://gam0022.net/blog/2012/08/11/use-rsync-iconv-option/" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://gam0022.net/blog/2012/08/11/use-rsync-iconv-option/" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://gam0022.net/blog/2012/08/11/use-rsync-iconv-option/" target="_blank">カテゴリー名に濁点を含んだ日本語が使えない問題を解決する(Rsyncのiconvオプションを使う) - gam0022.net</a><a href="http://b.hatena.ne.jp/entry/http://gam0022.net/blog/2012/08/11/use-rsync-iconv-option/" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://gam0022.net/blog/2012/08/11/use-rsync-iconv-option/" alt="" /></a><br><span style="color: #808080;font-size: 80%;">brew tap homebrew/dupes #リポジトリを追加 brew install libiconv #iconvオプションを使うために必須のよう brew install rsync ...</span><br style="clear:both;" /><br>

<a href="http://d.hatena.ne.jp/miau/20110805/1312555736" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://d.hatena.ne.jp/miau/20110805/1312555736" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://d.hatena.ne.jp/miau/20110805/1312555736" target="_blank">Mac OS Xの濁点ファイルがやってきた - miauの避難所</a><a href="http://b.hatena.ne.jp/entry/http://d.hatena.ne.jp/miau/20110805/1312555736" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://d.hatena.ne.jp/miau/20110805/1312555736" alt="" /></a><br style="clear:both;" /><br>

<a href="http://macwiki.sourceforge.jp/wiki/index.php/UTF-8-MAC" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://macwiki.sourceforge.jp/wiki/index.php/UTF-8-MAC" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://macwiki.sourceforge.jp/wiki/index.php/UTF-8-MAC" target="_blank">MacWiki - UTF-8-MAC</a><a href="http://b.hatena.ne.jp/entry/http://macwiki.sourceforge.jp/wiki/index.php/UTF-8-MAC" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://macwiki.sourceforge.jp/wiki/index.php/UTF-8-MAC" alt="" /></a><br style="clear:both;" /><br>

[UTF-8にもいろいろある - ザリガニが見ていた...。](http://d.hatena.ne.jp/zariganitosh/20131124/utf8_nfd_nfc_bom)
[文字エンコードとロケールを体感する - ザリガニが見ていた...。](http://d.hatena.ne.jp/zariganitosh/20131118/text_encoding_locale_feeling)
