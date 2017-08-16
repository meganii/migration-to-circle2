---

title: "Middlemanで静的サイト構築 -Middlemanで複数ブログを構築-"
date: 2015-05-10T09:05:00+09:00
comments: true
category: ['Tech']
tags: ['middleman']
published: true
slug: middleman-multiple-blogs
---

Middlemanで複数ブログを設定する際のメモ。



{{% googleadsense %}}




## Middleman
[Sass - Middleman を使ってブログを作る (心折られずに) - Qiita](http://qiita.com/5t111111/items/7a7600b463256f1d4122)

上記のサイトを見ながら、middleman-blog-bootstrap-templateを導入済み。



## 複数ブログの前提
### blogの名前
blog1, blog2は以下の2つを運用する。

- http://domain.com/blog1/posttitle/
- http://domain.com/blog2/posttitle/


### ディレクトリの構成
ディレクトリの構成は、`source`ディレクトリに`blog1`, `blog2`を作成する。
その配下に`posts`ディレクトリを作成し、ブログ記事を格納する。

```
source
├─blog1
　　├─posts
├─blog2
　　├─posts
```


## Middlemanで複数ブログ設定をするポイント

### ポイント1 name, prefixの設定

以下のブログ機能の設定を複数定義する。
そのとき、`name`,`prefix`を別々に定義する。

- name
- prefix

```ruby
active :blog do |blog|
end
```

上記の設定を複数定義すればよい。

> Middleman は 1 つのサイトの中で複数のブログを設置できます。1 つ以上のブログを作るには, 単に :blog 拡張を複数回有効化するだけです


#### config.rb
```ruby

## １つ目のブログ設定
activate :blog do |blog|
  blog.name = "blog1"
  blog.prefix = "blog1"

  blog.permalink = "{title}/index.html"
  blog.sources = "posts/{year}-{month}-{day}-{title}.html"
  blog.taglink = "tags/{tag}/index.html"
  blog.layout = "post"
  blog.year_link = "{year}/index.html"
  blog.month_link = "{year}/{month}/index.html"
  blog.day_link = "{year}/{month}/{day}/index.html"
  blog.default_extension = ".md"

  blog.tag_template = blog.prefix + "/tag.html"
  blog.calendar_template = blog.prefix + "/calendar.html"

  # Enable pagination
  blog.paginate = true
  blog.per_page = 10
end


## 2つ目のブログ設定
activate :blog do |blog|
  blog.name = "blog2"
  blog.prefix = "blog2"

  blog.permalink = "{title}/index.html"
  blog.sources = "posts/{year}-{month}-{day}-{title}.html"
  blog.taglink = "tags/{tag}/index.html"
  blog.layout = "post"
  blog.year_link = "{year}/index.html"
  blog.month_link = "{year}/{month}/index.html"
  blog.day_link = "{year}/{month}/{day}/index.html"
  blog.default_extension = ".md"

  blog.tag_template = blog.prefix + "/tag.html"
  blog.calendar_template = blog.prefix + "/calendar.html"

  # Enable pagination
  blog.paginate = true
  blog.per_page = 10
end
```

### ポイント2 blog_controller.nameを設定する

config.rbに、:blog拡張を複数回有効にした後、テンプレートのページや、タグページの中で、ブログ記事を取得している部分に、どちらのブログを取得するか指定する必要がある。以下のとおり、ヘルパーメソッドを修正していく。

```diff
- page_articles.each_with_index
+ page_articles(blog_controller.name).each_with_index 
```

```diff
- blog.tags.each do |tag, articles|
+ blog(blog_controller.name).tags.each do |tag, articles|
```

```diff
- tag_path(tag)
+ tag_path(tag, blog_controller.name)
```

```diff
- blog_year_path(year)
+ blog_year_path(year, blog_controller.name)
```

### ポイント3 Frontmatterに、`blog: blog_name`の設定を追加する

ブログ記事の読込の際は、`page_articles(blog_controller.name).each_with_index`で自動的に(階層から識別している？)対象のブログを読み込んでくれる。しかし、タグページや、カレンダーのページに記載しているものについては、上手く対象を読み込んでくれなかった。

そこで、`source`ディレクトリ直下においていた、`index.html.slim`, `calandar.html`と`tag.html`をblog1, blog2のディレクトリ直下にコピーして、Fontmatterにblogの識別子を記載することで解決した。

下記は、blog1の設定だけだが、blog2も同様に設定する。

#### index.html.slim
 
```ruby
---
pageable: true
per_page: 10
blog: blog1
---
h1 blog1
- page_articles(blog_controller.name).each_with_index do |article, i|
  h1
    = link_to article.title, article
  p
    - article.tags.each do |tag|
      small.label.label-default
        = tag
  hr
  p
    span.glyphicon.glyphicon-time
    |  Posted on 
    = article.date.strftime('%b %e')
  hr
  - if article.data.image_src
    img.img-responsive src=article.data.image_src
    hr
  = article.summary
  a.btn.btn-primary href=article.url
    | Read More
    span.glyphicon.glyphicon-chevron-right
  hr
- if paginate
  - if num_pages > 1
    .well-sm
      ul.pager
        - if page_number > 1
          li.previous
            = link_to '&larr;', prev_page
        span.text-center
          | Page 
          = page_number
          |  of 
          = num_pages
        - if page_number < num_pages
          li.next
            = link_to '&rarr;', next_page

```

#### calandar.html

```ruby
---
pageable: true
blog: blog1
--- 
h1
  | Archive for 
  - case page_type
  - when 'day'
    = Date.new(year, month, day).strftime('%b %e %Y')
  - when 'month'
    = Date.new(year, month, 1).strftime('%b %Y')
  - else
    = year
- if paginate && num_pages > 1
  p
    | Page 
    = page_number
    |  of 
    = num_pages
  - if prev_page
    p
      = link_to 'Previous page', prev_page
ul
  - page_articles(blog_controller.name).each_with_index do |article, i|
    h2
      = link_to article.title, article
    p
      - article.tags.each do |tag|
        small.label.label-default
          = tag
    hr
    p
      span.glyphicon.glyphicon-time
      |  Posted on 
      = article.date.strftime('%b %e')
    hr
    - if article.data.image_src
      img.img-responsive src=article.data.image_src
      hr
    = article.summary
    a.btn.btn-primary href=article.url
      | Read More
      span.glyphicon.glyphicon-chevron-right
    hr
- if paginate
  - if next_page
    p
      = link_to 'Next page', next_page

```


#### tag.html

```ruby
---
pageable: true
per_page: 12
blog: blog1
---
h1
  | Articles tagged '
  = tagname
  | '
- if paginate && num_pages > 1
  p
    | Page 
    = page_number
    |  of 
    = num_pages
  - if prev_page
    p
      = link_to 'Previous page', prev_page
ul
  - page_articles(blog_controller.name).each_with_index do |article, i|
    h2
      = link_to article.title, article
    p
      - article.tags.each do |tag|
        small.label.label-default
          = tag
    hr
    p
      span.glyphicon.glyphicon-time
      |  Posted on 
      = article.date.strftime('%b %e')
    hr
    - if article.data.image_src
      img.img-responsive src=article.data.image_src
      hr
    = article.summary
    a.btn.btn-primary href=article.url
      | Read More
      span.glyphicon.glyphicon-chevron-right
    hr
- if paginate
  - if next_page
    p
      = link_to 'Next page', next_page
```

## ハマった点

:blog拡張を複数有効にした後、試しに`bundle exec middleman`で確認する際に、以下のエラーメッセージに悩まされた。

```
You must either specify the blog name in calling this method or in your page frontmatter (using the 'blog' blog_name)
```

2つのblogを認識できてないため、識別子を指定しなければならないのだが、指定方法がなかなか分からなかった。指定方法については、ポイント2、ポイント3の記述で解決できた。





## 参考
- [Middleman: ブログ機能](https://middlemanapp.com/jp/basics/blogging/)
- [初めてのMiddleman：Middleman-blogでマルチブログを試してSkeletonを作った | Webデザイン、フロントエンド系の技術に関する備忘録 - whiskers](http://whiskers.nukos.kitchen/2015/03/04/middleman-multi-blog-skeleton.html)
