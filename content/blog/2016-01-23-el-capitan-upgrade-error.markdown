---
title: "El Capitanへのアップグレード時AppStoreに接続できなくなった場合(さらにキーチェーンアクセスでも対処できなかった時)の対処法
"
date: 2016-01-23T20:51:43+09:00
comments: true
category: ['Tech']
tags: ['Mac']
published: true
slug: el-capitan-upgrade-error
---

今朝、El Capitanのアップグレードしたのだが、いつものごとくエラーが出たので対処方法をまとめておく。

## 起きた現象

- App Storeにアクセスできない
- 通信が遅い

App Storeから気軽にアップデートを行い、意外とすんなりいけたかと思ったがやはり問題が生じた。調べてみると、SSL証明書が壊れるケースがあり、今回もそれに該当した。

解決方法としては、「Keychan Access.app」で、VeriSign関連の証明書を削除すればよいらしいのだが、自分の環境の場合、GUIから対象の証明書を選択しただけで、アプリが落ちてしまい対処できなかった。

※以下の証明書を選択するとアプリが固まってしまった。

```
VeriSign Class 3 Public Primary Certification Authority - G3
VeriSign Class 3 Public Primary Certification Authority - G5
```

大概のことは、ターミナル(terminal)からできるだろうと思い調べたら対処方法があったので共有したい。


{{% googleadsense %}}

## 対処方法

### 1. 該当証明書の存在確認

下記コマンドで、VeriSignの証明書を検索する。

```
security find-certificate -c "VeriSigh" -Z -a
```

### 2. SHA-1値取得

「1. 該当証明書の存在確認」で、削除したいリストが出ていることを確かめた上で以下のコマンドを実行して、一意となるSHA-1値を取得する。

```
security find-certificate -c "VeriSigh" -Z -a | grep SHA-1
```

### 3. 削除

以下のコマンドを実行し、取得したSHA-1の値を指定して削除する。

```
sudo security delete-certificate -Z {取得したSHA-1の値} /Users/meganii/Library/Keychains/login.keychain
```

※ `/Users/meganii/Library/Keychains/login.keychain`の部分は、`security list-keychains`で取得できるlogin.keychainの値

### 4. 再起動

最後は、再起動すれば、App Storeにも接続することができた。



## 後は、毎度おなじみ Homebrew 周り

```
brew doctor
Please note that these warnings are just used to help the Homebrew maintainers
with debugging if you file an issue. If everything you use Homebrew for is
working fine: please don't worry and just ignore them. Thanks!

Warning: The /usr/local is not writable.

You should probably change the ownership and permissions of /usr/local
back to your user account.
  sudo chown -R $(whoami) /usr/local

Warning: Some directories in /usr/local/share/man aren't writable.
This can happen if you "sudo make install" software that isn't managed
by Homebrew. If a brew tries to add locale information to one of these
directories, then the install will fail during the link step.

You should probably `sudo chown -R $(whoami)` them:
    /usr/local/share/man/mann

Warning: The /usr/local directory is not writable.
Even if this directory was writable when you installed Homebrew, other
software may change permissions on this directory. For example, upgrading
to OS X El Capitan has been known to do this. Some versions of the
"InstantOn" component of Airfoil or running Cocktail cleanup/optimizations
are known to do this as well.

You should probably change the ownership and permissions of /usr/local
back to your user account.
  sudo chown -R $(whoami):admin /usr/local

Warning: Unbrewed dylibs were found in /usr/local/lib.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected dylibs:
    /usr/local/lib/libnghttp2.14.dylib
    /usr/local/lib/libtcl8.6.dylib
    /usr/local/lib/libtk8.6.dylib

Warning: Unbrewed header files were found in /usr/local/include.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected header files:
    /usr/local/include/fakemysql.h
    /usr/local/include/fakepq.h
    /usr/local/include/fakesql.h
    /usr/local/include/itcl.h
    /usr/local/include/itcl2TclOO.h
    /usr/local/include/itclDecls.h
    /usr/local/include/itclInt.h
    /usr/local/include/itclIntDecls.h
    /usr/local/include/itclMigrate2TclCore.h
    /usr/local/include/itclTclIntStubsFcn.h
    /usr/local/include/mysqlStubs.h
    /usr/local/include/nghttp2/nghttp2.h
    /usr/local/include/nghttp2/nghttp2ver.h
    /usr/local/include/odbcStubs.h
    /usr/local/include/pqStubs.h
    /usr/local/include/tcl.h
    /usr/local/include/tclDecls.h
    /usr/local/include/tclOO.h
    /usr/local/include/tclOODecls.h
    /usr/local/include/tclPlatDecls.h
    /usr/local/include/tclThread.h
    /usr/local/include/tclTomMath.h
    /usr/local/include/tclTomMathDecls.h
    /usr/local/include/tdbc.h
    /usr/local/include/tdbcDecls.h
    /usr/local/include/tdbcInt.h
    /usr/local/include/tk.h
    /usr/local/include/tkDecls.h
    /usr/local/include/tkPlatDecls.h

Warning: Unbrewed .la files were found in /usr/local/lib.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected .la files:
    /usr/local/lib/libnghttp2.la

Warning: Unbrewed .pc files were found in /usr/local/lib/pkgconfig.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected .pc files:
    /usr/local/lib/pkgconfig/libnghttp2.pc
    /usr/local/lib/pkgconfig/tcl.pc
    /usr/local/lib/pkgconfig/tk.pc

Warning: Unbrewed static libraries were found in /usr/local/lib.
If you didn't put them there on purpose they could cause problems when
building Homebrew formulae, and may need to be deleted.

Unexpected static libraries:
    /usr/local/lib/libnghttp2.a
    /usr/local/lib/libtclstub8.6.a
    /usr/local/lib/libtkstub8.6.a

Warning: Your Xcode (6.4) is outdated
Please update to Xcode 7.2.
Xcode can be updated from the App Store.
```


### 対応

- 以下のコマンドを実行

```
sudo chown -R $(whoami) /usr/local
/usr/local/share/man/mann
```

- XCodeのバージョンアップ


## 参考

- [El CapitanのSSL問題、Keychainもフリーズする場合の対処法 | 踊る犬.net](http://blog.odoruinu.net/2016/01/14/how-to-solve-el-capitan-ssl-problem-with-freezing-keychain/)
