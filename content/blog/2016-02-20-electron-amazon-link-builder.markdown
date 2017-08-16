---
title: "ElectronでAmazonアフィリエイトリンクビルダーを作った"
date: 2016-02-20T17:51:18+09:00
comments: true
category: ['Tech']
tags: ['Electron', 'JavaScript']
published: true
slug: electron-amazon-link-builder
img: 'https://farm2.staticflickr.com/1467/25143519475_14929051ec_z.jpg'
---

[Electronでデスクトップアプリ作成](https://meganii.com//blog/2016/01/25/electron-tutorial/)に引き続き、Amazonアフィリエイトリンクビルダーのデスクトップアプリを作った。

{{% googleadsense %}}

## 動機

Amazonのアフィリエイトリンクビルダーには、ヨメレバ、カエレバのようなブックマークレットもあるが、現時点でAmazonのリンクがhttpsに対応していないため、せっかくhttps化をしてもchromeのURLバーが緑色にならない。[Lets's Encryptでブログの常時SSL化にチャレンジ](https://meganii.com/blog/2016/01/17/lets-encrypt-always-on-ssl/)

これは困るということで、せっかくなのでElectronでデスクトップアプリを作ってみた。

React.jsとか使ってオシャレに作りたかったのだけど、JavaScript初心者にはまずそもそも素のJavaScriptが何をしているのかがわかってなかったので、一度愚直に作った。

## 外観

<p><a href="https://www.flickr.com/photos/35571855@N06/25117168326" title="electron-amazon-linkbuilderby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1714/25117168326_9fe61fdeb7_z.jpg" alt="electron-amazon-linkbuilder"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/25143519475" title="electron-amazon-linkbuilder-resultby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1467/25143519475_14929051ec_z.jpg" alt="electron-amazon-linkbuilder-result"></a></p>


## コード

正直、JavaScriptの書き方がまだよくわかってない。コールバックの書き方や、関数定義が正しいか怪しいが、ひとまず動くところまではできた。

メインプロセス(main.js)とレンダラープロセス(index.htmlのscript)を意識して書く。レンダラープロセスは、画面の描画に関する記述、メインプロセスは、ファイル処理や主な処理に関する記述と役割が分かれている。

Amazon Product Advertising APIは、`node-apac`というライブラリを利用した。
[dmcquay/node-apac: node-apac - Node.js client for the Amazon Product Advertising API, including support of Request Signatures](https://github.com/dmcquay/node-apac)

少しハマった点は、Endpointの修正と、AWS IDとAWS Secretの取得の部分である。

```
var opHelper = new OperationHelper({
  endPoint:   'webservices.amazon.co.jp',
  awsId:      'YOUR AWS ID',
  awsSecret:  'YOUR AWS SERCET',
  assocId:    'YOUR Amazon ASSOCIATE ID',
});
```

Endpointは、デフォルトだとUSのAmazonを指しているため、`webservices.amazon.co.jp`を指定する。

### IAMユーザを作成してProduct Advertising APIを利用する方法

AWS IDと、AWS Secretを取得するためにはまず、[Product Advertising API](https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html)でDeveloper登録をする必要がある。

<p><a href="https://www.flickr.com/photos/35571855@N06/24777745429" title="Product_Advertising_APIby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1500/24777745429_476475dc3d_z.jpg" alt="Product_Advertising_API"></a></p>

<p><a href="https://www.flickr.com/photos/35571855@N06/24515006124" title="Product_Advertising_APIby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1618/24515006124_a87c7f60cf_z.jpg" alt="Product_Advertising_API"></a></p>


登録完了後は、AWS Security Credentials Consoleから、Access Key ID と Secret Keyを取得する。ここでハマったのは、現在推奨されるのはIAMで特定のユーザを作成して、権限を適切に与えた状態にすることを求められる。


<p><a href="https://www.flickr.com/photos/35571855@N06/24518590253" title="Product_Advertising_APIby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1631/24518590253_86af913239_z.jpg" alt="Product_Advertising_API"></a></p>


<p><a href="https://www.flickr.com/photos/35571855@N06/25145533635" title="IAM_Management_Consoleby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1495/25145533635_26e2116751_z.jpg" alt="IAM_Management_Console"></a></p>

そうか、では、Product Advertising API用にユーザを作って、ユーザを作成してProduct Advertisingのポリシーをアタッチすればよいのだなと思い、やってみたのだが、Product Adverting APIなんて存在しない。。。

<p><a href="https://www.flickr.com/photos/35571855@N06/24849951570" title="IAM_Management_Consoleby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1624/24849951570_05b18beda4_z.jpg" alt="IAM_Management_Console"></a></p>

<a href="https://forums.aws.amazon.com/thread.jspa?threadID=171558">AWS Developer Forums: Support for IAM Users in Product ...</a>のフォーラムを読むと、`AdministratorAccess`
のポリシーを設定してあげれば良いとのこと。(Admin権限を与えるんじゃ意味ないのではと思ったが)

よって、IAMを利用する場合は、`AdministratorAccess`のポリシーをアタッチして、keyを取得すれば良い。



### index.html
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>LinkBuilder</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/photon.css">
  </head>
  <body>
    <div class="window">

      <header class="toolbar toolbar-header">
        <h1 class="title">Amazon Link Builder</h1>
      </header>

      <div class="window-content">
        <div class="row container">
          <div id="tab-amazon" class="col-md-12">

            <h1>Link Builder</h1>

            <div id="control">
              <form class="form-inline">
                <div class="form-group">
                  <label for="search-word">検索条件</label>
                  <input type="text" class="form-control" id="search-word" placeholder="search" width="500px">
                </div>
                <button type="submit" class="btn btn-default" onclick="sendQuery();">検索する</button>
              </form>
              <textarea id="linkbox" class="form-control" name="linkbox" rows="8" cols="40"></textarea>
            </div>
            <div id="content" class="row">
            </div>
          </div>

      </div>
    </div>

    <script>
      const ipcRenderer = require('electron').ipcRenderer;

      // send message to main process
      var sendQuery = function() {
        var filelds = document.getElementById('search-word').value;
        ipcRenderer.send('asynchronous-message-amazon', filelds);
      }

      // from main process
      ipcRenderer.on('asynchronous-reply-amazon', function(event, arg) {
        for (var i = 0; i < arg.length; i++) {
          // create div
          var div = createItemElement(arg[i]);
          div.className = "col-sm-6 col-md-3"
          document.getElementById('content').appendChild(div);
        }
      });

      ipcRenderer.on('asynchronous-reply-createUrl', function(event, result) {
          document.getElementById('linkbox').textContent = result;
      });

      // <div class="item">
      //  <label><input type='checkbox' onclick='handleClick(this);'>Checkbox</label>
      //  <a href="http://hoge"><img src="hoge" /></a>
      // </div>
      var createItemElement = function(item) {

        var createRakutenLink = function(item){
          var isbn = item.ItemAttributes[0].ISBN;
          if (isbn !== undefined) {
            ipcRenderer.send('asynchronous-message-rakuten', isbn);
          }
        };

        var handleClick = function() {
          console.log('handleClick');
          // send message
          // on message
          // contentは、main process側で作成する
          ipcRenderer.send('asynchronous-message-createUrl', item);
        };

        var div = document.createElement('div');
        div.className = "thumbnail";
        div.textContent = item.ASIN;

        // create image
        var a = document.createElement('a');
        a.href = item.DetailPageURL;
        var img = document.createElement('img');
        // http://ecx.images-amazon.com/images/I/51XdQhacD-L._SL75_.jpg
        // https://images-na.ssl-images-amazon.com/images/I/51UMwuX4tjL._SL160_.jpg
        var url = "";
        url += item.MediumImage[0].URL;
        img.src = url.replace(/http:\/\/ecx\.images-amazon\.com\/images\//, 'https://images-na.ssl-images-amazon.com/images/');
        a.appendChild(img);

        // create label
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.onclick = handleClick;

        div.appendChild(checkbox);
        div.appendChild(a);
        return div;
      };

    </script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js" onload="window.$ = window.jQuery = module.exports;"></script>
    <script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script src="js/menu.js" charset="utf-8"></script>
  </body>
</html>
```


### main.js
```
'use strict';

const electron = require('electron');
// Module to control application life.
const app = electron.app;
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow;

const ipcMain = electron.ipcMain;
const util = require('util');
const OperationHelper = require('apac').OperationHelper;
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow;

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    'min-width': 500,
    'min-height': 200,
    'accept-first-mouse': true,
    'title-bar-style': 'hidden'
  });

  // and load the index.html of the app.
  mainWindow.loadURL('file://' + __dirname + '/index.html');

  // Open the DevTools.
  // mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', function() {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null;
  });
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
app.on('ready', createWindow);

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow();
  }
});

