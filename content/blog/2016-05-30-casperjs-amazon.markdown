---
title: "CasperJSでAmazonログイン"
date: 2016-05-30T07:04:55+09:00
comments: true
category: ['Tech']
tags: ['CasparJS']
published: true
slug: casperjs-amazon
---

CasperJSで、Amazonに自動ログインするサンプル。PhantomJSを直接触るよりは書きやすい.

<!--more-->
{{% googleadsense %}}


```
var casper = require("casper").create({
  verbose: true,
  logLevel: 'debug',
  pageSettings: {
       loadImages:  false,         // The WebPage instance used by Casper will
       loadPlugins: false,         // use these settings
       userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)'
  }
});

casper.start("https://affiliate.amazon.co.jp/", function () {
    this.fillSelectors("#identitybox > div > form", {
        "input[name='username']": "AMAZON_ID",
        "input[name='password']": "AMAZON_PW"
    }, true);
    this.click('#signin > input[type="image"]');
});

casper.then(function() {
  console.log(this.evaluate(function() {
    return document.querySelector('#mini-report > div.line-item-total > div.data').textContent;
  }));
});
```

## 参考

[Casper.JSのススメ - yuukigoodman blog](http://blog.yuukigoodman.net/entry/2013/08/17/005440)
