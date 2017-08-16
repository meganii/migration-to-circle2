---

title: "数世代バージョンを持つファイル名から最新版以外を抽出する"
date: 2015-03-27T23:54:00+09:00
comments: true
category: ['Tech']
tags: ['ruby']
published: true 
slug: leave-latest-filename
---

数世代バージョンを持っているようなファイルから、最新版だけ残す(2世代以上持っているものを抽出する)方法。


## 前提
ファイル名_yyyymmddという形式になっている。
あらかじめファイル名をソートしておく。

ファイルリスト。

```
TBTA1001_20140222
TBTA1001_20150520
TBTA1002_20151212
TBTA1002_20151222
TBTA1003_20140609
```


## スクリプト
```ruby
File.open('filename.txt') do |f|
  prev = ""
  f.each_line do |line|
    name = line.split(/_\d{8}/)
    if prev.split(/_\d{8}/) == name
      puts prev
    end
    prev = line
  end
end
```


## 結果
```
TBTA1001_20140222
TBTA1002_20151212
```

`sed`とか`awk`とか使ってさくっと出来ないものかと思ってるのだが・・・。
勉強不足。







