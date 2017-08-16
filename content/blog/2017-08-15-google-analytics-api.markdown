---
title: "HugoのData driven ContentのためにCloud FunctionsでGoogle Analytics Reporting API v4を利用する"
date: 2017-08-15T19:42:44+09:00
lastmod: 2017-08-15T19:42:44+09:00
comments: true
category: ['Tech']
tags: ['Hugo','CloudFunctions','Serverless']
published: true
slug: google-analytics-reporting-api-v4-on-cloud-functions
img:
---

HugoのData driven Contentを利用するために、Google Analytics

## 狙い

- さくらVPS撤廃に伴い、元々[Hugoで人気記事を表示するためJSONを返すAPIサーバを作りData\-driven Contentを試してみた](https://www.meganii.com/blog/2016/09/06/hugo-data-driven-content-for-polupar-posts/)で実現していた人気記事の取得APIをGoogle Cloud Functionに切り替えたい
- Google Cloud Functionsに切り替えるため、Pythonで書いていた
- Google Analytics Reporting APIがいつのまにかv4に上がっていたため追随する


## この記事に書いてあること

- Node.jsからGoogle Analytics Reporting V4を利用する方法
- Cloud Functionsへの適用
- async/awaitの利用方法


<!--more-->
{{% googleadsense %}}


## 前提

- Node.js v8.2.1　-> v6.11.1へBabelでコンパイル


### 事前準備

- サービスアカウントを管理者として追加しておく。

[google/google\-api\-nodejs\-client: Google's officially supported Node\.js client library for accessing Google APIs\. Support for authorization and authentication with OAuth 2\.0, API Keys and JWT \(Service Tokens\) is included\. API Reference Docs: http://google\.github\.io/google\-api\-nodejs\-client/](https://github.com/google/google-api-nodejs-client)



- [概要  \|  アナリティクス Reporting API v4  \|  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/v4/)


DimensionsとMetricsのパラメータは、下記リファレンスを参照する。

[Dimensions & Metrics Explorer  \|  アナリティクス Reporting API v4  \|  Google Developers](https://developers.google.com/analytics/devguides/reporting/core/dimsmets)


## json認証ファイルを利用して

サービスアカウントの作成から認証ファイル(json)を作成し、その認証ファイルで認証を行い、Google AnalyticsのAPIを叩きます。


[google/google\-api\-nodejs\-client: Google's officially supported Node\.js client library for accessing Google APIs\. Support for authorization and authentication with OAuth 2\.0, API Keys and JWT \(Service Tokens\) is included\. API Reference Docs: http://google\.github\.io/google\-api\-nodejs\-client/](https://github.com/google/google-api-nodejs-client#using-jwt-service-tokens)


以下のサンプルスクリプトを参考にしました。

> The Google Developers Console provides .json file that you can use to configure a JWT auth client and authenticate your requests.
.jsonファイルでの認証は、JWT(JSON Web Token)で行うそうです。


```javascript
var key = require('/path/to/key.json');
var jwtClient = new google.auth.JWT(
  key.client_email,
  null,
  key.private_key,
  ['https://www.googleapis.com/auth/plus.me', 'https://www.googleapis.com/auth/calendar'], // an array of auth scopes
  null
);

jwtClient.authorize(function (err, tokens) {
  if (err) {
    console.log(err);
    return;
  }

  // Make an authorized request to list Drive files.
  drive.files.list({
    auth: jwtClient
  }, function (err, resp) {
    // handle err and response
  });
});
```


### 前提

```javascript
const google = require('googleapis');
const key = require('./cloud-api-9c4e9dc86ba5.json');
const request = require('request');
const cheerio = require('cheerio');

const jwtClient = new google.auth.JWT(
  key.client_email,
  null,
  key.private_key,
  ['https://www.googleapis.com/auth/analytics.readonly', 'https://www.googleapis.com/auth/analytics'],
  null
);

jwtClient.authorize(function (err, data) {
  if (err) {
    console.log(err);
    return;
  }

  const analyticsreporting = google.analyticsreporting('v4');
  const params = {
        'auth': jwtClient,
        'resource': {
          'reportRequests': [{
              "viewId": "68665476",
              "metrics": [{
                  "expression": "ga:pageviews"
              }],
              "dimensions": [{
                  "name": "ga:pageTitle",
                  "name": "ga:pagePath"
              }],
              "orderBys": [{
                  "fieldName": "ga:pageviews",
                  "sortOrder": "DESCENDING"
              }]
          }]
        }
    };

  analyticsreporting.reports.batchGet(params, {}, (error, result) => {
    if (error) { console.log(error); }
    const data = result.reports[0].data;
    console.log(data);
  });
});
```

Google Analytics Reporting APIからデータを取得するだけであれば、上記のように


```javascript
import google from 'googleapis';
import key from './cloud-api-9c4e9dc86ba5.json';
import request from 'request';
import cheerio from 'cheerio';

function googleAuth() {
  return new Promise((resolve, reject) => {
    const jwtClient = new google.auth.JWT(
      key.client_email,
      null,
      key.private_key,
      ['https://www.googleapis.com/auth/analytics.readonly', 'https://www.googleapis.com/auth/analytics'],
      null
    );

    jwtClient.authorize(function (err, data) {
      if (err) {
        console.log(err);
        return;
      } else {
        resolve(jwtClient);
      }
    });
  });
}

function getAnalyticsReportData(jwt) {
  return new Promise((resolve, reject) => {
    const analyticsreporting = google.analyticsreporting('v4');
    const params = {
      'auth': jwt,
      'resource': {
        'reportRequests': [{
          "viewId": "68665476",
          "metrics": [{
            "expression": "ga:pageviews"
          }],
          "dimensions": [
            {"name": "ga:pageTitle"},
            {"name": "ga:pagePath"}
          ],
          "orderBys": [{
            "fieldName": "ga:pageviews",
            "sortOrder": "DESCENDING"
          }]
        }]
      }
    };

    analyticsreporting.reports.batchGet(params, {}, (error, result) => {
      if (error) { console.log(error); }
      const data = result.reports[0].data;
      resolve(data);
    });
  });
}

function createAddingThumbTask(data) {
  return new Promise((resolve, reject) => {
    request('https://meganii.com' + data.dimensions[1], (error, response, body) => {
      const $ = cheerio.load(body);
      const img = $('head').find("meta[property='og:image']").attr('content');
      resolve([data.dimensions[0], data.dimensions[1], img, data.metrics[0].values[0]]);
    });
  });
}

async function execAll(req, res) {
  // Google Authorization
  let jwt = await googleAuth();

  // Get Google Analytics Reports data
  let data = await getAnalyticsReportData(jwt);

  // Create adding og:image Tasks
  let createTasks = async _ => {
    return data.rows.slice(0,10).filter((row) => {
      return row.dimensions[1] === '/' ? false : true;
    }).map(async row => {
      return await createAddingThumbTask(row)
    });
  }
  let tasks = await createTasks();

  // Do the tasks
  Promise.all(tasks).then((rankingData) => {
    console.log(rankingData);
    res.send({
      'rows': rankingData
    })
  });
}

execAll();
```


### メモ

async / awaitを使うときに、ひたすらawaitは予約語だから使うなとコンパイラに怒られた。しばらく原因がわからなかったのだが、awaitを使うためには、呼び出す関数が全てasync修飾子がついていないといけないようだ。このあたり、理解が足りない。

`await is a reserved word`

[javascript \- Await is a reserved word error inside async function \- Stack Overflow](https://stackoverflow.com/questions/42299594/await-is-a-reserved-word-error-inside-async-function)


## 非同期処理を同期的に書く


<script src="https://gist.github.com/meganii/5b858bea7067b951c57582772657d50f.js"></script>

JavaScript Promiseの本は、すごくお世話になっています。

- [JavaScript Promiseの本](http://azu.github.io/promises-book/)
- [JavaScriptのasync/awaitがPromiseよりもっと良い \- Qiita](http://qiita.com/Anders/items/dfcb48d8b27ceaffb443)
- [Promiseとasync/awaitを用いた非同期処理の実装 \- TerraSkyBase](https://base.terrasky.co.jp/articles/3BHoO)
- [Promiseとasync\-awaitの例外処理を完全に理解しよう \- Qiita](http://qiita.com/gaogao_9/items/40babdf63c73a491acbb)
- [async/awaitで非同期処理はシンプルになる \- Qiita](http://qiita.com/ryosukes/items/db8b45c8ea42f924f02f#_reference-e1ed8768cf3ba6648d1d)


## 料金
