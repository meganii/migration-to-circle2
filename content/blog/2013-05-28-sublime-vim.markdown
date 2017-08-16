---

title: sublime-vim
date: 2013-05-28T21:02:00+09:00
category: ['Tech']
tags: 
published: true
slug: sublime-vim
---

そろそろ重たい腰を上げて、vi系のコマンドを覚えたいなと思い始めたので、Sublime Text 2をVimっぽく操作するようにカスタマイズしてみようと思う。

<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4774143960/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/518fmwtEh0L._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4774143960/meganii-22/ref=nosim/" rel="nofollow" target="_blank">vi/Vim コマンドポケットリファレンス</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">山森 丈範 技術評論社 2010-10-22    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=%83R%83%7D%83%93%83h%83%7C%83P%83b%83g%83%8A%83t%83%40%83%8C%83%93%83X&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazon</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/10b94576.1f973e7e.10b94577.43b11258/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E3%2582%25B3%25E3%2583%259E%25E3%2583%25B3%25E3%2583%2589%25E3%2583%259D%25E3%2582%25B1%25E3%2583%2583%25E3%2583%2588%25E3%2583%25AA%25E3%2583%2595%25E3%2582%25A1%25E3%2583%25AC%25E3%2583%25B3%25E3%2582%25B9%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>

参考にさせてもらいながら、設定変更。
[Vimと僕とSublime - fukayatsu.dev](http://blog.fukayatsu.com/2013/01/02/vim-advent-calendar/)


{{% googleadsense %}}

メニューからPreferences > Settings-User(⌘,)
を選択して、以下の様に追加します(Mac向け)。

```
 "ignored_packages": [""],
 "vintage_ctrl_keys": true,
 "vintage_start_in_command_mode": true
```

[Vintage Mode - Sublime Text 2 Documentation](http://www.sublimetext.com/docs/2/vintage.html)

Package Control を導入して、VintageExを導入。
 
