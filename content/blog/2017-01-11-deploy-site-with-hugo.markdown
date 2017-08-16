---
title: "静的サイトジェネレータ「Hugo」〜公開方法〜"
date: 2017-01-11T22:22:15+09:00
lastmod: 2017-01-11T22:22:15+09:00
comments: true
category: ['Tech']
tags: ['Hugo','deploy']
published: true
slug: deploy-site-with-hugo
img: /images/hugo_s.png
---

## 公開 Deploy

Hugoには、サイトを生成する仕組みはありますが公開する仕組みは持っていません。そのため、Hugoで生成した生成物(HTML+CSS)を何らかの方法で、Webサーバに持っていってあげなければいけません。

必要なのは、どこに公開するかと、どうやって公開するかです。

<!--more-->
{{% googleadsense %}}


## どこで公開するか

Hugoで生成したサイトをどこに公開するかは、いくつか選択肢があります。例えば、以下のようなものです。

- VPS(Virtual Private Server)
- レンタルサーバ(ロリポップ)
- Github Pages
- Amazon S3


私は、<a href="https://px.a8.net/svt/ejp?a8mat=2NDW0A+8S5702+D8Y+CATCY" target="_blank">さくらのVPS</a><img border="0" width="1" height="1" src="https://www13.a8.net/0.gif?a8mat=2NDW0A+8S5702+D8Y+CATCY" alt="">を契約しています。自分で色々といじれるので楽しいです。


## どうやって公開するか

やることは単純で、Hugoで生成したHTML+CSSを公開サーバにアップロードするだけのことです。とはいえ、毎回手動で配置するわけにはいかないため、スクリプトで自動化させます。

例えば、以下の方法です。

- FTP
- rsync
- git push

私は、以下のようにRakeタスクとして定義しています。

```
require "rubygems"
require "bundler/setup"
require "stringex"

posts_dir       = "content/blog/"    # directory for blog files
new_post_ext    = "markdown"  # default new post file extension when using the new_post task

desc "deploy_to_sakura"
task :deploy_to_sakura do
  sh 'rm -r public'
  sh 'hugo -t hugo-zen'
  sh 'mv public/category public/blog'
  sh 'mv public/tags public/blog'
  sh 'mv public/en/category public/en/blog'
  sh 'mv public/en/tags public/en/blog'
  sh "rsync --iconv=UTF-8-MAC,UTF-8 -e \"ssh -p #{ENV['SSH_PORT']}\" -avz --delete public/ web@#{ENV['SAKURA_IP']}:/home/web/www/meganii.com"
end
```
