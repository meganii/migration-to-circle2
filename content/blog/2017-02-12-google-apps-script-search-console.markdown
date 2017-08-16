---
title: "Google Apps ScriptでGoogle Search Consoleの情報を取得する"
date: 2017-02-12T16:54:25+09:00
lastmod: 2017-02-12T16:54:25+09:00
comments: true
category: ['Tech']
tags: ['GoogleAppsScript','GoogleSearchConsole']
published: true
slug: google-apps-script-search-console
img: https://i.gyazo.com/thumb/200/_403a124a37d8ae1a3c1327d873df452c-png.jpg
---

検索ワードは、Google Search ConsoleでWeb管理画面からも確認できますが以下の制限があります。

- データは90日間しか保管されない
- 1000件までしか表示されない

これらの制限を回避するためには、Googleが提供する`Google Search Console API`を利用して自分自身で取得する必要があります。
ここでは、Google Apps Scriptを利用してGoogle Sheetsに結果を出力する方法を紹介します。

<!--more-->
{{% googleadsense %}}


## 手順

- GoogleAppsScriptを利用できるように追加する
- Google Search Console APIを有効化する
- 資格情報を作成
- OAuth2ライブラリの読込
- Google Apps Scriptに処理を記述する
- Developers ConsoleのRedirect URIを記述

### Google Search Console APIを有効化する

