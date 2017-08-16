---

title: 2台目のMacBookAirからさくらVPSへSSH接続を行うための鍵の設定
date: 2013-06-21T21:16:00+09:00
category: ['Tech']
tags: ['さくらvps']
published: true
slug: ssh-sakuravps
---

新しくMacBookAirを買ったので、さくらVPSへSSH接続を行うための鍵の設定。

<a href="http://meganii.com/blog/2013/06/18/macbookair/" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://meganii.com/blog/2013/06/18/macbookair/" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://meganii.com/blog/2013/06/18/macbookair/" target="_blank">念願のAir!! MacBookAir Mid 2013買いました - じょーぶん男子</a><a href="http://b.hatena.ne.jp/entry/http://meganii.com/blog/2013/06/18/macbookair/" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://meganii.com/blog/2013/06/18/macbookair/" alt="" /></a><br style="clear:both;" /><br>


{{% googleadsense %}}

```
su
vim /etc/ssh/sshd_config
```

パスワードによるログインを許可する

```
PasswordAuthentication yes
```


設定を変えたら、sshdを再起動。

```
service sshd restart
```

鍵を作る

```
ssh-keygen
```

id_rsa.pubという公開鍵が作られる。（ここでは、id_rsa_sakura.pubに変更）

```
cp id_rsa.pub id_rsa_sakura.pub
```

さくらVPS(CentOS)に配置。

```
scp -P port ~/.ssh/id_rsa.pub user@example.com:~/.ssh/id_rsa_sakura.pub 
```

さくらVPS側で スーパーユーザになって、authorized_keysに、作った公開鍵を入れておけばよいみたい。

cat id_rsa_sakura.pub >> authorized_keys


パスワードによるログインを無効に戻す

```
PasswordAuthentication yes
```


これで2台目のMacBookAirからSSH接続できるようになりました。

## 参考
- [CentOS で公開鍵暗号方式を使用した SSH ログイン設定: あるＳＥのつぶやき](http://fnya.cocolog-nifty.com/blog/2012/03/centos-ssh-8291.html)
- [Macのターミナルから「さくらVPS」にSSHリモート接続＆鍵方式でログインする方法（複数のid_rsaを管理） - おしい県で働くプチブログラマのブログ](http://cashew.hatenablog.com/entry/2013/02/10/Mac%E3%81%AE%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%81%8B%E3%82%89%E3%80%8C%E3%81%95%E3%81%8F%E3%82%89VPS%E3%80%8D%E3%81%ABSSH%E3%83%AA%E3%83%A2%E3%83%BC%E3%83%88%E6%8E%A5%E7%B6%9A%EF%BC%86)
- [さくらVPS – 複数環境からSSH接続する | shibuya blog](http://blog.kazuhiroshibuya.com/archives/51461147.html)
- [さくらのVPS を改めて使いはじめる 1 – 使用準備、SSH 公開鍵認証 | アカベコマイリ](http://akabeko.me/blog/2012/04/revps-01-prepare-ssh-key/)
- [さくらVPS申し込み～SSHするまで - ASとか](http://d.hatena.ne.jp/murakaming/20120619/1340129460)
- [sshd](http://open-groove.net/linux/sshd-restart/)


<a href="http://www.amazon.co.jp/exec/obidos/ASIN/B008B3AMMO/" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://www.amazon.co.jp/exec/obidos/ASIN/B008B3AMMO/" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://www.amazon.co.jp/exec/obidos/ASIN/B008B3AMMO/" target="_blank">Amazon.co.jp： APPLE MacBook Air 1.8GHz Core i5/13.3/4GB/128GB MD231J/A: パソコン・周辺機器</a><a href="http://b.hatena.ne.jp/entry/http://www.amazon.co.jp/exec/obidos/ASIN/B008B3AMMO/" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://www.amazon.co.jp/exec/obidos/ASIN/B008B3AMMO/" alt="" /></a><br style="clear:both;" /><br>

