---

title: XPathでの属性値の取得
date: 2014-02-19T22:09:00+09:00
category: ['Tech']
tags: ['xpath']
published: true
slug: xpath-java
---

知っててよかったXPath。
XMLのノードを特定するときに使う。

## XPath使い方
```java
XPath xpath = XPathFactory.newInstance().newXPath();
String expression = "/widgets/widget";
InputSource inputSource = new InputSource("widgets.xml");
NodeList nodes = (NodeList) xpath.evaluate(expression, inputSource, XPathConstants.NODESET);
```

## ルートノードの選択
```
html
```


## 属性値の取得方法
```
//html/body/hoge[@id='test']
```

id属性が'test'のhogeノードを取得する


## 参考
- [XML/XPath/XPathの書き方 - 俺の基地](http://yakinikunotare.boo.jp/orebase/index.php?XML%2FXPath%2FXPath%A4%CE%BD%F1%A4%AD%CA%FD)
- [javax.xml.xpath (Java Platform SE 6)](http://docs.oracle.com/javase/jp/6/api/javax/xml/xpath/package-summary.html)