// ---my code----------
ipcMain.on('asynchronous-message-amazon', function(event, arg) {
  var opHelper = new OperationHelper({
    endPoint:   'webservices.amazon.co.jp',
    awsId:      'YOUR AWS ID',
    awsSecret:  'YOUR AWS SERCET',
    assocId:    'YOUR Amazon ASSOCIATE ID',
  });
  opHelper.execute('ItemSearch', {
    'SearchIndex': 'Books',
    'Keywords': arg,
    'ResponseGroup': 'Images,ItemAttributes,Offers'
  }, function(err, results) {
      var items = results.ItemSearchResponse.Items[0].Item;
      event.sender.send('asynchronous-reply-amazon', items);
  });
});

// create rakuten affiliateUrl
ipcMain.on('asynchronous-message-rakuten', function(event, arg) {
  console.log('start');
  var url = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522?format=json&affiliateId={YOUR_AFF_ID}&applicationId={APP_ID}&isbn=' + arg;
  getRequsest(url, function(result){
    console.log(result.Items[0].Item.affiliateUrl);
    event.sender.send('asynchronous-reply-rakuten', result);
  });
});

ipcMain.on('asynchronous-message-createUrl', function(event, arg) {
  console.log('start asynchronous-message-createUrl');
  var item = arg;

  console.log(item.ItemAttributes[0].ISBN);
  // rakuten
  var url = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522?format=json&affiliateId={YOUR_AFF_ID}}&applicationId={YOUR_APP_ID}&isbn=' + item.ItemAttributes[0].ISBN;
  getRequsest(url, function(result){
    var url = "";
    url += item.MediumImage[0].URL;
    var src = url.replace(/http:\/\/ecx\.images-amazon\.com\/images\//, 'https://images-na.ssl-images-amazon.com/images/');

    console.log(result.Items[0].Item.affiliateUrl);
    var content =   '<div class="booklink-box">'
                  +   '<div class="booklink-image">'
                  +     '<a href=' + item.DetailPageURL[0] + ">"
                  +       '<img src="' + src + '" />'
                  +     '</a>'
                  +   '</div>'
                  +   '<div class="booklink-info">'
                  +     '<div class="booklink-name">'
                  +       '<a href="http://www.amazon.co.jp/exec/obidos/asin/' + item.ASIN +'/meganii-22/">'
                  +         item.ItemAttributes[0].Title
                  +       '</a>'
                  +     '</div>'
                  +     '<div class=shoplinkrakuten>'
                  +       '<a href="' + result.Items[0].Item.affiliateUrl + '">楽天で買う</a>'
                  +     '</div>'
                  +   '</div>'
                  + '</div>';
      event.sender.send('asynchronous-reply-createUrl', content);
  });
});

// to get request
var getRequsest = function(url, callback) {
  if (!url) { return; }
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.timeout = 30000;
  xhr.ontimeout = function() {
    console.log('time out');
  };
  xhr.onerror = function() {
    console.log('error');
  };
  xhr.onreadystatechange = function() {
    if (this.readyState !== 4) { return; }

    if (this.status === 200) {
      if (typeof callback === 'function') {
        try {
          var result = JSON.parse(this.responseText);
          callback(result);
        } catch (e){
          console.log(e);
        }
        return;
      }
    }
  };
  xhr.send();
};
```

## 参考

{{% amazon_ 4798131113 %}}
{{% amazon_ 4798128457 %}}