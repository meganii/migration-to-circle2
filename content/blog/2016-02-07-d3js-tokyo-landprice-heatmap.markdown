---
title: "D3.jsで東京の地価データを可視化する"
date: 2016-02-07T19:42:50+09:00
comments: true
category: ['Tech']
tags: ['D3.js', 'JavaScript']
published: true
slug: d3js-tokyo-landprice-heatmap
img: "https://farm2.staticflickr.com/1680/24844125586_c74f952e38_s.jpg"
---

<p><a href="https://www.flickr.com/photos/35571855@N06/24844125586" title="tokyo-landprice_heatmapby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1680/24844125586_c74f952e38_z.jpg" alt="tokyo-landprice_heatmap"></a></p>


{{% googleadsense %}}

[d3js tutorial | じょーぶん部](https://meganii.com//blog/2016/02/06/d3js-tutorial/)で、一通りD3.jsのイメージを掴みつつ、次は、東京の地価データの可視化に挑戦する。方法については、下記のページを参考にした。

[Ars longa, vita brevis: 東京の地価公示データを眺める](http://kshigeru.blogspot.jp/2013/07/tokyo-landprice.html)



## 環境準備

[D3.js と TopoJSON で地図を作る](http://ja.d3js.node.ws/blocks/mike/map/)を元に、環境を準備する。


### Geospatial Data Abstraction Library （地理空間データ抽出ライブラリ）のインストール

```
brew install gdal
```


## データを取得する

地価公示データは、以下のページからダウンロードする。
[国土数値情報　地価公示データの詳細](http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-L01-v2_3.html)

今回は、`L01-15_13_GML.zip`をダウンロードし、解凍すると以下のファイル

```
KS-META-L01-15_13.xml  L01-15_13.dbf  L01-15_13.prj  L01-15_13.shp  L01-15_13.shx  L01-15_13.xml
```



## orginfoで中身を確認する

```
ogrinfo -al L01-15_13.shp | head -n 8
INFO: Open of `L01-15_13.shp'
      using driver `ESRI Shapefile' successful.

Layer name: L01-15_13
Geometry: Point
Feature Count: 2162
Extent: (139.136421, 27.094612) - (142.203304, 35.828359)
Layer SRS WKT:
```

```
ogrinfo -sql "SELECT L01_006, L01_019 FROM 'L01-15_13'" L01-15_13.shp
```

例えばこんな以下のような形で取得できる。

```
OGRFeature(L01-15_13):2122
  L01_006 (String) = 273000
  L01_019 (String) = 東京都　江戸川区西瑞江５丁目１４番４６
  POINT (139.878173 35.67957)
```  

> 次に、行政区域コード (L01_017) で制限をかけます。 東京都 (都道府県コードは13) の場合、 13101 から23区が始まり、13201 から市が始まり、13301 から村が始まります。 離島は 13320 より大きいものになります。 したがって、島嶼部を除くためには行政区域コードが 13320 より小さいものを指定します。 コード体系の詳細は Wikipedia の 全国地方公共団体コード を参照してください。

whereで抽出しながら、GeoJSON形式に変換して、geojsonファイルに書き出す。

```
ogr2ogr -f GeoJSON -where "L01_017 < '13320'" tokyo-landprice-2015.geojson L01-15_13.shp
```



## d3.jsで表示する

<p><a href="https://www.flickr.com/photos/35571855@N06/24844125586" title="tokyo-landprice_heatmapby meganii, on Flickr"><img class="img-responsive" src="https://farm2.staticflickr.com/1680/24844125586_c74f952e38_z.jpg" alt="tokyo-landprice_heatmap"></a></p>


```
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>Tokyoの地価</title>
    <style>
    </style>
    <script src="//d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <script src="http://d3js.org/topojson.v0.min.js"></script>
  </head>
  <body>
    <div id="main"></div>
    <script type="text/javascript">

      var width = 960,
          height = 600;

      var g = d3.select('#main').append('svg')
                    .attr('width', width)
                    .attr('height', height)
                    .append('g');

      d3.json("tokyo-landprice-2015.geojson", function(err, tokyo) {
        if (err) {
          console.log("file not found.");
          return;
        }

        var projection = d3.geo.mercator()
                                .scale(60000)
                                .center(d3.geo.centroid(tokyo))
                                .translate([width / 2, height /2]);

        var path = d3.geo.path().projection(projection);

        g.selectAll("path")
            .data(tokyo.features)
            .enter()
            .append("path")
            .attr("d", path)
            .style("fill", function(tokyo) {
              if (tokyo.properties.L01_006 > 1000000) {
                return "#ff0000";
              } else if (tokyo.properties.L01_006 <= 1000000 && tokyo.properties.L01_006 > 800000) {
                return "#ff6600"
              } else if (tokyo.properties.L01_006 <= 800000 && tokyo.properties.L01_006 > 500000) {
                return "#ff9900"
              } else if (tokyo.properties.L01_006 <= 500000 && tokyo.properties.L01_006 > 200000) {
                return "#ffcc00"
              } else if (tokyo.properties.L01_006 <= 200000 && tokyo.properties.L01_006 > 100000) {
                return "green"
              } else {
                return "blue";
              }
            });
      });

    </script>
  </body>
</html>

```


## 次にやりたいこと

- 数十年分のデータを次々に描画して移り変わりを確認する
- 地図上にマッピングする


## 参考
- [D3.js - Data-Driven Documents](https://d3js.org/)
- [国土数値情報　地価公示データの詳細](http://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-L01-v2_3.html)
- [Ars longa, vita brevis: D3.js と GeoJSON でポリゴンを描く](http://kshigeru.blogspot.jp/2013/03/d3-geojson-polygon.html)
- [Ars longa, vita brevis: 東京の地価公示データを眺める](http://kshigeru.blogspot.jp/2013/07/tokyo-landprice.html)
