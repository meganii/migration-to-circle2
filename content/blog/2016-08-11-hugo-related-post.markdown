---
title: "Hugoで関連記事を表示する方法"
date: 2016-08-11T13:54:52+09:00
comments: true
category: ['Tech']
tags: ['Python','Hugo']
published: true
slug: hugo-related-post
img: https://images-fe.ssl-images-amazon.com/images/I/51%2BfZJOKEKL._SL160_.jpg
---

静的サイトジェネレータを使っていて困るのは、関連記事の表示です。Jekyllのときもそうでしたが、Hugoにしてもこの悩みは同じでした。


Wordpressを利用していれば、関連記事プラグインで簡単に表示させることも可能ですが、静的サイトジェネレーターを利用した場合に「これがベスト」という方法がいまいちわかっていません。

私が考える方法には、以下の4つあります。

1. 手動で頑張る
2. Hugoテンプレート
3. JavaScript
4. Hugo DataFiles

<!--more-->
{{% googleadsense %}}

## 1. 手動で頑張る

なんといっても人(自分自身)が頑張って関連記事を選択して、手作業で関連記事を貼っていくので、正確にはなりそうですが、労力が掛かります。

デザインの変更にも強くありません。

## 2. Hugoテンプレート

Hugoのテンプレートを利用して、同じタグを持つページを関連記事として表示させるものです。(以下のように、Hugoのテンプレートを用いる)

```
{{ $page_link := .Permalink }}
{{ $tags := .Params.tags }}
{{ range .Site.Pages }}
{{ $page := . }}
{{ $has_common_tags := intersect $tags .Params.tags | len | lt 0 }}
  {{ if and $has_common_tags (ne $page_link $page.Permalink) }}
  <li><a href="{{ $page.Permalink }}">{{ $page.Title }}</a></li>
  {{ end }}
{{ end }}
```

タグを適切に運用して、割りきって使う分にはこの方法が一番楽です。ただし、タグを適切に運用しないと全然関係のない記事を「関連記事」として表示させてしまったり、タグのつけ忘れで表示できなかったりします。

## 3. JavaScript

例えば、[Zenback](https://zenback.jp/)のように、JavaScriptで関連記事を表示する方法です。

現在(2016/08/11現在)、このブログでは、人気記事の表示に[Ranklet](https://ranklet.com/)を利用しています。このWebサービスは、Google Analyticsのデータを利用して、JavaScriptで動的にDOMを書き換えるものです。

もしも自前で用意するのであれば、これらZenback, RankletのようにJavaScriptで制御することが可能です。(どのように実装すべきかはまた別の問題があります…)

ただし、せっかく静的サイトジェネレーターを利用して、静的なサイトを目指しているところに、JavaScriptで動的に書き換えるのはいかがなものかという疑問はあります。

## 4. Hugo DataFiles

Hugoには、DataFilesという機能があり、この機能を利用することで、自前でyamlなどを作成して、そのパラメータを呼び出すことができます。

DataFilesに、ある記事に対する関連記事の情報をあらかじめ書いておくことで、buildする際に、そのパラメータを利用して関連記事を表示させることができます。

静的ジェネレータのメリットを活かしつつ、関連記事を自動的に表示させることができるのでよさそうですが、どうやってパラメータファイルを作成するかが課題です。


## 今後の方針

現在は、「2. Hugoテンプレート」を利用していますが、「3. JavaScript」「4. Hugo DataFiles」の方法を実現させるためにも、機械的に関連記事を抽出する手段を確立することを目指します。

まずは、どのような手法・アルゴリズムがあるのかを調べてみます。
