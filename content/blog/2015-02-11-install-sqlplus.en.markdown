---
title: "How to install SQL*Plus in MacOSX Marverics"
date: 2015-02-11T22:54:00+09:00
lastmod: 2017-01-02T08:19:00+09:00
comments: true
category: ['Tech']
tags: ['Oracle', 'sqlplus']
published: true
slug: how-to-install-sqlplus-in-macosx
---

## What is this article

This article explain how to install SQL*Plus after installing Oracle Express Edition 11g.

[How to install Oracle Database Express Edition11g on Vagrant CentOS6.4](https://meganii.com/en/blog/2015/02/08/oracle-express-edition-11g-install/)


{{% googleadsense %}}


## How to install

1. Download files blow url

[http://www.oracle.com/technetwork/topics/intel-macsoft-096467.html)](http://www.oracle.com/technetwork/topics/intel-macsoft-096467.html)

- instantclient-basic-macos.x64-11.2.0.4.0.zip
- instantclient-jdbc-macos.x64-11.2.0.4.0.zip
- instantclient-sqlplus-macos.x64-11.2.0.4.0.zip
- instantclient-sdk-macos.x64-11.2.0.4.0.zip


2. Expand zip files

```
mkdir ~/bin/sqlplus
```

```
unzip instantclient-basic-macos.x32-11.2.0.4.0.zip -d ~/bin/sqlplus/
unzip instantclient-jdbc-macos.x32-11.2.0.4.0.zip -d ~/bin/sqlplus/
unzip instantclient-sdk-macos.x32-11.2.0.4.0.zip -d ~/bin/sqlplus/
unzip instantclient-sqlplus-macos.x32-11.2.0.4.0.zip -d ~/bin/sqlplus/
```

3. Setting Path

```
vim ~/.bash_profile

## oracle client
export ORACLE_HOME=~/bin/sqlplus/instantclient_11_2
export PATH=$ORACLE_HOME:$PATH
export DYLD_LIBRARY_PATH=~/bin/sqlplus/instantclient_11_2
export NLS_LANG=American_America.AL32UTF8

```

```
source ~/.bash_profile
```

4. Installing rlwrap

You can't display command history default. `rlwrap` is able to remember command histories and display them. You can install by `brew` command.

If you would like to show histories, you type `rlwrap sqlplus`.

```
meganii-air:oracle meganii$ brew install rlwrap
==> Installing rlwrap dependency: readline
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/readline-6.3.8.mavericks.bottle.tar.
######################################################################## 100.0%
==> Pouring readline-6.3.8.mavericks.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local.

Mac OS X provides similar software, and installing this software in
parallel can cause all kinds of trouble.

OS X provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only.

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/readline/lib
    CPPFLAGS: -I/usr/local/opt/readline/include

==> Summary
🍺  /usr/local/Cellar/readline/6.3.8: 40 files, 2.1M
==> Installing rlwrap
==> Downloading https://downloads.sf.net/project/machomebrew/Bottles/rlwrap-0.42.mavericks.bottle.tar.gz
######################################################################## 100.0%
==> Pouring rlwrap-0.42.mavericks.bottle.tar.gz
🍺  /usr/local/Cellar/rlwrap/0.42: 29 files, 312K
```


## Reference

[Mac OSXに64ビット版sqlplus(11.2)をインストールしてAmazon RDS for Oracleに接続 - yoshidashingo](http://yoshidashingo.hatenablog.com/entry/2014/08/08/165311)
