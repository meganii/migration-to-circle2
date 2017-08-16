---

title: "AngularJSでFlickrの埋め込みタグを作成する"
date: 2014-11-08T20:37:00+09:00
comments: true
category: ['Tech']
tags: ['AngularJS']
published: true 
slug: angular-flickr
---

ブログ用に自分のFlickrフォトストリームから画像を選択して、貼り付け用URLを作りたくなったので、AngularJSで作ってみた。

[meganii.com/angularjs-flickr.html](http://meganii.com/angularjs-flickr.html)


## 参考
- [AngularJS — Superheroic JavaScript MVW Framework](https://angularjs.org/)
- [AngularJS入門 (全12回) - プログラミングならドットインストール](http://dotinstall.com/lessons/basic_angularjs)
- [daisy1754/angular-simple-demo-flickr-cat · GitHub](https://github.com/daisy1754/angular-simple-demo-flickr-cat)

こういうときのドットインストールはとても便利。



{{% googleadsense %}}

### angularjs-flickr.html 

```html
<html ng-app="FlickrPhotos">
  <head>
    <script src="angular.min.js"></script>
    <script src="photo_controller.js"></script>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css">
  </head>
  <body ng-controller="PhotoCtrl">
    <h1>Make Markdown URL for Flickr</h1>
    <div class="col-md-12">
      <label>Time: </label>
      <input type="text" ng-model="time">
      <button ng-click="doSearch()">Search</button>
      <div ng-show="loadingIndicator"><img src="loading-indicator.gif"></div>
    </div>
    <div class="col-md-6">
      <h2>My photos</h2>
      <div>
        <ul>
          <div ng-repeat="photo in photos">
          <li>
            <input type="checkbox" ng-model="photo" id="photo-{{photo.id}}" ng-change="selected({{$index}})">
            <h2>{{photo.title}}</h2>
            <img ng-src="http://farm{{photo.farm}}.static.flickr.com/{{photo.server}}/{{photo.id}}_{{photo.secret}}_z.jpg">
          </li>
        </ul>
        </div>
      </div> 
    </div>
    <div class="col-md-6">
      <h2>Selected</h2>
        <textarea class="form-control" row="3">{{markdown}}</textarea>
        <div ng-repeat="photo in photos | filter:selectedFilter">
          <h2>{{photo.title}}</h2>
          <img class="img-responsive" src="http://farm{{photo.farm}}.static.flickr.com/{{photo.server}}/{{photo.id}}_{{photo.secret}}_m.jpg">
        </div>
    </div>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
  </body>
</html>
```

## photo_contoroller.js

```js
var App = angular.module('FlickrPhotos', []);

App.controller('PhotoCtrl', function RepoListCtrl($scope, $http) {

  $scope.markdown = "";

  $scope.doSearch = function() {
    $http.jsonp("https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=API_KEY&user_id=35571855%40N06&sort=date-posted-desc&format=json&jsoncallback=JSON_CALLBACK")
      .success(function(data) {
        $scope.photos = data.photos.photo;
        $scope.loadingIndicator = false;
      });
    $scope.loadingIndicator = true;
  }

  $scope.selectedFilter = function(photo) {
    return photo.selected == true;
  }

  $scope.selected = function(index) {
  	$scope.photos[index].selected = true;
  	$scope.markdown = $scope.markdown + makeLinkTag($scope.photos[index]);
  }

  function makeLinkTag(photo) {
  	return '<p><a href="https://www.flickr.com/photos/' + photo.owner + '/' + photo.id + '" title="' + photo.title + 'by meganii, on Flickr"><img class="img-responsive" src="https://farm' + photo.farm + '.staticflickr.com/' + photo.server +'/' + photo.id + '_' + photo.secret + '_z.jpg" alt="' + photo.title + '"></a></p>\n';
  }

  $scope.titleFilter = function(photo) {
    if (!$scope.filterWord || $scope.filterWord.length == 0) return true;
    return photo.title.indexOf($scope.filterWord) >= 0;
  }
})
```


<div class="kaerebalink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="kaerebalink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873116678/meganii-22/ref=nosim/" rel="nofollow" target="_blank"><img src="https://images-na.ssl-images-amazon.com/images/I/515Z%2BlXDi4L._SL160_.jpg" style="border: none;" /></a></div><div class="kaerebalink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="kaerebalink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4873116678/meganii-22/ref=nosim/" rel="nofollow" target="_blank">AngularJSアプリケーション開発ガイド</a><div class="kaerebalink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://kaereba.com" rel="nofollow" target="_blank">カエレバ</a></div></div><div class="kaerebalink-detail" style="margin-bottom:5px;">Brad Green,Shyam Seshadri オライリージャパン 2014-04-18    </div><div class="kaerebalink-link1" style="margin-top:10px;"><div class="shoplinkamazon" style="display:inline;margin-right:5px"><a href="http://www.amazon.co.jp/gp/search?keywords=AngularJS&__mk_ja_JP=%83J%83%5E%83J%83i&tag=meganii-22" rel="nofollow" target="_blank" title="アマゾン" >Amazonで購入</a></div><div class="shoplinkrakuten" style="display:inline;margin-right:5px"><a href="http://hb.afl.rakuten.co.jp/hgc/0f1c1106.d5997202.117c2ed9.4ab7d4d2/?pc=http%3A%2F%2Fsearch.rakuten.co.jp%2Fsearch%2Fmall%2FAngularJS%2F-%2Ff.1-p.1-s.1-sf.0-st.A-v.2%3Fx%3D0%26scid%3Daf_ich_link_urltxt%26m%3Dhttp%3A%2F%2Fm.rakuten.co.jp%2F" rel="nofollow" target="_blank" title="楽天市場" >楽天市場で購入</a></div></div></div><div class="booklink-footer" style="clear: left"></div></div>
