---
title: "Capistrano3でRails5+Unicornのアプリをデプロイしたときに環境変数SECRET_KEY_BASEが読み込まれない"
date: 2016-11-23T19:50:01+09:00
lastmod: 2016-11-23T19:50:01+09:00
comments: true
category: ['Tech']
tags: ['Rails','Capistrano3']
published: true
slug: capistrano3-can-not-read-env
---

## 現象

Capistrano3を利用して、Rails5のアプリをデプロイしたときに、`SECRET_KEY_BASE`が指定されていないという以下のエラーメッセージが表示される。

```
Missing `secret_token` and `secret_key_base` for 'production' environment, set these values in `config/secrets.yml`
```


## 前提

- Rails 5.0.0.1
- Capistrano Version: 3.6.1 (Rake Version: 11.3.0)
- ruby 2.3.1p112 (2016-04-26 revision 54768) [x86_64-darwin15]
- unicorn v5.2.0

<!--more-->
{{% googleadsense %}}


## 解決策

Capistrano3は、`.bash_profile`ではなく`.bashrc`を読み込むため、いくら`.bash_profile`に`export SECRET_KEY_BASE=hogehoge`と書いても読み込んでもらえなかった。

`.bashrc`に`export SECRET_KEY_BASE=hogehoge`と記載することで、上手く読み込まれた。

`SECRET_KEY_BASE`に定義する値は、`bundle exec rake secret`で生成するのが流儀のようです。


## そもそも SECRET_KEY_BASEって何？

>However, since Rails 4, the default store is EncryptedCookieStore. With EncryptedCookieStore the session is encrypted before being stored in a cookie. This prevents the user from accessing and tampering the content of the cookie. Thus the session becomes a more secure place to store data. The encryption is done using a server-side secret key secrets.secret_key_base stored in config/secrets.yml .  
http://guides.rubyonrails.org/security.html

railsガイドを読んだところ以下の理解です。

- セッションハイジャックを防ぐため、`EncryptedCookieStore`では、セッションは暗号化されてからクッキーに格納される
- この暗号化を行う際の秘密鍵が、`SECRET_KEY_BASE`
- 秘密鍵`SECRET_KEY_BASE`による暗号化を行っているため、この`SECRET_KEY_BASE`が盗まれると復号化されてしまう

[Ruby on Rails Security Guide — Ruby on Rails Guides](http://guides.rubyonrails.org/security.html)

[secret\_key\_baseとは \- DesignAssembler](http://hyottokoaloha.hatenablog.com/entry/2016/02/17/215910)



## 参考
[Capistrano で\.bash\_profileに書いてある環境変数が読まれない件 \- Qiita](http://qiita.com/AknEp/items/6e47ee6c363ed1ba9c68)

[secret\_key\_baseあたりのメモ \- Qiita](http://qiita.com/kanpe777/items/cb11dc88ced544d10bd5)
