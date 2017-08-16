---

title: phonegap-start
date: 2014-02-16T12:14:00+09:00
category: ['Tech']
tags: 
published: true
slug: phonegap-start
---

## PhogeGapのインストール

```
npm install -g phonegap
```

## Monacaに登録
[Monaca - HTML5モバイルアプリ開発プラットフォーム](http://monaca.mobi/ja/)


## MonacoデバッカーをiPhoneにインストール
AppStoreから Monacaをインストール。


## チュートリアル
以下のチュートリアルをやってみて、雰囲気をつかむ

- [PhoneGapでHello World! 初級講座 | PhoneGap Fan](http://phonegap-fan.com/school/katsuya_2_1.php) 
- [PhoneGapで年齢計算アプリを作ろう！ 初級講座 | PhoneGap Fan](http://phonegap-fan.com/school/katsuya_3_1.php)

基本的には、JavaScriptとHTML5でどうにかなるみたい。スゴイね。


### なんかハマった点
- 「最小限のプロジェクト」を選択して作成したプロジェクトを、Monacoデバッカから見ると、白紙のページにしかならなかった。
⇛ 「Hello World」のプロジェクトを修正することで、対応した。必要なファイルがあるのだろうか。

- 「Hello Wolrd」のプロジェクトを利用しても、JavaScriptが動作しない場合がある。
⇛　Monacaアプリを再インストールすると治った。んー、なぜだ。

#### 追記
iPhoneアプリ側で、キャッシュを削除するというボタンがあるため、それを使えば正常に戻ることが多い。


##Cameraを使用するチュートリアル

以下のチュートリアルページを参考に、Monacoの HelloWorldアプリを修正していきます。

[PhoneGapで端末の機能を用いたアプリを作ろう！ 初級講座 | PhoneGap Fan](http://phonegap-fan.com/school/katsuya_4_1.php)


Camera
[PhoneGap API Documentation](http://docs.phonegap.com/jp/2.2.0/cordova_camera_camera.md.html#camera.getPicture)


### index.html
HelloWorldのサンブルが含まれているが、追加した部分は、`<script></script>`内の

`document.addEventListener`と`snapPicture()`のみ。




```
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <script src="plugins/plugin-loader.js"></script>
    <link rel="stylesheet" href="plugins/plugin-loader.css">
    <link rel="stylesheet" href="css/style.css">
    <script>
        // Set virtual screen width size to 640 pixels
        monaca.viewport({width: 320});
        document.addEventListener ("deviceready", function() {
            $("#camera-button").attr("disabled", false);
        });

        // PhoneGap event handler
        document.addEventListener("deviceready", onDeviceReady, false);
        function onDeviceReady() {
            // Update Toolbar Header
            monaca.updateUIStyle("header", "title", "Your First App");
            monaca.updateUIStyle("tapme-button", "disable", false);
            
            console.log("PhoneGap is ready");
        }
        function onTapButton(){
            // Triggers when button is tapped: defined in index.ui
            navigator.notification.alert("HelloWorld", function() {}, " ", "OK")
        }
        function snapPicture() {
            var options = {
                destinationType: Camera.DestinationType.FILE_URI,
                targetWidth: 150,
                targetHeight: 150
            };
            
            navigator.camera.getPicture(onSuccess, onFail, options)
            
            function onSuccess (imageData) {
                var image = document.createElement("img");
                $(image).attr("src", imageData);
                $("#photos").append(image);
            }
            
            function onFail (message) {
                alert ('error:' + message)
            }
        }
    </script>
</head>
<body>
    <header>PhoneGapで写真撮影</header>
    <div id="photos">
      <!-- ここに写真が登録されていきます -->
    </div>
    <div id="take-photo">
      <input id="camera-button" type="button" onclick="snapPicture()" value="写真を撮影します" disabled>
    </div>
</body>
</html>


```

## 次回
こんなに簡単に、iPhoneの機能を利用できるなんて素敵！
Cameraで撮った写真をWebアプリに連携させたい。




