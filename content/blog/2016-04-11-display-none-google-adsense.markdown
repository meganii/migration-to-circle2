---
title: "Adsense広告をレスポンシブデザインでPCビュー2つ横並び、モバイル1つにする方法"
date: 2016-04-11T23:28:02+09:00
comments: true
category: ['Tech']
tags: ['Adsense','Web Design']
published: true
slug: display-none-google-adsense
img: "https://images-na.ssl-images-amazon.com/images/I/41AmQGGOU-L._SL160_.jpg"
---

Adsenseのレスポンシブ広告は、レスポンシブデザインの時に便利で使っているが、レクタングル広告を横に２つ並べた場合、モバイルで問題になることが多い。

どういうことかというと、PCで横に２つ並べた時、そのままのデザインでモバイルビューにすると縦に２つレクタングル広告が並ぶことにある。そうすると、画面全体が広告が広告で埋まってしまうことになり、Google Adsenseのポリシー違反になる。

では、どうすればいいか？


{{% googleadsense %}}

結論から言うと、

**「Adsenseのレスポンシブ広告を選択し、メディアクエリでモバイルの場合は、`display: none`で表示にする」** ことで対応できる可能性が高い。


気になる点は、以下のようにGoogleのポリシー違反にあたらないか、`display: none`で隠した広告は、１つの広告としてカウントされるのかといったところであろう。


## 気になる点・疑問点

1. `display: none`で広告コードを改変するのは、Google Adsenseのポリシー違反に当たらないか？
2. `display: none`でコンテンツを隠すのはGoogleのペナルティを受けないか？
3. Google Adsenseは１ページ当たり３つまでしか広告を表示できないが、`display: none`で非表示にした広告は１つとしてカウントされるのか？

１つ目のGoogle Adsenseのポリシー違反に当たらないか？という疑問に対しては、Google Adsenseのガイドラインを見ることで安心できる。

