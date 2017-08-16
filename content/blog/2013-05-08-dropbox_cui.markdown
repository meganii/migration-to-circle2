---

title: さくらVPSにDropboxをインストール
date: 2013-05-08T21:06:00+09:00
category: ['Tech']
tags: ["dropbox","vps"]
published: true
slug: dropbox_cui
---

ようやく重たい腰を上げて、さくらVPSにCUI版のDropboxをインストール。
Python2.6が必要みたいです。

以下のページを参考にさせてもらいました。
<a href="http://cl.pocari.org/2012-04-05-1.html" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://cl.pocari.org/2012-04-05-1.html" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://cl.pocari.org/2012-04-05-1.html" target="_blank">cl.pocari.org - さくらの VPS (CentOS 6.2) にコマンドライン版 Dropbox をインストールする</a><a href="http://b.hatena.ne.jp/entry/http://cl.pocari.org/2012-04-05-1.html" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://cl.pocari.org/2012-04-05-1.html" alt="" /></a><br style="clear:both;" /><br>


{{% googleadsense %}}

### Dropbox CLIをダウンロード
```
$ wget https://www.dropbox.com/download?dl=packages/dropbox.py
```

### インストール
```
$./dropbox.py start --install
Starting Dropbox...
Dropbox is the easiest way to share and store your files online. Want to learn more? Head to https://www.dropbox.com/

In order to use Dropbox, you must download the proprietary daemon. [y/n] y
Downloading Dropbox... 100%
Unpacking Dropbox... 100%
Dropbox isn't running!
Done!
```

### Dropboxアカウントへのリンク
```
$ ./dropbox.py start
```
ここで表示されるリンクにアクセスして、Dropboxアカウントとの紐付けを行う。

### 再起動
```
$ ./dropbox.py stop
$ ./dropbox.py start
```

これで、 $HOME/Dropboxが同期されるように！意外と簡単！！

### LAN Syncを止める
```
$ dropbox.py lansync n
```
17500/udp でのブロードキャストが行われて大変みたいです。


<a href="http://nefo.hatenablog.com/entry/20111001/1317481919" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://nefo.hatenablog.com/entry/20111001/1317481919" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://nefo.hatenablog.com/entry/20111001/1317481919" target="_blank">CLI DropboxのLAN Syncを止める - じゃ、ま、いっか</a><a href="http://b.hatena.ne.jp/entry/http://nefo.hatenablog.com/entry/20111001/1317481919" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://nefo.hatenablog.com/entry/20111001/1317481919" alt="" /></a><br style="clear:both;" /><br>



### Octpress用に、.dropboxを省く設定を追加
source/_posts/を共有させるようにしたため、deployしようとすると怒られる。

```
$ bundle exec rake deploy
cp -r source/_posts/.dropbox public/_posts/.dropbox
rake aborted!
No such file or directory - public/_posts/.dropbox
```

.dropboxを無視するように、Rakefileを修正。
excludeの中に、```**/.dropbox```を追加。


```
desc "copy dot files for deployment"
task :copydot, :source, :dest do |t, args|
  FileList["#{args.source}/**/.*"].exclude("**/.", "**/..", "**/.DS_Store", "**/._*", "**/.dropbox").each do |file|
    cp_r file, file.gsub(/#{args.source}/, "#{args.dest}") unless File.directory?(file)
  end
end
```



### 参考
- [cl.pocari.org - さくらの VPS (CentOS 6.2) にコマンドライン版 Dropbox をインストールする](http://cl.pocari.org/2012-04-05-1.html)
- [さくらVPSサーバにDropboxをインストール | Everyday Deadlock](http://hayamiz.com/~haya/blog/?p=155)


