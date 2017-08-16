---

title: "Swiftで初めてのMacOSXアプリケーション-FFViewer-"
date: 2015-07-04T18:23:00+09:00
comments: true
category: ['Tech']
tags: ['Swift','Cocoa','Xcode']
published: true 
img: "https://c4.staticflickr.com/4/3877/19396261452_c2ec154bfd_n.jpg" 
slug: building-cocoa-os-x-application-with-swfit-in-xcode
---


<p><a href="https://www.flickr.com/photos/35571855@N06/19396261452" title="swift_applicationby meganii, on Flickr"><img class="img-responsive" src="https://farm4.staticflickr.com/3877/19396261452_c2ec154bfd_z.jpg" alt="swift_application"></a></p>


## つくりたいもの

JekyllのPost用として書いたMarkdownのFrontFormatterの情報を読み込んで表示し、編集、再出力ができるツール。


WebアプリケーションとしてViewerまでは作ったけど、編集まで考えるとなかなかめんどくさいので活用できなかった。(今どんな情報を書いていたのかは把握出来たが)

[Jekyllのタグとカテゴリを整理するために、一覧表示するWebアプリ(個人用)をつくった](http://meganii.com/blog/2014/12/13/jekyl-front-matter-viewer/)

Objective-Cは、ちょっと触りたくなかったが、SwiftでMacアプリケーションも作成できるらしいので試しにつくってみた。



{{% googleadsense %}}


## 作ったもの

<p><a href="https://www.flickr.com/photos/35571855@N06/19015646869" title="FFViewerby meganii, on Flickr"><img class="img-responsive" src="https://farm1.staticflickr.com/351/19015646869_6032c17a1e_z.jpg" alt="FFViewer"></a></p>

[meganii/FFViewer](https://github.com/meganii/FFViewer)


## 前提

- Xcode Version 6.4 (6E35b)
- Swift1.2 

重い腰をあげて、Yosemiteにアップグレードした。


## ハマった点

- Xcodeが分からない
- Swiftの文法が分からない
- tableViewの実装の仕方が分からない


## 正規表現

```
let pattern = "---"
let regex = NSRegularExpression(pattern: pattern, options: NSRegularExpressionOptions.CaseInsensitive, error: nil)


let regex = NSRegularExpression(pattern: pattern, options: NSRegularExpressionOptions.CaseInsensitive, error: nil)
var matches=regex?.matchesInString(content, options: nil, range:NSMakeRange(0,  content.length)) as Array<NSTextCheckingResult>

```

## tableViewの実装

- `optional func numberOfRowsInTableView(_ aTableView: NSTableView) -> Int`
- `optional func tableView(_ aTableView: NSTableView, objectValueForTableColumn aTableColumn: NSTableColumn?, row rowIndex: Int) -> AnyObject?`

tableViewを利用する際に、必ず実装しないといけないのが、上記２つの関数である。

[SwiftでOS Xアプリケーションのプログラミング - 表](http://www.ne.jp/asahi/room/kuro/programmingTable.html)




## tableViewのソート処理

<p><a href="https://www.flickr.com/photos/35571855@N06/19006621158" title="Swift-TableView-Sortby meganii, on Flickr"><img class="img-responsive" src="https://farm1.staticflickr.com/488/19006621158_ec8b60f0ac_z.jpg" alt="Swift-TableView-Sort"></a></p>


- Xcode側で、紐付けをしておく

`tableView(tableView: NSTableView, sortDescriptorsDidChange oldDescriptors: [AnyObject])`を実装すると、ヘッダ部分をクリックしたときにこの関数が呼ばれる。


sortDescriptorに、降順か昇順かが入っているのでそれをみて判断する。

```
    func tableView(tableView: NSTableView,
        sortDescriptorsDidChange oldDescriptors: [AnyObject])  {
            for sortDescriptor in tableView.sortDescriptors.reverse() as! [NSSortDescriptor] {
                var key = sortDescriptor.key() as String!
                if sortDescriptor.ascending {
                    data.sort {(item1, item2) in return item1.prop[key] < item2.prop[key]}
                } else {
                    data.sort {(item1, item2) in return item1.prop[key] > item2.prop[key]}
                }
            }
        tableView.reloadData()
    }
```

## 今後実装したい

- カテゴリ、タグの置換機能
- 記事の中身の簡易編集
- カテゴリ、タグのフィルター機能
