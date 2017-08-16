---

title: "Hugoで人気記事を表示するためJSONを返すAPIサーバを作りData-driven Contentを試してみた"
date: 2016-09-06T07:21:53+09:00
comments: true
category: ['Tech']
tags: ['Python','Hugo']
published: true
slug: hugo-data-driven-content-for-polupar-posts
img: '/images/hugo_s.png'

---

Hugo Data-Driven Contentを試してみる。


## 目的

- サイドバーの人気記事をJavascriptを利用せずに、表示できるようにしたい。
- 脱サードパーティアプリ。

<!--more-->
{{% googleadsense %}}


## 対応方法

1. Hugo Data Files を利用する
2. Hugo Data-driven content を利用する

1つ目のData Filesは、関連記事表示の際に利用した([PythonでTF\-IDFによる文書推薦 \- SIS Lab](https://meganii.com/blog/2016/08/13/tf-idf-recommendation/))ので、今度は2つのHugo Data-driven Contentを試してみる。

実装方法は、以下の通り。

Google Analyticsから情報を取得し、その結果を加工してJSONを返すAPIサーバを作る。

その後、HugoのData-driven contentの機能を利用して、APIを叩いてJSONを取得し、表示させる。


## JSONを返すAPIサーバを立てる

以下のページを参考に、Pythonのfalconでつくった。さくっとAPIサーバが構築できて非常に良い。

[Falcon \- The minimalist Python WSGI framework](https://falconframework.org/)
[Falconで光速のWeb APIサーバーを構築する \- Qiita](http://qiita.com/icoxfog417/items/913bb815d8d419148c33)
[Python Falcon ちょっと本気のクイックスタート \- Qiita](http://qiita.com/yohjizzz/items/f46bb3bc7b7c40768836)



```python
# -*- coding: utf-8 -*-
import json
import falcon
from analytics import Analytics

class HelloResource(object):

    def on_get(self, req, resp):
        analytics = Analytics()
        scope = ['https://www.googleapis.com/auth/analytics.readonly']

        service_account_email = "analytics@meganii-reports.iam.gserviceaccount.com"
        key_file_location = './key.pem'

        # apiの呼び出し・結果出力
        service = analytics.get_service('analytics', 'v3', scope, key_file_location, service_account_email)
        profile = analytics.get_first_profile_id(service)
        resp.body = json.dumps({ "rows" : analytics.get_json(analytics.get_rankings_results(service, profile))} )

app = falcon.API()
app.add_route("/", HelloResource())


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 3000, app)
    httpd.serve_forever()
```


## Hugo

### popular.html
```
{{ $dataJ := getJSON "http://localhost:3000/" }}
<ul class="list-unstyled urllist">
{{ range first 5 $dataJ.rows }}
  <li>
    <div>
      <a href="{{ index . 1 }}">
        <img class="urllist-img" src="{{ index . 2 }}" width="75" height="75" />
      </a>
      <a href="{{ index . 1 }}">{{ index . 0 }}</a>
    </div>
  </li>
{{ end }}
</ul>
```

## Hugo build

```
hugo server -t hugo-zen
```

あとは、いつも通り、`hugo server`やbuildを実行すれば、動的にJSONリソースにアクセスして、ページを生成してくれる。


気をつけないといけないのは、キャッシュされていること。値が変わらないときは、キャッシュされていることを忘れていた。

`--ignoreCache`とかオプションに指定してあげれば、キャッシュしないようにできます。

[Hugo \- Data\-driven Content](https://gohugo.io/extras/datadrivencontent)



## Pythonスクリプトのデーモン化

Hubotをデーモン化したときに利用した`pm2`を使用した。Node.js用のデーモン化ツールと思っていたがそのほかの言語でも利用できたことがわかった。
取り急ぎ、pm2で対応した。

[http://pm2.keymetrics.io/docs/usage/quick-start/](http://pm2.keymetrics.io/docs/usage/quick-start/)


## まとめ

Pythonで簡単に、APIサーバを構築して、静的サイトジェネレータで、動的にサイトを生成できた。

後は、Circle CIに組み込めば、git push したときに人気記事を読込直して生成してくれる。
