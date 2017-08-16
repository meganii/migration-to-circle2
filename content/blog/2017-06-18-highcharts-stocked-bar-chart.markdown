---
title: "Highchartsを使って財務諸表(BS/PL)のグラフを出力する"
date: 2017-06-18T14:49:27+09:00
lastmod: 2017-06-18T14:49:27+09:00
comments: true
category: ['Tech']
tags: ['highcharts','visualization']
published: true
slug: highcharts-stocked-bar-chart
img: /images/2017/06/BS_PL-64x.png
---

<script async src="//jsfiddle.net/meganii/wdppph94/4/embed/result/"></script>

<!--more-->
{{% googleadsense %}}

## plotOptions

`pointPadding: 0`に指定することで、group内での間隔を0にできる。

```
  plotOptions: {
      column: {
          stacking: 'normal',
      },
      series: {
          pointPadding: 0,
          borderWidth: 0,
          shadow: false,
      }
  },
```

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Balance Sheets</title>
  </head>
  <body>
    <div id="container" style="width:100%; height:560px;"></div>
    <script src="http://code.highcharts.com/highcharts.js"></script>
    <script>
      // create a new chart
      new Highcharts.chart('container', {
        chart: {
            type: 'column'

        },

        title: {
            text: '会社名'
        },

        xAxis: {
            categories: ['Balance Sheets', 'Income Statement']
        },

        yAxis: {
            allowDecimals: false,
            min: 0,
            title: {
                text: 'Yen'
            }
        },

        tooltip: {
            formatter: function () {
                return '<b>' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y;
            }
        },

        plotOptions: {
            column: {
                stacking: 'normal',
            },
            series: {
                pointPadding: 0,
                borderWidth: 0,
                shadow: false,
            }
        },

        series: [{
            name: '現金預金等',
            data: [1169409, null],
            stack: 'Credit'
        }, {
            name: '売掛金',
            data: [46840, null],
            stack: 'Credit'
        }, {
            name: '棚卸資産',
            data: [2627138, null],
            stack: 'Credit'
        }, {
            name: 'その他流動資産',
            data: [405844, null],
            stack: 'Credit'
        }, {
            name: '有形固定資産',
            data: [17990, null],
            stack: 'Credit'
        }, {
            name: '無形固定資産',
            data: [49806, null],
            stack: 'Credit'
        }, {
            name: 'その他固定資産',
            data: [19854, null],
            stack: 'Credit'
        }, {
            name: '買掛金',
            data: [4372, null],
            stack: 'Dedit'
        }, {
            name: '有利子負債',
            data: [521575, null],
            stack: 'Dedit'
        }, {
            name: 'その他流動負債',
            data: [864756, null],
            stack: 'Dedit'
        }, {
            name: 'その他固定負債',
            data: [0, null],
            stack: 'Dedit'
        }, {
            name: '純資産',
            data: [2950550, null],
            stack: 'Dedit'
        }, {
            name: '営業原価',
            data: [null, 4596029],
            stack: 'Credit'
        }, {
            name: '販管費',
            data: [null, 710028],
            stack: 'Credit'
        }, {
            name: '営業利益',
            data: [null, 1027949],
            stack: 'Credit'
        }, {
            name: '売上',
            data: [null, 6334008],
            stack: 'Dedit'
        }],
      });
    </script>
  </body>
</html>

```

## 参考

- [Interactive JavaScript charts for your webpage \| Highcharts](https://www.highcharts.com/)
- [JSのグラフライブラリを今選ぶならHighchartsで決まり \- Qiita](http://qiita.com/grgrjnjn/items/fa39778657493008c3b6)
- http://jsfiddle.net/2pVkd/2/
- http://jsfiddle.net/2pVkd/4/
