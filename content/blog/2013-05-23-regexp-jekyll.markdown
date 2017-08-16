---

title: Jekyllのお勉強 -YAML部分と記事本文を分離する正規表現-
date: 2013-05-23T07:19:00+09:00
category: ['Tech']
tags: ['jekyll','正規表現']
published: true
slug: regexp-jekyll
---

JekyllのYAML部分と記事本文を分離していると思われる正規表現を確認する。

正規表現	
```
/\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
```

こんな感じらしい

<a href="http://www.flickr.com/photos/35571855@N06/8802953102/" title="20130522224919 by meganii, on Flickr"><img src="http://farm8.staticflickr.com/7340/8802953102_f2b245cfb1.jpg" width="400" /></a>



{{% googleadsense %}}

```ruby
# Read the YAML frontmatter.
#
# base - The String path to the dir containing the file.
# name - The String filename of the file.
#
# Returns nothing.
def read_yaml(base, name)
  begin
    self.content = File.read(File.join(base, name))

    if self.content =~ /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
      self.content = $POSTMATCH
      self.data = YAML.safe_load($1)
    end
  rescue SyntaxError => e
    puts "YAML Exception reading #{File.join(base, name)}: #{e.message}"
  rescue Exception => e
    puts "Error reading file #{File.join(base, name)}: #{e.message}"
  end

  self.data ||= {}
end
```

## 参考
 <a href="http://doc.ruby-lang.org/ja/1.9.3/doc/spec=2fregexp.html" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://doc.ruby-lang.org/ja/1.9.3/doc/spec=2fregexp.html" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://doc.ruby-lang.org/ja/1.9.3/doc/spec=2fregexp.html" target="_blank">正規表現</a><a href="http://b.hatena.ne.jp/entry/http://doc.ruby-lang.org/ja/1.9.3/doc/spec=2fregexp.html" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://doc.ruby-lang.org/ja/1.9.3/doc/spec=2fregexp.html" alt="" /></a><br style="clear:both;" /><br>

 <div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873114500/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/51v9IZgj%2BeL._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873114500/meganii-22/ref=nosim/" rel="nofollow" target="_blank">正規表現クックブック</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">Jan Goyvaerts,Steven Levithan オライリージャパン 2010-04-15    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=%90%B3%8BK%95%5C%8C%BB%83N%83b%83N%83u%83b%83N&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazon</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/10b94576.1f973e7e.10b94577.43b11258/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E6%25AD%25A3%25E8%25A6%258F%25E8%25A1%25A8%25E7%258F%25BE%25E3%2582%25AF%25E3%2583%2583%25E3%2582%25AF%25E3%2583%2596%25E3%2583%2583%25E3%2582%25AF%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>
