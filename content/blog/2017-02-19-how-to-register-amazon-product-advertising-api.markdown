---
title: "Amazon Product Advertising APIを利用するためのIAMユーザ登録とアクセスキーの発行"
date: 2017-02-19T11:06:41+09:00
lastmod: 2017-02-19T11:06:41+09:00
comments: true
category: ['Tech']
tags: ['API','Amazon']
published: true
slug: how-to-register-amazon-product-advertising-api
img: https://i.gyazo.com/thumb/200/_96237a7bdceefabf3b4786753bb83897-png.jpg
---

プログラムからAmazon Product Advertising APIを利用するためには、Amazon Web Servicesからアクセスキーを発行する必要があります。

GitHubにAWSアクセスキーを誤ってCommitしてしまったため、アクセスキーを再取得したのでそのときの備忘録を載せておきます。


<!--more-->
{{% googleadsense %}}


### 前提

AWSアカウントは作成済みであること。

まだAWSアカウントを持っていない方は、下記リンクを参照してアカウントを作成してください。

[AWS アカウント作成の流れとポイント \| AWS](https://aws.amazon.com/jp/register-flow/)


## IAMユーザ作成
### ユーザ作成

[![https://gyazo.com/f9c6143ff7f49a37b25bcd50ef35ca35](https://i.gyazo.com/f9c6143ff7f49a37b25bcd50ef35ca35.png)](https://gyazo.com/f9c6143ff7f49a37b25bcd50ef35ca35)

### ポリシー設定

Amazon Product Advertising APIを利用するには、`AdministratorAccess`の権限が必要です。「既存のポリシーを直接」

[![https://gyazo.com/d7a4ae00aff0a764d5f402bdae6be893](https://i.gyazo.com/d7a4ae00aff0a764d5f402bdae6be893.png)](https://gyazo.com/d7a4ae00aff0a764d5f402bdae6be893)

### 確認

[![https://gyazo.com/473cae8c0a0e6b08af3b2dd1febe5c29](https://i.gyazo.com/473cae8c0a0e6b08af3b2dd1febe5c29.png)](https://gyazo.com/473cae8c0a0e6b08af3b2dd1febe5c29)

### 完了

[![https://gyazo.com/3e08edfe9d0237cf9c092c6668654bfa](https://i.gyazo.com/3e08edfe9d0237cf9c092c6668654bfa.png)](https://gyazo.com/3e08edfe9d0237cf9c092c6668654bfa)

## アクセスキー発行
### アクセスキーの作成

[![https://gyazo.com/62b6cb38210f24ce354f575d912921f2](https://i.gyazo.com/62b6cb38210f24ce354f575d912921f2.png)](https://gyazo.com/62b6cb38210f24ce354f575d912921f2)

[![https://gyazo.com/36e7fc358a0915548036d94836c43b78](https://i.gyazo.com/36e7fc358a0915548036d94836c43b78.png)](https://gyazo.com/36e7fc358a0915548036d94836c43b78)


上記手順で取得した`アクセスキーID`と`シークレットアクセスキー`を利用して、Amazon Product Advertising APIを利用します。


{{% amazon_ 4774176737 %}}