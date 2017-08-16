---
title: "Electronでデスクトップアプリ作成"
date: 2016-01-25T07:15:22+09:00
comments: true
category: ['Tech']
tags: ['electron','React.js']
published: true
slug: electron-tutorial
img: "https://farm2.staticflickr.com/1653/24649661356_a4251f1e29_n.jpg"
---


<p><a href="https://www.flickr.com/photos/35571855@N06/24649661356" title="electronby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1653/24649661356_a4251f1e29_z.jpg" alt="electron"></a></p>


Electronを使って自分用のデスクトップアプリを作りたいと思い、調べてみた。

{{% googleadsense %}}

## JavaScriptの開発環境を整える

node.jsのバージョンをみると、未だに 0.1系だった。2016/01/25現在、Node.jsの最新バージョンは、`v5.5.0` !!!!
[Node.js](https://nodejs.org/en/)

JavaScriptの進化はすごい！！と思ったら、Node.jsとio.jsの争いがあったみたいで、Node.jsは1系の次は2,3を飛ばしてv4になってみたい。

<script async class="speakerdeck-embed" data-id="3505d390fb8448baa0de732c31544228" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>

### nodebrew

その前に、Homebrewで入れていたNode.jsを削除する。

```
brew uninstall node
```

nodeのバージョンを管理するために、nodebrewを導入する。
[hokaccha/nodebrew: Node.js version manager](https://github.com/hokaccha/nodebrew)

```
curl -L git.io/nodebrew | perl - setup
```

`.bash_profile`にパスを通す

```
export PATH=$HOME/.nodebrew/current/bin:$PATH
```

bashに適用する
```
source ~/.bashrc
```


### Node.jsのインストール

バージョンを指定してインストールする。

```
nodebrew install-binary v.5.5.0
```

Node.jsとnpmが最新化された。
```
node -v
v5.5.0
npm -v
3.3.12
```


## Electronのインストールとアプリ起動

以下の通りコマンドを叩けば、最初のElectronアプリが起動する。

```
# Clone the Quick Start repository
$ git clone https://github.com/atom/electron-quick-start

# Go into the repository
$ cd electron-quick-start

# Install the dependencies and run
$ npm install && npm start
```

ただ、ここからどうやっていじっていくか途方にくれた。そもそも、JavaScriptの書き方が分からない。基本的な文法は抑えているつもりだけど、実際にJavaScriptで何か作り上げた経験がないので、

でも、どうせなら最新のJavaScriptの流れにも追いついておきたい。最新ホットな話題といえば、React.jsかなと安易に考え、とりあえず、React.jsのチュートリアルをやってみた。
[チュートリアル | React](https://facebook.github.io/react/docs/tutorial-ja-JP.html)

## React.jsを利用したQiitaの記事一覧を取得して表示するElectronアプリ

まず参考にしたのが、以下のQiitaのコード。

[JavaScript - RailsエンジニアがElectronを触ってみた - Qiita](http://qiita.com/ysk_1031/items/9b9b0c485a8a68ee73a8)


```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Electron Sample</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/0.14.6/react.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/0.14.6/react-dom.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.23/browser.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/0.3.2/marked.min.js"></script>
  </head>
  <body>
    <div class="container">
      <h1>Qiita Item Reader</h1>
      <div id="content"></div>
      <!-- <script type="text/babel" src="src/app.js"></script> -->
      <script type="text/babel">

        var QiitaBox = React.createClass({
          getInitialState: function(){
            return {data: []};
          },
          componentDidMount: function() {
            $.ajax({
              url: "http://qiita.com/api/v2/items",
              dataType: 'json',
              cache: false,
              success: function(data) {
                this.setState({data: data});
              }.bind(this),
              error: function(status, err) {
                console.error(status, err.toString());
              }.bind(this)
            });
          },
          render: function() {
            return (
              <div className="qiitaBox">
                <QiitaList data={this.state.data} />
              </div>
            );
          }
        });

        var QiitaList = React.createClass({
          render: function() {
            var itemNodes = this.props.data.map(function(item) {
              return (
                <QiitaItem key={item.id}>
                  {item.title}
                </QiitaItem>
              );
            });
            return (
              <div className="qiitaList">
                {itemNodes}
              </div>
            );
          }
        });

        var QiitaItem = React.createClass({
          render: function() {
            return (
              <div className="qiitaItem">
                {this.props.children}
              </div>
            );
          }
        });

        ReactDOM.render(
          <QiitaBox />,
          document.getElementById('content')
        );
      </script>
    </div>
  </body>
</html>
```

```
'use strict';

const electron = require('electron');
// Module to control application life.
const app = electron.app;
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow;

const ipcMain = electron.ipcMain;

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow;

function createWindow () {
  // Create the browser window.
  // mainWindow = new BrowserWindow({width: 800, height: 600});
  mainWindow = new BrowserWindow({width: 800, height: 600, 'node-integration': false});


  // and load the index.html of the app.
  mainWindow.loadURL('file://' + __dirname + '/index.html');

  // Open the DevTools.
  mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', function() {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null;
  });
}

var onlineStatusWindow;

app.on('ready', function() {
  onlineStatusWindow = new BrowserWindow({ width: 0, height: 0, show: false });
  onlineStatusWindow.loadURL('file://' + __dirname + '/online-status.html');
});

ipcMain.on('online-status-changed', function(event, status) {
  console.log(status);
});

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

```

## jQueryが読み込まれない件


以下のエラーが出るのだが、jQeuryの読み込みに問題があるみたい。

```
Uncaught ReferenceError: $ is not defined
```

以下のように、node-integrationをfalseにすればエラーはなくなる。（その他のnode.jsのライブラリも読み込まれなくなる模様）

```
mainWindow = new BrowserWindow({width: 800, height: 600, 'node-integration': false});
```

[Electron で jQuery をスマートに読み込む方法 | phiary](http://phiary.me/electron-jquery-script-tag-load/)



## Electronで作られたアプリケーションの一覧
[sindresorhus/awesome-electron](https://github.com/sindresorhus/awesome-electron)
