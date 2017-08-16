---
title: Jekyllのバージョンアップ
date: 2013-11-24T21:34:00+09:00
category: ['Tech']
tags: ['jekyll']
published: true
slug: jekyll-versionup
---

Jekyllのバージョンがいつの間にか1.3になっているので、バージョンアップする。


{{% googleadsense %}}

```
brew update
```

Xcodeが古くなっているので、AppStoreから最新をダウンロード

```
rbenv install 2.0.0-p195
```

```
brew update  # Homebrew自体とfomulaを最新にする
brew upgrade # 更新のあるパッケージを再ビルド
brew doctor
```

設定が間違っていたので、修正
export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

[Configuring Mac OS X Mountain Lion 10.8 | Hacker Codex](http://hackercodex.com/guide/mac-osx-mountain-lion-10.8-configuration/)

## rbenvによるバージョン切り替え
### global 通常使用するバージョンの指定
rbenv global 2.0.0-p353

### local プロジェクト毎(特定のディレクトリ以下)で使用するバージョンの指定
rbenv local 2.0.0-p353

### shell そのシェル内でのみ使用するバージョンの指定
rbenv shell 2.0.0-p353