[レスポンシブ広告コードを修正する方法 - AdSense ヘルプ](https://support.google.com/adsense/answer/6307124#hide)


> 現在のレスポンシブ広告コードではご希望どおりの広告ユニットを作成できていない場合は、レスポンシブ サイトの要件を満たすように広告コードを修正してください。次の例に従うと、広告コードを正しく修正することができます。  

> 重要:

> - CSS メディアクエリのご使用や広告コードの変更の経験が初めての場合は、画面の幅ごとに正確な広告ユニットサイズを指定する場合の例を使って修正してください。
> - CSS メディアクエリのご使用や広告コードの変更に精通されている場合は、レスポンシブ広告コードの高度な機能の例を使って修正してください。

基本的に広告コードを変更することはNGだけど、レスポンシブ広告コードについては上記ページの指示に従う限り問題ないとの認識。




２つ目のGoogleのペナルティを受けないか？という疑問に対しては、まずGoogle公式のページに「隠しテキストと隠しリンク」について言及している箇所があるため、見てみる。




[隠しテキストと隠しリンク - Search Console ヘルプ](https://support.google.com/webmasters/answer/66353)

>Google の検索結果でのランキングを操作するためにコンテンツに隠しテキストや隠しリンクを含めることは、偽装行為と見なされることがあり、Google のウェブマスター向けガイドライン（品質に関するガイドライン）への違反にあたります。

> ただし、隠しテキストがすべて偽装行為と見なされるわけではありません。たとえば、サイトで JavaScript、画像、Flash ファイルといった検索エンジンにとってアクセスしにくい技術が使用されている場合、そのようなアイテムについて説明テキストを使用するとサイトのアクセシビリティが向上することがあります。また、スクリーン リーダー、モバイル ブラウザ、プラグインなしのブラウザ、低速接続環境でアクセスする多くの人間のユーザーもそのようなコンテンツを表示できないため、その場合も説明テキストがあれば役立ちます。サイトのアクセシビリティは、ブラウザで JavaScript、Flash、画像をオフにしたり、Lynx（リンク先は英語）などのテキスト ブラウザを使用したりすることで確認できます。

確かに、意図的にランキングを操作するために、隠しテキストとして大量のキーワードを埋め込んだりすることは違反になるが、PCとモバイルでデザインを変えることは問題ないと受け取ってもよいと(個人的には)読み取れる。


そのあたり、問題あるかないかについては、以下のページでも言及されているので目を通してみるとよい。

- [[SEO] レスポンシブWebデザインで display:none の利用はGoogleペナルティになりますか？ ::SEM R (#SEMR)](http://www.sem-r.com/seo/20121127114806.html)
- [display:noneを利用してテキストを非表示にするのはスパム？ | 正しいSEO相談室 | Web担当者Forum](http://web-tan.forum.impressrd.jp/e/2007/01/23/560)
- [『display:noneの利用 = 検索エンジンスパム』 ではない- Google Wysz ::SEM R (#SEMR)](http://www.sem-r.com/0702/20071012073357.html)


３つ目の`display: none`で非表示にした広告は１つとしてカウントされるのかという疑問に対しては、残念ながら、１つとしてカウントされてしまう。PCでも、モバイルでもAdsenseの広告枠３つを必ず出したいのであれば、PCとモバイルでビューを分けないといけないが、レスポンシブデザインからすると、本末転倒になってしまう。ここは、割り切りが必要かと思う。


## 参考

[【css】スマホ構築にも便利！displayの値オススメ5つ | Webマーケティング ブログ｜アドブログ](http://adgocoo.com/blog/smartphone/20150529-handy-css-display-kwus/)


<div class="booklink-box"><div class="booklink-image"><a href=http://www.amazon.co.jp/Google-AdSense-%E6%88%90%E5%8A%9F%E3%81%AE%E6%B3%95%E5%89%87-57-%E6%9F%93%E8%B0%B7/dp/4800710561%3FSubscriptionId%3DAKIAI6MZOKQQCKBKJBLQ%26tag%3Dmeganii-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4800710561><img src="https://images-na.ssl-images-amazon.com/images/I/51ekXX7wiUL._SL160_.jpg" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4800710561/meganii-22/">Google AdSense 成功の法則 57</a></div><div class=shoplinkrakuten><a href="http://hb.afl.rakuten.co.jp/hgc/g00q0725.il1o2897.g00q0725.il1o3b57/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F12855371%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Frms%2Fmsv%2FItem%3Fn%3D12855371%26surl%3Dbook">楽天で買う</a></div></div></div>

<div class="booklink-box"><div class="booklink-image"><a href=http://www.amazon.co.jp/%E3%83%96%E3%83%AD%E3%82%B0%E9%A3%AF-%E5%80%8B%E6%80%A7%E3%82%92%E5%8F%8E%E5%85%A5%E3%81%AB%E5%A4%89%E3%81%88%E3%82%8B%E7%94%9F%E3%81%8D%E6%96%B9-%E6%9F%93%E8%B0%B7-%E6%98%8C%E5%88%A9/dp/4844334166%3FSubscriptionId%3DAKIAI6MZOKQQCKBKJBLQ%26tag%3Dmeganii-22%26linkCode%3Dxm2%26camp%3D2025%26creative%3D165953%26creativeASIN%3D4844334166><img src="https://images-na.ssl-images-amazon.com/images/I/41AmQGGOU-L._SL160_.jpg" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/4844334166/meganii-22/">ブログ飯 個性を収入に変える生き方</a></div><div class=shoplinkrakuten><a href="http://hb.afl.rakuten.co.jp/hgc/g00q0725.il1o2897.g00q0725.il1o3b57/?pc=http%3A%2F%2Fbooks.rakuten.co.jp%2Frb%2F12350547%2F&m=http%3A%2F%2Fm.rakuten.co.jp%2Frms%2Fmsv%2FItem%3Fn%3D12350547%26surl%3Dbook">楽天で買う</a></div></div></div>
