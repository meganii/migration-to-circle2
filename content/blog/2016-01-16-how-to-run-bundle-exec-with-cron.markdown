---
title: "Capyabara + PhantomJS(poltergeist)のRubyスクリプトをcronで流したい"
date: 2016-01-16T22:34:08+09:00
comments: true
category: ['Tech']
tags: ['cron']
published: true
slug: how-to-run-bundle-exec-with-cron
---

Capyabara + PhantomJS(poltergeist)のRubyスクリプトをcronで流したいと思った時のお話。
シェルにログインして実行すると、上手く動作するのに、cronからは動かない。

結論から言うと、自分の環境では、

- `.bash_profile`にphantomjsのPATHを明記($HOME/pahtomjs/bin直下にバイナリ生成済み)する
- `bash -lc` でログインして、実行するdirectoryまで行き、実行する

ことで、cronで実行できた。cronの使い方も分からないが、PATH関係も疎いので

{{% googleadsense %}}


## 最終形


```
# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

export PATH="$PATH:$HOME/bin"

export PATH="$HOME/phantomjs/bin:$PATH"
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
```

```
00 06 * * * /bin/bash -lc 'cd /home/app/appname/current/; bundle exec ruby script.rb 1>> /home/app/appname/current/script.log 2>> /home/app/appname/current/error.log'
```


## 参考

- [cronでrbenvのrubyを使う３つの方法 - sonots:blog](http://blog.livedoor.jp/sonots/archives/33204053.html)
- [cron力をつけよう！全てのcrontab入門者に贈る9個のテクニック · DQNEO起業日記](http://dqn.sakusakutto.jp/2012/06/cron_crontab9.html)
- [-e オプションは、環境変数 VISUAL もしくは EDITOR で指定されているエディターを使って、現在の crontab を編集するのに使われる。編集終了後、 変 更された crontab は自動的にインストールされる。  ](http://www.server-memo.net/tips/crontab.html)
