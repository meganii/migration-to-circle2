---
title: "MariaDBの日本語文字化けを解消するための設定"
date: 2016-05-29T15:55:28+09:00
comments: true
category: ['Tech']
tags: ['MariaDB', 'DB']
published: true
slug: mariadb-utf8
img: 'https://images-na.ssl-images-amazon.com/images/I/51pj9W0WxzL._SL160_.jpg'
---

Ruby on RailsからMariaDBを利用した時に、文字化けが発生したのでMariaDBの設定内容を見直した。


## 前提

MariaDBのバージョン

```
Server version: 10.1.10-MariaDB MariaDB Server
```

{{% googleadsense %}}

## 文字化けする

character_set_server, character_set_databaseが、latin1になっているのが原因で、新規作成したデータベース、テーブルの文字latin1になっていた。


```
MariaDB [(none)]> show variables like 'char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | latin1                     |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
```

### 各設定の説明

|設定値                    |	説明               |
|:------------------------|:------------------------------------------------------------------------|
|character_set_client	    |クライアント => サーバーにメッセージを送る際に使われるキャラセット                 |
|character_set_connection	|クライアントが送ったクエリをサーバーが解析する際、このキャラセットに従ってunescapeする|
|character_set_database	  |DBのdefaultキャラセット。"LOAD DATA INFILE"文はこの指定に従う|
|character_set_filesystem	|ファイルシステムの文字コード|
|character_set_results	  |サーバー => クライアントに結果を送信するときに使われるキャラセット|
|character_set_server	    |サーバーのdefaultキャラセット|
|character_set_system	    |ファイル名をこのキャラセットで扱う。utf8固定|
|character_sets_dir	      |キャラセットファイルの置いてあるディレクトリ|


参考: [MySQL/MariaDB　文字コードの設定 - takafumi blog](http://takafumi-s.hatenablog.com/entry/2015/04/03/010720)


## 設定

一般的には、`/etc/my.cnf`に`/etc/my.cnf.d`ディレクトリにある設定ファイルを読み込む設定を書いておき、詳細設定は、`/etc/my.cnf.d`の各設定ファイルに書く。今回、自分の設定ファイルを確認すると、`/etc/my.cnf`に`my.cnf.d`ディレクトリを読み込む設定がされていなかったため、追加した。

### /etc/my.cnf

```diff
[mysqld]
datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock
user=mysql
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
port=3306

[mysqld_safe]
log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

+!includedir /etc/my.cnf.d
```

### /etc/my.cnf.d/server.cnf

続いて、`/etc/my.cnf.d/server.cnf`に文字コードの設定を追記した。

```
sudo vim /etc/my.cnf.d/server.cnf
```

```diff
# this is read by the standalone daemon and embedded servers
[server]

# this is only for the mysqld standalone daemon
[mysqld]
+character-set-server=utf8 #added

[galera]

[embedded]

[mariadb]
```


MariaDBを再起動し、設定を反映させる。
```
sudo /etc/init.d/mysql restart
```


## utf-8

```
MariaDB [(none)]> show variables like 'char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | utf8                       |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | utf8                       |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
```

これで新規作成されるデータベース、テーブルの文字コードは、utf8になった。


## 参考

- [MariaDBの日本語の文字化けを解消する - Qiita](http://qiita.com/aiiro/items/1c160f5cb70c0850e8ce)
- [MySQL/MariaDB　文字コードの設定 - takafumi blog](http://takafumi-s.hatenablog.com/entry/2015/04/03/010720)


{{% amazon_ 4774164100 %}}
{{% amazon_ 4774170208 %}}