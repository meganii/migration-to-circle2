---
title: "CircleCIでMeCabを利用してHugoビルドする"
date: 2017-01-14T23:02:29+09:00
lastmod: 2017-01-14T23:02:29+09:00
comments: true
category: ['Tech']
tags: ['Hugo']
published: true
slug: circle-ci-settings-for-mecab-hugo
img: /images/hugo_s.png
---

Circle CIで、PythonからMeCab、sklearnを利用して関連記事を作成し、Hugoでビルド＆さくらVPSでブログを公開するためのコンテナの設定がやっと落ち着いたので備忘録として残しておきます。

<!--more-->
{{% googleadsense %}}

## circle.yml

現在の`circle.yml`です。以下のモジュールをインストールして、コンテナの準備、Hugoでビルド、さくらVPSへの公開を行なっています。

- MeCab
- Python
- Hugo


```
machine:
  timezone: Asia/Tokyo
  ruby:
    version: 2.2.4
  python:
    version: 3.5.1

dependencies:
  cache_directories:
    - mecab-0.996
    - mecab-ipadic-2.7.0-20070801
  pre:
    - git config --global user.name "meganii"
    - git config --global user.email "email@hogehoge.com"
    - >
      HUGO_VERSION=0.18.1 &&
      set -x &&
      set -e &&
      if [ ! -e $CIRCLE_BUILD_DIR/bin/hugo ] || ![[ `hugo version` =~ v${HUGO_VERSION} ]]; then
        wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz &&
        tar xvzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz &&
        sudo cp hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64 $CIRCLE_BUILD_DIR/bin/hugo;
      fi
    - sudo apt-get update -qq
    - sudo apt-get install -qq python3-dev
    - >
      if [[ ! -e mecab-0.996/src/mecab ]]; then
        wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE" &&
        tar xvzf mecab-0.996.tar.gz &&
        cd mecab-0.996 &&
        ./configure --enable-utf8-only &&
        make
      fi
    - >
      cd mecab-0.996 &&
      sudo make install &&
      sudo ldconfig
    - >
      if [[ ! -e mecab-ipadic-2.7.0-20070801/sys.dic ]]; then
        wget -O mecab-ipadic-2.7.0-20070801.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM" &&
        tar xvzf mecab-ipadic-2.7.0-20070801.tar.gz &&
        cd mecab-ipadic-2.7.0-20070801 &&
        ./configure --with-charset=utf8 &&
        make
      fi
    - >
      cd mecab-ipadic-2.7.0-20070801 &&
      sudo make install
    - pip install --upgrade pip
    - pip install -r requirements.txt

test:
  override:
    - python -V
    - hugo version

deployment:
  master:
    branch: master
    commands:
      - rake create_relatedposts
      - rake -q deploy_to_sakura_from_circleci
      - pwd
      - git add data/* tmp/* && git commit -m "[ci skip] publish"; if [ $? -eq 0 ]; then git push origin master; else :; fi
```

## Hugoインストールの修正

元々はHugoのインストールを以下の通り、都度最新版をダウンロードしていたのですが、Hugoの開発が行われる度、ビルドに失敗するため、バージョン固定としました。

### 変更前

```
- go get -u -v github.com/kardianos/govendor
- go get -u -v github.com/spf13/hugo
- cd /home/ubuntu/.go_workspace/src/github.com/spf13/hugo && govendor sync && go install
```

### 変更後(バイナリをダウンロード)

```
- >
 HUGO_VERSION=0.18.1 &&
 set -x &&
 set -e &&
 if [ ! -e $CIRCLE_BUILD_DIR/bin/hugo ] || ![[ `hugo version` =~ v${HUGO_VERSION} ]]; then
   wget https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz &&
   tar xvzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz &&
   sudo cp hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64 $CIRCLE_BUILD_DIR/bin/hugo;
 fi
```
