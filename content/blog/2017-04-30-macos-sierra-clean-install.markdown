---
title: "macOS sierraクリーンインストール時に行ったこと"
date: 2017-04-30T18:10:38+09:00
lastmod: 2017-04-30T18:10:38+09:00
comments: true
category: ['Tech']
tags: ['Mac','macOS']
published: true
slug: macos-sierra-clean-install
img: /images/2017/06/macOS-64x.png
---

![](/images/2017/06/macOS.png)


macOS sierraをクリーンインストールして、開発環境を整えたのでそのときのメモです。


<!--more-->
{{% googleadsense %}}


## Karabiner-Elements

下記URLを参考にインストールしました。

[macOS Sierra で Karabiner-Elements を使って左右の Commandキーで「英数 / かな」の切り替えを行う方法](https://beadored.com/macos-sierra-karabiner-elements-switching-eisuu-kana/)

```json
{
    "global": {
        "check_for_updates_on_startup": true,
        "show_in_menu_bar": true,
        "show_profile_name_in_menu_bar": false
    },
    "profiles": [
        {
            "devices": [
                {
                    "disable_built_in_keyboard_if_exists": false,
                    "identifiers": {
                        "is_keyboard": true,
                        "is_pointing_device": false,
                        "product_id": 657,
                        "vendor_id": 1452
                    },
                    "ignore": false
                }
            ],
            "fn_function_keys": {
                "f1": "display_brightness_decrement",
                "f10": "mute",
                "f11": "volume_decrement",
                "f12": "volume_increment",
                "f2": "display_brightness_increment",
                "f3": "mission_control",
                "f4": "launchpad",
                "f5": "illumination_decrement",
                "f6": "illumination_increment",
                "f7": "rewind",
                "f8": "play_or_pause",
                "f9": "fastforward"
            },
            "name": "Default profile",
            "one_to_many_mappings": {},
            "selected": true,
            "simple_modifications": {
                "caps_lock": "left_control",
                "left_command": "left_command",
                "left_control": "caps_lock",
                "right_command": "right_command"
            },
            "standalone_keys": {
                "left_command": "japanese_eisuu",
                "right_command": "japanese_kana"
            },
            "virtual_hid_keyboard": {
                "caps_lock_delay_milliseconds": 0,
                "keyboard_type": "ansi",
                "standalone_keys_delay_milliseconds": 200
            }
        }
    ]
}
```

## 開発環境構築

http://dev.classmethod.jp/server-side/ansible/automate-build-mac-osx-env-by-ansible/
http://t-wada.hatenablog.jp/entry/mac-provisioning-by-ansible

- Xcode
- Homebrewはshell scriptから実行
- Homebrewで入るものは、アプリケーションもcaskで入れた　ansible

https://github.com/twada/macbook-provisioning/blob/master/localhost.yml
http://qiita.com/itkr/items/82ddb1902b0051940526
https://github.com/ttskch/ansible-mac/blob/master/localhost.yml
https://github.com/knakayama/mac-os-x-setup
https://github.com/AkkeyLab/mac-auto-setup




[テキスト処理のための標準的なコマンド群の OS X への導入手順](http://qiita.com/eumesy/items/3bb39fc783c8d4863c5f)


## zsh環境を整える

### zplug

- [zplug/zplug: A next\-generation plugin manager for zsh](https://github.com/zplug/zplug)
- [おい、Antigen もいいけど zplug 使えよ \- Qiita](http://qiita.com/b4b4r07/items/cd326cd31e01955b788b)

`https://zplug.sh`のサイトがそもそも落ちてるので、下記のコマンドを実行した

```
$ export ZPLUG_HOME=~/.zplug
$ git clone https://github.com/zplug/zplug $ZPLUG_HOME
```


[新しいMBP買ったしoh\-my\-zshからzplugに乗り換えた話 \- Qiita](http://qiita.com/Iwark/items/f6ba765473dae03827e6)


### ghq + peco

個人の趣味ファイルもゴロゴロしてるので、`ghq`を利用して`src`で一括管理することにした。

[ghqを使ったローカルリポジトリの統一的・効率的な管理について \- Kentaro Kuribayashi's blog](http://blog.kentarok.org/entry/2014/06/03/135300)

http://webtech-walker.com/archive/2014/06/peco-ghq-gh-open.html

### iTerm2

[iTerm2の使い方まとめてみた \- uittie::blog](https://uittie.com/blog/2014/02/24/20140224iterm2%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%E3%81%BE%E3%81%A8%E3%82%81%E3%81%A6%E3%81%BF%E3%81%9F/)


## Atom

コマンドラインから実行できるように`Install Shell Commands`を実行する
[Install Shell Commands](http://qiita.com/kon_yu/items/56cc87be47022a31dda1)


## SSH鍵

鍵も作り直した。

```
$ ssh-keygen -t rsa -C "hoge@mail.com"
```

[SSH認証キーをBitbucket/GitHubに設定しよう！ \[Mac簡単手順\] \| 酒と涙とRubyとRailsと](http://morizyun.github.io/blog/ssh-key-bitbucket-github/)


## Dockerのpostgresに接続

```
docker exec -it kenchan2_db_1 psql -U postgres kenchan2_productio
```


## 参考
- [Macクリーンインストールからpython開発環境構築メモ【2017/4現在】 \- Qiita](http://qiita.com/sue_charo/items/2b0bca00ba2470965d1f)
- [Postgresqlのシーケンスを再設定する：地方で活動するweb制作者の日々を綴るblog](http://blog.livedoor.jp/loopus/archives/50846480.html)
