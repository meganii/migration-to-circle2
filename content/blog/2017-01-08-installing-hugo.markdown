---
title: "静的サイトジェネレータ「Hugo」インストール"
date: 2017-01-08T20:53:29+09:00
lastmod: 2017-01-08T20:53:29+09:00
comments: true
category: ['Tech']
tags: ['Hugo']
published: true
slug: installing-hugo
img: /images/hugo_s.png
---

静的ジェネレータ「Hugo」のインストール方法です。
MacでHomebrewを使っている方は、`brew update && brew install hugo`とすれば、すぐにインストールできます。

<!--more-->
{{% googleadsense %}}


## Macでのインストール方法

[Hugo \- Installing on a Mac](https://gohugo.io/tutorials/installing-on-mac/)

### brewのインストール

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

```
$ brew update
$ brew install hugo
```

## Windowsでのインストール方法

下記URLに従い、利用するWindows環境に合わせて32bit or 64bitをどちらをダウンロードします。
[Hugo \- Installing on Windows](https://gohugo.io/tutorials/installing-on-windows/)

https://github.com/spf13/hugo/releases
- https://github.com/spf13/hugo/releases/download/v0.18.1/hugo_0.18.1_Windows-32bit.zip  
- https://github.com/spf13/hugo/releases/download/v0.18.1/hugo_0.18.1_Windows-64bit.zip  

## 構築

以下のコマンドを実行すると、最低限のフォルダ構成が作成されます。

```
$ hugo new site myblog.com
$ tree
.
├── archetypes
├── config.toml
├── content
├── data
├── layouts
├── static
└── themes
```

`hugo server`とコマンドを実行すれば、直下の`config.toml`を読み込んでサイトのプレビューができるのですが、この最低限のフォルダ構成ではなにも表示されないので、まずはテーマをインストールします。


```
$ cd themes
$ git clone https://github.com/dim0627/hugo_theme_robust.git
```

ダウンロードしたthemeを利用するには、以下の通り`--theme`オプションで、インストールしたテーマを指定して`hugo server`を実行します。

```
hugo server --theme=hugo_theme_robust
```
