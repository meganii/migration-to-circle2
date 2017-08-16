---
title: "Google Cloud Functions for Firebase -FirebaseからCloud Functionを使ってみた"
date: 2017-08-11T07:42:17+09:00
lastmod: 2017-08-11T07:42:17+09:00
comments: true
category: ['Tech']
tags: ['Firebase','CloudFunction']
published: false
slug: google-cloud-functions-for-firebase
img:
---



[Firebase]: https://firebase.google.com/?hl=ja

## Firebaseとは?

[Firebase]とは、元々はモバイル向けのバックエンドサービス(MBaaS, BaaS)のプロダクトでした。代表的な機能は、Realtime Database(リアルタイム同期データベース)でしょうか。

Googleが2014年に買収し、Googleが元々提供するサービスと統合する形で機能が拡張され、今では下記に書き出すようにさまざまなサービスを提供しています。

[Firebase]を利用することにより、アプリ開発のバックエンド部分を丸ごと面倒をみてくれるのでアプリ開発者の負担を減らすことができます。


<!--more-->
{{% googleadsense %}}


今回は、Realtime Databaseと、Cloud Functions, Hostingを利用して、Reactアプリを作成しました。


### アプリの作成とテスト Develop & test your app

- **Realtime Database** (Store and sync app data in milliseconds)
- **Crash Reporting** (Find and prioritize bugs; fix them faster)
- **Authentication** (Authenticate users simply and securely)
- **Cloud Functions** (Run mobile backend code without managing servers)
- **Cloud Storage** (Store and serve files at Google scale)
- **Hosting** (Deliver web app assets with speed and security)
- **Test Lab for Android** (Test your app on devices hosted by Google)
- **Performance Monitoring** (Gain insight into your app's performance)


### ユーザー層の拡大と利用促進 Grow & engage your audience

- **Google Analytics** (Get free and unlimited app analytics)
- **Cloud Messaging** (Send targeted messages and notifications)
- **Dynamic Links** (Drive growth by using deep links with attribution)
- **Remote Config** (Modify your app without deploying a new version)
- **Invites** (Make it easy to share your app and content)
- **App Indexing** (Drive search traffic to your mobile app)
- **AdMob** (Maximize revenue with in-app ads)
- **AdWords** (Drive installs with targeted ad campaigns)


[Google、Firebaseをモバイル開発者に向けた統一プラットフォームに進化させる \| TechCrunch Japan](http://jp.techcrunch.com/2016/05/20/20160518google-turns-firebase-into-its-unified-platform-for-mobile-developers/)

[第1回　一歩進んだMBaas，Firebaseとは？：スマホアプリ開発を加速する，Firebaseを使ってみよう｜gihyo\.jp … 技術評論社](http://gihyo.jp/dev/serial/01/firebase/0001)

[Firebaseの始め方 \- Qiita](http://qiita.com/kohashi/items/43ea22f61ade45972881)



## Firebase FunctionsとGoogle Cloud Functionsの関係

Cloud Functions for Firebaseと言われてもピンきませんでしたが、動かしてみると概要が掴めたのでメモします。

Cloud Function for Firebaseは、Firebaseへのイベントを受け取って、Cloud Function内(サーバ側)で処理をするものです。

![Cloud Function for firebase](https://farm5.staticflickr.com/4346/36394476171_612982a2ca.jpg)


Firebase Funtionsは、`firebase deploy --only functions`を実行すると、FunctionがFirebaseにデプロイされますが、実態はGoogle Cloud PlatformのCloud Functionsに作られます。


サンプルのfunction

```javascript
import * as functions from "firebase-functions"
import cors from "cors"
import express from "express"

const app = express()
app.use(cors({ origin: true }))
app.get("/users", (req, res) => {
  response.send("users")
})

export let api = functions.https.onRequest(app)
```

後は、apiのURLを叩けばCloud Functionが動作します。

ここでの注意点は、**FirebaseのSPARK(無料プラン)では外向けに通信ができない**ということです。外部への通信が発生するような処理(例えば、function内で別のGETリクエストを投げるなど)を行う場合は、BLAZE(従量課金プラン)にする必要があります。

BLAZE(従量課金プラン)だと、Cloud Functionには無料枠がありますが、HostingやRealtime Databaseには無料枠がありません。

今回は、Cloud Functionsを動かすFirebaseプロジェクト(BLAZE)と、Reactアプリを動かすFirebaseプロジェクト(SPARK)を分けてみました。

### Firebaseへのdeployログ

```
$ $(npm bin)/babel src --out-dir functions
src/index.js -> functions/index.js

$ firebase deploy --only functions
=== Deploying to 'xxxx-xxx-xxxxx'...

i  deploying functions
i  functions: ensuring necessary APIs are enabled...
i  runtimeconfig: ensuring necessary APIs are enabled...
✔  runtimeconfig: all necessary APIs are enabled
✔  functions: all necessary APIs are enabled
i  functions: preparing functions directory for uploading...
i  functions: packaged functions (11.58 KB) for uploading
✔  functions: functions folder uploaded successfully
i  starting release process (may take several minutes)...
i  functions: updating function api...
✔  functions[api]: Successful update operation.
✔  functions: all functions deployed successfully!

✔  Deploy complete!

Project Console: https://console.firebase.google.com/project/xxxx-xxxxx/overview
Function URL (api): https://us-central1-xxxx-xxxxx.cloudfunctions.net/api
```


### 参考リンク

- [Cloud Functions for Firebaseとは？ \- Qiita](http://qiita.com/koki_cheese/items/013d4e6ab5aefc792388)
- [node\.js \- Calling HTTPS request on google cloud function getting connect connect to server \- Stack Overflow](https://stackoverflow.com/questions/43176794/calling-https-request-on-google-cloud-function-getting-connect-connect-to-server)

## Reactアプリ作成

詳しくは別記事でまとめる予定ですが、`create-react-app`で雛形を作って利用しました。

```
npm install -g create-react-app
create-react-app
```

## Realtime Databaseの使い方

今までほぼリレーショナルデータベースしか触ってこなかったので、スキーマレスデータベース、リアルタイム同期データベースと言われてもすんなりと理解できませんでした。今回、自分でアプリを使ってみて理解が増しました。

特にRealtime Databaseは、Reactとの相性がよく、ある端末でデータを更新した場合、すぐにその更新分をReact側で反映できるというのは、みていてこぎみよい感じでした。



## データの取得

```javascript
var starCountRef = firebase.database().ref('posts/' + postId + '/starCount');
starCountRef.on('value', function(snapshot) {
  updateStarCount(postElement, snapshot.val());
});
```

一度だけ値を取得すればよい場合は、以下の通り。

```javascript
var userId = firebase.auth().currentUser.uid;
return firebase.database().ref('/users/' + userId).once('value').then(function(snapshot) {
  var username = snapshot.val().username;
  // ...
});
```

## データの更新

`update()`を利用します。

```javascript
const stocksRef = firebase.database().ref().child('stocks');
let updates = {};
let list = [];
stocksRef.once('value').then((snap) => {
  list = snap.val();
  const stocks = Object.keys(list).map(key=> Object.assign(list[key], {key}));
  stocks.map((stock) => {
    fetch(`${CLOUD_FUNCTION_API_URL}/stocks/${stock.code}`)
      .then(response => response.text())
      .then(text => text.split('\n'))
      .then(str => str.slice(8, str.length-1))
      .then(str => str[str.length-1].split(','))
      .then((str) => {
        console.log(str[1]);
        updates['/stocks/' + stock.key] = {
          avgBuyPrice: stock.avgBuyPrice,
          code: stock.code,
          currentPrice: str[1],
          name: stock.name,
          numberOfSharesHeld: stock.numberOfSharesHeld,
          previousPrice: stock.previousPrice,
        };
        firebase.database().ref().update(updates);
      });
  });
});
```

## Tips メモ

### 結果を配列にする

React内で
何かよいやり方があれば、

```javascript
const stocksRef = firebase.database().ref().child('stocks');
let list = [];
stocksRef.once('value').then((snap) => {
  list = snap.val();
  const stocks = Object.keys(list).map(key=> Object.assign(list[key], {key}));
  console.log(stocks);
});
```
