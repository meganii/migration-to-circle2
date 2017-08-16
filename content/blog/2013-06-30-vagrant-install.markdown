---

title: 勉強用に、簡単に作っては壊せる仮想環境をVagrantで構築する
date: 2013-06-30T06:39:00+09:00
category: ['Tech']
tags: ['vagrant']
published: true
slug: vagrant-install
---

簡単に作っては壊せる環境があれば、勉強にはいいのかなと思い、まずは、簡単に仮想環境を作る環境を探しました。すると、Vagrantというツールがあることが分かりましたので、インストールして、環境構築を行なってみました。


## Vagrantとは
>Vagrant は、Ruby で組まれたスクリプトで、仮想マシン上の開発環境の構築・配布の自動化を支援するためのツール。仮想マシン環境(VirtualBox) と構成管理ツール(Chef, Puppet)を利用することで実現している。これを使えば、コマンド一つで、開発に必要な環境を用意できるようになる。 [Vagrant で開発環境構築を自動化しよう - エンジニアきまぐれTips](http://d.hatena.ne.jp/okinaka/20110717/1310892601)

<a href="http://docs.komagata.org/4673" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://docs.komagata.org/4673" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://docs.komagata.org/4673" target="_blank">触りだけでも便利なVagrant - komagata</a><a href="http://b.hatena.ne.jp/entry/http://docs.komagata.org/4673" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://docs.komagata.org/4673" alt="" /></a><br style="clear:both;" /><br>



{{% googleadsense %}}


## Vitrualbox ダウンロード
[Downloads – Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)

最初は、トップページからダウンロードできる最新版を利用したところ、Vagrant v1.2.2と相性が悪かったみたいで、以下のバージョン(4.2.8)を入れなおした。	

http://download.virtualbox.org/virtualbox/4.2.8/VirtualBox-4.2.8-83876-OSX.dmg

## Vagrant
[Vagrant](http://www.vagrantup.com/)のDownloadsから v1.2.2をダウンロード。	


## 環境を追加する
```
vagrant box add centos6.4 http://developer.nrel.gov/downloads/vagrant-boxes/CentOS-6.4-x86_64-v20130427.box
Downloading or copying the box...
Extracting box...te: 61981/s, Estimated time remaining: 0:00:02)
Successfully added box 'centos6.4' with provider 'virtualbox'!
```


上記のコマンドで、CentOSのVagrantfilesが作られる。~/.vagrant に box がキャッシュされる
その後に、'vagrant up'を実行すれば、環境が作られるはずだったが、ここでエラー。

```
vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
[default] Importing base box 'centos6.4'...
There was an error while executing `VBoxManage`, a CLI used by Vagrant
for controlling VirtualBox. The command and stderr is shown below.

Command: ["import", "/Users/meganii/.vagrant.d/boxes/centos6.4/virtualbox/box.ovf"]

Stderr: 0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Interpreting /Users/meganii/.vagrant.d/boxes/centos6.4/virtualbox/box.ovf...
OK.
0%...
Progress object failure: NS_ERROR_CALL_FAILED
```

どうやら、Virtual Boxのバージョンと、Vagrantのバージョンに相性があるみたい。
[windows7 - Windows 7でVagantを使う時はVirtual Boxのバージョンに注意 - Qiita [キータ]](http://qiita.com/yando/items/4a9acdcf3503230957e5)

VirtualBoxのバージョンを4.2.8したところ以下のように正しく動作した。

```
vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
[default] Importing base box 'centos6.4'...
[default] Matching MAC address for NAT networking...
[default] Setting the name of the VM...
[default] Clearing any previously set forwarded ports...
[default] Creating shared folders metadata...
[default] Clearing any previously set network interfaces...
[default] Preparing network interfaces based on configuration...
[default] Forwarding ports...
[default] -- 22 => 2222 (adapter 1)
[default] Booting VM...
[default] Waiting for VM to boot. This can take a few minutes.
[default] VM booted and ready for use!
[default] Configuring and enabling network interfaces...
[default] Mounting shared folders...
[default] -- /vagrant
```

以下のコマンドで、作成した仮想環境にSSH接続できる。root パスワードは "vagrant"みたい。
```
vagrant ssh
```

```
cat /etc/redhat-release
CentOS release 6.4 (Final)
```

簡単にCentOSの環境が作られました!!



## 参考
- [A list of base boxes for Vagrant - Vagrantbox.es](http://www.vagrantbox.es/)
- [Vagrant - naoyaのはてなダイアリー](http://cdn-ak.f.st-hatena.com/images/fotolife/n/naoya/20130205/20130205195831.png)
- [Vagrant コトハジメ](https://gist.github.com/voluntas/5525719)
- [Vagrant のベースBOX作成手順 (Scientific Linux 6.1) - エンジニアきまぐれTips](http://d.hatena.ne.jp/okinaka/20110805/1312474847)
- [chef-solo で学ぶ chef の基本動作 - jedipunkz' blog](http://jedipunkz.github.io/blog/2012/08/18/chef-solo/)

chef-soloっていうサーバー構築自動化ツールもあるみたいです。



### CentOSのバージョンを確認する方法
'cat /etc/redhat-releas'



