---
title: "google-api-ruby-clientからGoogle Adsense Management APIを操作する方法"
date: 2016-06-05T09:58:34+09:00
comments: true
category: ['Tech']
tags: ['Google','Ruby', 'api']
published: true
slug: ruby-google-api-client
img: "https://c8.staticflickr.com/8/7305/27394115551_0612eb23fb_t.jpg"
---


## 何をしたいか？

- `google-api-ruby-client`を利用して、Google Adsenseの収益情報を取得したい

## 概要(何が書いてあるか)

- [https://github.com/google/google-api-ruby-client](https://github.com/google/google-api-ruby-client)のサンプルを参考に、プロジェクトの作成の仕方から、認証情報の作り方、Adsense用のコード


## どこにハマったか？

- `google-api-ruby-client`のversion 0.9以降の方法がなかなか見つからず試行錯誤した
- 特に、認証周りがよく分からず、苦労した

最終的には、googleのサンプルコードをベースに作成することでレポート取得ができることができた。


<!--more-->
{{% googleadsense %}}


## 手順

googleのサンプルをベースにAdsense用のコードを作成する。(「Adsense用コード」参照)
[https://github.com/google/google-api-ruby-client](https://github.com/google/google-api-ruby-client)


以下の手順で'google-api-samples'コマンドを実行する。

1. プロジェクトの作成
2. API Managerで利用したいAPI(ここではAdsense Management API)を有効化
3. 利用するAPIに応じた認証を作成
4. '.env'ファイルに「3.」で作成した認証情報を設定
5. google-api-samples コマンドを実行し認証


以下、README.md より抜粋。

>Depending on which particular samples you want to run, different
steps may be required. Some samples, like Pub/Sub, require a service account,
others like Drive, Calendar, and YouTube require an OAuth Client ID. And in
some cases like Translate, only an API key is needed.

>* Create a project at https://console.developers.google.com
* Go to the `API Manager` and enable the APIs you'd like to try
* Go to `Credentials` and create the appropriate type of credential for the sample
    * For keys, use 'Server key' as the type
    * For OAuth Client IDs, use 'Other' as the type
    * For service accounts, use the 'JSON' key type  


## 1. プロジェクトの作成

[https://console.developers.google.com](https://console.developers.google.com) からプロジェクトを作成する。

<p><a href="https://www.flickr.com/photos/35571855@N06/27189242280" title="1__Create_Projectby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7385/27189242280_b0ec5e22db_z.jpg" alt="1__Create_Project"></a></p>


<p><a href="https://www.flickr.com/photos/35571855@N06/27366603062" title="2__Input_Project_Nameby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7191/27366603062_9b6662f0c7_z.jpg" alt="2__Input_Project_Name"></a></p>


## 2. API Managerで利用したいAPI(ここではAdsense Management API)を有効化


<p><a href="https://www.flickr.com/photos/35571855@N06/27394115551" title="3__Complete_creating_project_and_Go_to_Adsenes_Management_APIby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7305/27394115551_0612eb23fb_z.jpg" alt="3__Complete_creating_project_and_Go_to_Adsenes_Management_API"></a></p>


<p><a href="https://www.flickr.com/photos/35571855@N06/27189242110" title="4__Enable_AdSense_Management_APIby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7325/27189242110_7d5f40f3fa_z.jpg" alt="4__Enable_AdSense_Management_API"></a></p>


## 3. 利用するAPIに応じた認証を作成

<p><a href="https://www.flickr.com/photos/35571855@N06/27189242330" title="5__Go_to_Credentials_pageby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7376/27189242330_102f846d72_z.jpg" alt="5__Go_to_Credentials_page"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/27189241950" title="6__Credentials_wizardby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7611/27189241950_b5766e0ff2_z.jpg" alt="6__Credentials_wizard"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/27189241850" title="7__Credentials_wizard_-_test-meganii-projectby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7437/27189241850_bc23e5d7d8_z.jpg" alt="7__Credentials_wizard_-_test-meganii-project"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/27189241810" title="8__Credentials_wizardby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7324/27189241810_9813ce7c15_z.jpg" alt="8__Credentials_wizard"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/27394115421" title="9__Credentials_wizardby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7613/27394115421_079882466f_z.jpg" alt="9__Credentials_wizard"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/27366602942" title="10__Credentials_wizardby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7743/27366602942_a666affcbd_z.jpg" alt="10__Credentials_wizard"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/27189241920" title="11__Credentialsby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7664/27189241920_4c7713f2c1_z.jpg" alt="11__Credentials"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/27189241770" title="12__OAuth_clientby meganii, on Flickr"><img class="img-responsive" src="https://farm8.staticflickr.com/7505/27189241770_dde3819202_z.jpg" alt="12__OAuth_client"></a></p>


## 4. '.env'ファイルに「3.」で作成した認証情報を設定

'dotenv'は、プロジェクト直下の`.env`を環境変数としてロードする。
先ほど、作成した認証情報の`Client ID`と`Client sercret`を書く。

```.env
GOOGLE_CLIENT_ID=CLIENT_ID
GOOGLE_CLIENT_SECRET=CLIENT_SECRET
GOOGLE_APPLICATION_CREDENTIALS=hogehoge.json
GOOGLE_CREDENTIAL_STORE=credentials.yaml
```

## 5. 5. google-api-samples コマンドを実行し認証

google-api-samples コマンドを実行して出力されたURLにアクセスして、認証を行う。




## Adsense用コード

Google Analyticsのサンプルコードを参考に、Adsense用のプログラムを作成した。

```
# This software includes the work that is distributed in the Apache License 2.0

require 'google/apis/adsense_v1_4'
require 'base_cli'


module Samples
  class Adsense < BaseCli

    Adsense = Google::Apis::AdsenseV1_4

    desc 'show_report ACCOUNT_ID', 'Show report for the given adsense account ID'
    method_option :start, type: :string, required: true
    method_option :end, type: :string, required: true
    def show_report(account_id)
      adsense = Adsense::AdSenseService.new
      adsense.authorization = user_credentials_for(Adsense::AUTH_ADSENSE)

      result = adsense.generate_account_report(account_id,
                                                options[:start],
                                                options[:end],
                                                :metric => 'EARNINGS')
      puts result
    end
  end
end
```


## 参考

### dotenv

環境変数を読み込ませる。

- [bkeepers/dotenv: Loads environment variables from `.env`.](https://github.com/bkeepers/dotenv)
- [Dotenv使ってみた - Qiita](http://qiita.com/ogawatti/items/e1e612b793a3d51978cc)

### thor

コマンドラインインターフェース(CLI)のツールキット

- [erikhuda/thor: Thor is a toolkit for building powerful command-line interfaces.](https://github.com/erikhuda/thor)
- [Ruby の CLI ツールの作成を支援する、 thor gem の基本について。 #thor #ruby](http://qiita.com/tbpgr/items/10a5c236cfb528c76ef5)


## Next Action

- OAuthの認証周りの考え方がいまいち完全に理解していないため、まとめる。
- ダッシュボード化を検討していて、以下のサンプルが面白そう [ButecoOpenSource/dashboard: Status Dashboard](https://github.com/ButecoOpenSource/dashboard)
