---

title: "Middleman getting start"
date: 2015-05-09T12:57:00+09:00
comments: true
category: ['Tech']
tags: ['middleman']
published: true
slug: middleman-getting-start
---

Middlemanでの構築メモ。


{{% googleadsense %}}


## MiddlemanにBlog機能を持たせる

素の状態のMiddlemanで`middleman init new_site`をしたときに、デザインがあまりにもアレだったので、心が折られてしまった。
そこで、以下の記事を参考に、最低限のデザインをもったサイトを構築する。
(何もない状態から、ガシガシ作っていけるひとはいいんだが、自分も心が折れました。。。)

[Sass - Middleman を使ってブログを作る (心折られずに) - Qiita](http://qiita.com/5t111111/items/7a7600b463256f1d4122)


```
gem install middleman
```

```
middleman init my_new_project --template=blog-bootstrap
```

```
cd my_new_project
bower install
bundle install
```

```
bundle exec middleman server
```

```
middleman init
```
