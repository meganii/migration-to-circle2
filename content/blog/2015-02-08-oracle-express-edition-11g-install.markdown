---

title: "Vagrant上のCentOS6.4にOracle Database Express Edition11gをインストールする"
date: 2015-02-08T15:11:00+09:00
comments: true
category: ['Tech']
tags: ['Oracle','database']
published: true
img: "https://farm9.staticflickr.com/8640/16468400201_39ccfefbac_s.jpg" 
slug: oracle-express-edition-11g-install
---


学習用として、ローカルにOracleが欲しかったので、無償版のExpress EditionをVagrantで作成したCentOSにインストールした。


Vagrantで作成したCentOS6.4にOracle XEをインストールする流れは、以下のとおり。

1. Vagrantの設定(ホスト側作業)
2. Oracle Database Express Edition 11gのダウンロード(ホスト側作業)
3. Oracleインストールに必要なパッケージのインストール(ゲストOS側作業)
4. Oracleインストール(ゲストOS側作業)


{{% googleadsense %}}


## 前提
- VirtualBox version 4.3.14
- Vagrant 1.6.3
- Oracle Database Express Edition 11g R2
- ホストOS: Mac OS X Mavericks
- ゲストOS: CentOS 6.4 x86_64 Minimal(20140116)
[Release CentOS 6.4 x86_64 Minimal (2014-01-16) · 2creatives/vagrant-centos](https://github.com/2creatives/vagrant-centos/releases/tag/v6.4.2)



## 1. Vagrantの設定(ホスト側作業)

### Vagrantの追加

Vagrantのインストール、Virtualboxのインストールについては、割愛する。

### ネットワークの設定

Vagrantfileに、利用したいIPアドレスを記載する。

```
# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos64-x86_64-20140116"

  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"
end

```

### 共有フォルダ設定

CentOS側からみれる共有フォルダを用意する。

<p><a href="https://www.flickr.com/photos/35571855@N06/16444231326" title="Vagrant share folderby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7423/16444231326_e7bed11e94_z.jpg" alt="Vagrant share folder"></a></p>



### CentOSを立ち上げる
```
vagrant up
```



## 2. Oracle Database Express Edition 11gのダウンロード(ホスト側作業)
下記のリンクからExpress Editionをダウンロードする。
(要オラクルアカウント。登録は無料です)

http://www.oracle.com/technetwork/jp/database/database-technologies/express-edition/downloads/index.html

ダウンロードが完了したら、共有フォルダに格納しておく。


3. Oracleインストールに必要なパッケージのインストール(ゲストOS側作業)

[公式ドキュメント](http://docs.oracle.com/cd/E17781_01/install.112/e18802/toc.htm#XEINL102)を見てみると、必要なパッケージは以下のものとなっている。


- glibc should be greater than or equal to 2.3.4-2.41
- make should be greater than or equal to 3.80
- binutils should be greater than or equal to 2.16.91.0.5
- gcc should be greater than or equal to 4.1.2
- libaio should be greater than or equal to 0.3.104


### libaio, bcのインストール

今回は、`yum`で`libaio`と`bc`をインストールでOracle XEのインストール要件は満たされた。

```
yum install libaio bc
```


### hostsファイルにコンピュータ名を追加

```
vi /etc/hosts
```

```diff
- 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
+ 127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4 vagrant-centos64.vagrantup.com
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
```

コンピュータ名は、`hostname`で得ることができる。



## 4. Oracleインストール

### rpmによるインストール

```
rpm -ivh oracle-xe-11.2.0-1.0.x86_64.rpm
```

```
$ rpm -ivh oracle-xe-11.2.0-1.0.x86_64.rpm
Preparing...                ########################################### [100%]
   1:oracle-xe              ########################################### [100%]
Executing post-install steps...
You must run '/etc/init.d/oracle-xe configure' as the root user to configure the database.
```

### 構築

以下のコマンドを叩いて、databaseを構築する。

```
/etc/init.d/oracle-xe configure
```


```
Oracle Database 11g Express Edition Configuration
-------------------------------------------------
This will configure on-boot properties of Oracle Database 11g Express
Edition.  The following questions will determine whether the database should
be starting upon system boot, the ports it will use, and the passwords that
will be used for database accounts.  Press <Enter> to accept the defaults.
Ctrl-C will abort.

Specify the HTTP port that will be used for Oracle Application Express [8080]:

Specify a port that will be used for the database listener [1521]:

Specify a password to be used for database accounts.  Note that the same
password will be used for SYS and SYSTEM.  Oracle recommends the use of
different passwords for each database account.  This can be done after
initial configuration:
Confirm the password:

Do you want Oracle Database 11g Express Edition to be started on boot (y/n) [y]:y

Starting Oracle Net Listener...Done
Configuring database...Done
Starting Oracle Database 11g Express Edition instance...Done
Installation completed successfully.
```



## 稼働確認

iptablesを一時的に無効にして、http://192.168.33.10:8080 にアクセスした。
(IPアドレス192.168.33.10の部分は、Vagrantfileに記載のもの)

ユーザ名とパスワードは下記の通り。

- ユーザ名： system
- パスワード： インストール時に設定したもの


以下のページが表示されて、Oracleが動いていることがわかる。

<p><a href="https://www.flickr.com/photos/35571855@N06/16468400201" title="oracle xe installby meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8640/16468400201_39ccfefbac_z.jpg" alt="oracle xe install"></a></p>

##参考
- [ swapon /swapfile](https://gist.github.com/koudaiii/0ed6a8558aa297af463e)
- [linux スワップ（swap）領域の作成](http://kazmax.zpp.jp/linux_beginner/mkswap.html)
- [http://docs.oracle.com/cd/E11882_01/install.112/e24326/toc.htm#BHCGJCEA](http://docs.oracle.com/cd/E11882_01/install.112/e24326/toc.htm#BHCGJCEA)