[![https://gyazo.com/752b910f61f50470e43e61f0eb54e08b](https://i.gyazo.com/752b910f61f50470e43e61f0eb54e08b.png)](https://gyazo.com/752b910f61f50470e43e61f0eb54e08b)

[![https://gyazo.com/79ea92c85a8acfaadc02154098cadbba](https://i.gyazo.com/79ea92c85a8acfaadc02154098cadbba.png)](https://gyazo.com/79ea92c85a8acfaadc02154098cadbba)


### 資格情報を作成

[![https://gyazo.com/b3550c1f12dbf42fdedc12c96f63771a](https://i.gyazo.com/b3550c1f12dbf42fdedc12c96f63771a.png)](https://gyazo.com/b3550c1f12dbf42fdedc12c96f63771a)


### GoogleAppsScriptを利用できるように追加する


### Google OAuth2ライブラリ追加

[![https://gyazo.com/f06c6ffac99e13c481b8b039dd5f564d](https://i.gyazo.com/f06c6ffac99e13c481b8b039dd5f564d.png)](https://gyazo.com/f06c6ffac99e13c481b8b039dd5f564d)

Resources > Libraryから`1B7FSrk5Zi6L1rSxxTDgDEUsPzlukDsi4KGuTMorsTQHhGBzBkMun4iDF`を追加する。

[![https://gyazo.com/23fa3fb0e5d6eeee44c6a1c557cf44de](https://i.gyazo.com/23fa3fb0e5d6eeee44c6a1c557cf44de.png)](https://gyazo.com/23fa3fb0e5d6eeee44c6a1c557cf44de)

Versionを指定して、保存すればOKです。

[![https://gyazo.com/59388fa7bcb3e713ad8ad33904804bd0](https://i.gyazo.com/59388fa7bcb3e713ad8ad33904804bd0.png)](https://gyazo.com/59388fa7bcb3e713ad8ad33904804bd0)


### Google Apps Scriptに処理を記述する

以下は、Google Search Consoleでデータ抽出して、Google Sheetsに書き込むサンプル。


実行方法は、まず`openSheet`を実行する。
[![https://gyazo.com/6ad8c768d69a872838a2205754061cd8](https://i.gyazo.com/6ad8c768d69a872838a2205754061cd8.png)](https://gyazo.com/6ad8c768d69a872838a2205754061cd8)

その後、`Logs`から認証用のリンクに飛んで、OAuth認証を行います。
[![https://gyazo.com/c2b4cef2bfb5ef60ba43d1f12a777eef](https://i.gyazo.com/c2b4cef2bfb5ef60ba43d1f12a777eef.png)](https://gyazo.com/c2b4cef2bfb5ef60ba43d1f12a777eef)



```
var CLIENT_ID = '{YOUR_CLIENT_ID}';
var CLIENT_SECRET = '{YOUR_CLIENT_SECRET}';
var SITE_URL = 'https%3A%2F%2Fmeganii.com';
var PER_RECORD = 500;

var SHEET_ID = '{YOUR_SHEET_ID}';


function openSheet() {
  var spreadsheet = SpreadsheetApp.openById(SHEET_ID);
  var sheet = spreadsheet.getSheetByName("Sheet");  //この場合、あらかじめ「Sheet」シートを作成しておく
  sheet.clear();
  
  var response = query();
  var json = JSON.parse(response.getContentText());
  var rows = json["rows"];
  
  // Add Header
  sheet.getRange(1, 1).setValue("keys");
  sheet.getRange(1, 2).setValue("clicks");
  sheet.getRange(1, 3).setValue("ctr");
  sheet.getRange(1, 4).setValue("impressions");
  sheet.getRange(1, 5).setValue("position");
  
  for (var i = 0; i < rows.length; i++) {
    sheet.getRange(i+2, 1).setValue(rows[i]["keys"]);
    sheet.getRange(i+2, 2).setValue(rows[i]["clicks"]);
    sheet.getRange(i+2, 3).setValue(rows[i]["ctr"]);
    sheet.getRange(i+2, 4).setValue(rows[i]["impressions"]);
    sheet.getRange(i+2, 5).setValue(rows[i]["position"]);
    Logger.log(rows);
  }
}

function query() {
  var date = new Date('2016-12-01');
  var params = {
    rowLimit: PER_RECORD,
    startDate: '2016-10-01',
    endDate:   '2016-12-31',
    dimensions: ["query"],
  }
  Logger.log(params);
  
  var service = getService();
  if(!service.hasAccess()){
    alertAuth();
    return;
  }
      
  var response = UrlFetchApp.fetch('https://www.googleapis.com/webmasters/v3/sites/'+ SITE_URL +'/searchAnalytics/query', {
    method : "post",
    contentType: "application/json",   
    headers: {
      Authorization: 'Bearer ' + service.getAccessToken(),
    },
    payload:JSON.stringify(params),
  });
  Logger.log(response);
  return response;
}

function alertAuth() {
  var service = getService();
  var authorizationUrl = service.getAuthorizationUrl();
  Logger.log(authorizationUrl);
}

function getService() {
  // Create a new service with the given name. The name will be used when
  // persisting the authorized token, so ensure it is unique within the
  // scope of the property store.
  return OAuth2.createService('webmasters')

      // Set the endpoint URLs, which are the same for all Google services.
      .setAuthorizationBaseUrl('https://accounts.google.com/o/oauth2/auth')
      .setTokenUrl('https://accounts.google.com/o/oauth2/token')

      // Set the client ID and secret, from the Google Developers Console.
      .setClientId(CLIENT_ID)
      .setClientSecret(CLIENT_SECRET)

      // Set the name of the callback function in the script referenced
      // above that should be invoked to complete the OAuth flow.
      .setCallbackFunction('authCallback')

      // Set the property store where authorized tokens should be persisted.
      .setPropertyStore(PropertiesService.getUserProperties())

      // Set the scopes to request (space-separated for Google services).
      .setScope('https://www.googleapis.com/auth/webmasters.readonly')
}

function authCallback(request) {
  var service = getService();
  var isAuthorized = service.handleCallback(request);
  if (isAuthorized) {
    return HtmlService.createHtmlOutput('認証に成功しました。タブを閉じてください。');
  } else {
    return HtmlService.createHtmlOutput('認証に失敗しました。タブを閉じてください。');
  }
}

/**
 * Reset the authorization state, so that it can be re-tested.
 */
function reset() {
  var service = getService();
  service.reset();
}
```



## Google Apps Scriptの種類

Google Apps Scriptには2種類存在する。

- Container Bound Script
- Standalone Script

### Container Bound Script

ExcelマクロのようなGoogle SheetsやDocsに対するスクリプトです。

[![https://gyazo.com/c4bc138b1b9d7f0dc0b4a288fd4f8714](https://i.gyazo.com/c4bc138b1b9d7f0dc0b4a288fd4f8714.png)](https://gyazo.com/c4bc138b1b9d7f0dc0b4a288fd4f8714)

### Standalone Script

[![https://gyazo.com/3bd5f95006f7780c4574c2516c3a9832](https://i.gyazo.com/3bd5f95006f7780c4574c2516c3a9832.png)](https://gyazo.com/3bd5f95006f7780c4574c2516c3a9832)

### Container Bound ScriptとStandalone Scriptの違い

|                        | Container Bound Script                      | Standalone Script |
|:-----------------------|:--------------------------------------------|:-----------------------------------------------|
| 作成方法                   | 各コンテナ(Sheets,Forms,Sites)のメニューから作成 | Drive上またはhttps://script.google.com へアクセス |
| Sheetsでの独自関数         | Spreadsheet上に作成すれば○ | ☓
| onOpenトリガーの自動登録    | ○ | ☓
| Webアプリケーションとして動作 | ○ | ○
| ソースコードのダウンロード | ☓ | ○
| ScriptEditor以外での開発 | ☓ | ○


## 参考

- [Google Apps Script 入門 \- Qiita](http://qiita.com/t_imagawa/items/47fc130a419b9be0b447)
- [Google Apps Scriptの開発手法まとめ \- Qiita](http://qiita.com/soundTricker/items/4d04c97c499b22886dfd)
- [Google Search ConsoleをGoogle Apps Scriptから呼びだす \- Qiita](http://qiita.com/kiita312/items/d5ffd0207b8411c159e1)
- [googlesamples/apps\-script\-oauth2: An OAuth2 library for Google Apps Script\.](https://github.com/googlesamples/apps-script-oauth2)