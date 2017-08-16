---
title: "Circle CIでHugoのビルド・デプロイを実行する"
date: 2016-08-15T15:53:59+09:00
comments: true
category: ['Tech']
tags: ['CircleCI','CI','Hugo']
published: true
slug: circle-ci-hugo-deploy
img: https://qiita-image-store.s3.amazonaws.com/0/10564/f19fddc1-3b74-2798-9e5a-fa4fa1ce03fb.png
---

![circleci.png](https://qiita-image-store.s3.amazonaws.com/0/10564/f19fddc1-3b74-2798-9e5a-fa4fa1ce03fb.png "circleci.png")



## この記事で書くこと

- Circle CIの設定
- Circle CIからさくらVPS(CentOS 6.4)へのrsyncでハマったこと
- circle.ymlのRuby, Pythonの設定


## 実現したいこと

Githubのリポジトリに、git pushした後、以下の作業をCIで実現したい。

- (事前準備) TF-TDFに食わせるためのファイル生成
- TF-IDFで関連記事生成
- Hugo build
- さくらVPSにrsync
- 関連記事生成で変更分をgithubにコミット


## 目的

Hugo単体でbuild -> さくらVPSへ転送まではローカルで完結するため、あまりCIとかは必要ないと思っていた。しかし、[PythonでTF\-IDFによる文書推薦 \- SIS Lab](https://meganii.com/blog/2016/08/13/tf-idf-recommendation/)で、TF-IDFによる関連記事生成のタスクを追加したことで、若干buildまでの時間が掛かるようになった。

そこで、githubにpushしたら、関連記事の生成からHugoビルド・デブロイまでCIで面倒を見てもらうようにしたい。

また、githubで管理することで履歴が分かるようになること、ブラウザベースで記事を修正することができるようになることも狙いの一つ。

{{% googleadsense %}}


## Circle CIとは

[CircleCI](https://circleci.com/)

自分のCircle CIの認識は、継続的インテグレーション(CI)を実現するためのSaaS型のWebサービスです。同様のCIサービスには、TravisCIや、Weckerがあります。各サービスごとに、細かい違いはあるようですが、そのなかでも人気がありそうなCircle CIを選びました。

## How どうやって実現するか

1. Circle CIからGithubを連携させる
2. circle.ymlに処理を記述する
3. 対象リポジトリにgit pushする

実際の設定自体は単純で、circle.ymlというCircle CI用の設定ファイルを作ってあげるだけで、Circle CIが動き出す。

## ハマった点

- Circle CIからさくらVPSへのrsync
- githubへのコミット権限は、ユーザ定義を指定しなければならない


### Circle CIからさくらVPSへのrsync

Circle CIで毎回生成されるコンテナ(Ubuntu)からブログ記事をホストしているさくらVPSへのrsyncを行うために、SSHの鍵を登録する必要がある。

#### 1.さくらVPSで鍵を生成する

```
$ ssh-keygen -t rsa # 生成の際にパスワードは設定しない
```

#### 2. 公開鍵をauthorized_keysに登録する

```
$ cat id_rsa.pub >> authorized_keys
```

#### 3. CircleCIのプロジェクト設定のSSH Permissionsから秘密鍵を登録

「1.さくらVPSで鍵を生成する」で生成した秘密鍵 id_rsa をコピーして、Circle CIの「SSH Permissions」から登録します。

![circleci.png](https://farm8.staticflickr.com/7648/28936345722_c7fc15ee85_z.jpg "circleci.png")


#### 4. Circle CIのDebug Via SSHからSSHログインしてCircle CI側からさくらのレンタルサーバー側にログイン確認

```
$ ssh -p port番号 さくらVPSのユーザ名@さくらVPSのIPアドレス
```

[CircleCI側のSSHキーをさくらのレンタルサーバー側に登録する \- Qiita](http://qiita.com/ANTON072/items/fbcbca9fa440b391044b)


### githubへのコミット権限は、ユーザ定義を指定しなければならない

「Checkout SSH keys」で最初に作られている`deploy key`だとgithubにコミットができませんでした。

githubにコミットするためには、`user key`を利用する必要がありました。


### 環境変数の設定方法

直接コードに埋め込みたくない値などは、Circle CIでも環境変数として定義することができる。

![Environment_Variables_-_CircleCI.jpg](https://qiita-image-store.s3.amazonaws.com/0/10564/5ef1449c-1b31-64cc-bc5e-0ebc1609c91b.jpeg "Environment_Variables_-_CircleCI.jpg")

ここでは、さくらVPSのIPアドレス、ポート番号を環境変数として定義している。


### Rake -qによるサイレント実行

せっかくあまり見せたくない変数をCircle CIの環境変数として定義したにも関わらず、Rakeの実行ログがCircle CIのビルド結果に残ってしまうのはあんまり意味がありません。

Rakeのオプションに -q, --quietがあったのでこのオプションを付けて実行します。

```
-q, --quiet   Do not log messages to standard output.
```



### Mecabインストール

mecabインストールで参考にしたcircleci
https://circleci.com/gh/bungoume/mecab-web-api/76#config


## 今後対応したいこと

- TF-TDFのパラメータ調整
- Textlintによる文章校正
- Github Flowによる電子書籍作成
- Circle CIの定期実行


{{% affiliate title="改訂新版Jenkins実践入門 ――ビルド・テスト・デプロイを自動化する技術 (WEB+DB PRESS plus)" amazonUrl="http://www.amazon.co.jp/exec/obidos/ASIN/4774174238/meganii-22/ref=nosim/" img="https://images-fe.ssl-images-amazon.com/images/I/512-dGvAcJL._SL160_.jpg" amazondetailUrl="" rakutenUrl="http://hb.afl.rakuten.co.jp/hgc/0f1c1106.d5997202.117c2ed9.4ab7d4d2/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2F%25E7%25B6%2599%25E7%25B6%259A%25E7%259A%2584%25E3%2582%25A4%25E3%2583%25B3%25E3%2583%2586%25E3%2582%25B0%25E3%2583%25AC%25E3%2583%25BC%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%25B3%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" %}}
