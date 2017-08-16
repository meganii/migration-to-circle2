---
title: "NetlifyでServer Pushを利用する"
date: 2017-07-23T08:19:02+09:00
lastmod: 2017-07-23T08:19:02+09:00
comments: true
category: ['Tech']
tags: ['Netlify','HTTP/2']
published: true
slug: http2-server-push-on-netlify
img: https://farm5.staticflickr.com/4296/35297674803_dd5bd37b56_t.jpg
---

いつのまにかNetlifyでServer Pushができるようになったようです。このアナウンスに伴い、今までFreeアカウントでは利用できなかった`_headers`ファイルが有効になっています。

[HTTP/2 Server Push on Netlify \| Netlify](https://www.netlify.com/blog/2017/07/18/http/2-server-push-on-netlify/)


HTTP/2, Server Pushの詳細を理解しているわけではないので詳しくは説明できないのですが、Server Pushにより1回分の通信を節約でき、レンダリングブロックとなるCSSのクリティカルパスを解消できるとの理解です。

HTTP/2については[@kazuho](https://twitter.com/kazuho)さんのスライドが超絶参考になります。

- [HTTP/2時代のウェブサイト設計](https://www.slideshare.net/kazuho/http2-51888328)
- [HTTP/2の課題と将来](https://www.slideshare.net/kazuho/http2-70006550)

<!--more-->
{{% googleadsense %}}

## 設定方法

Hugoであれば、`static`フォルダに`_headers`ファイルを作成します。

`_headers`の記述方法は下記ドキュメントを参照し、Server Pushのためのルールを記述します。例えば、CSSとJavaScriptのServer Pushを行う際は、以下の通り設定します。

[Headers & Basic Authentication \| Netlify](https://www.netlify.com/docs/headers-and-basic-auth/#multi-key-header-rules)

```_headers
/*
  Link: </css/normalize.css>; rel=preload; as=style
  Link: </css/skeleton.css>; rel=preload; as=style
  Link: </css/custom.css>; rel=preload; as=style
  Link: </css/share.css>; rel=preload; as=style
  Link: </css/font-awesome.min.css>; rel=preload; as=style
  Link: </css/highlight-default-color.css>; rel=preload; as=style
  Link: </js/highlight.pack.js>; rel=preload; as=script
```

元々以下のcss,jsを外部リンクとして読み込んでいたのですが、せっかくServer Pushできるのであれば自サイトからロードさせたいため、ダウンロードしてNetlifyからServer Pushで配布するように変更しました。

- highlight.js
- font-awesome
- googlefonts

また、Google Fontsは利用頻度も低かったのでこれを機会に廃止しました。


## Before / After

Server Pushの変更前と変更後で、何が変わるのかをChromeのDeveloper Toolsで確認します。

### Before

変更前は下図の通り、`Initiator`の部分が`Other` もしくは`Perser`となっています。この計測時は、font-awesomeとgoogle fontsに気なる遅延は発生していませんでしたが、たまにレスポンスが著しく悪くなるときがあります。これを機会にNetlifyからホストするように変更します。

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/35571855@N06/35972414491/in/dateposted-public/" title="before"><img src="https://farm5.staticflickr.com/4295/35972414491_dd380e5672_z.jpg" width="640" height="458" alt="before"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/35571855@N06/35972549391/in/dateposted-public/" title="before_detail"><img src="https://farm5.staticflickr.com/4302/35972549391_d9676f6101_c.jpg" width="800" height="291" alt="before_detail"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>



### After

`Initiator`の部分が、`Push / Other`に変わりました。font-awesomもServer Pushしてることがわかります。

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/35571855@N06/35715193240/in/dateposted-public/" title="after"><img src="https://farm5.staticflickr.com/4320/35715193240_05231256c9_z.jpg" width="640" height="458" alt="after"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

<a data-flickr-embed="true"  href="https://www.flickr.com/photos/35571855@N06/35297674803/in/dateposted-public/" title="after_detail"><img src="https://farm5.staticflickr.com/4296/35297674803_dd5bd37b56_c.jpg" width="800" height="324" alt="after_detail"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>


## 参考
- [HTTP/2 Server Push on Netlify \| Netlify](https://www.netlify.com/blog/2017/07/18/http/2-server-push-on-netlify/)
- [A Comprehensive Guide To HTTP/2 Server Push — Smashing Magazine](https://next.smashingmagazine.com/2017/04/guide-http2-server-push/)
- [Announcing Support for HTTP/2 Server Push](https://blog.cloudflare.com/announcing-support-for-http-2-server-push-2/)
