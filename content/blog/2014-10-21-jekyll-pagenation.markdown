---

title: "Jekyllでページ分割する -pagenation-"
date: 2014-10-21T07:37:00+09:00
comments: true
category: ['Tech']
tags: ['jekyll']
published: true 
slug: jekyll-pagenation
---

## Jekyllでやりたいこと
Jekyllを使っていて、トップページにすべての記事が出てくるのもうっとおしい。
トップページの表示記事を5〜10件にして、そのほかの記事を「次へ」、「戻る」で遷移させたい。


{{% googleadsense %}}

## 解決策

**ページネーションを利用する。**

### 1. _config.ymlに以下の文言を追加する

```
paginate: 10
```

何件で分割するかを pagenate に指定する。

### 2. index.htmlの site.posts としている部分を paginator.postsに変更する

```html
---

---

<div class="home">
  <h1>Posts</h1>

  <ul class="posts">
    {{ "{% for post in paginator.posts " }}%}
    <li>
      <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
      <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      {{ "{% for tag in post.tags " }}%}
      <a href="/blog/tag/{{tag}}">{{ tag }}</a>
      {{ "{% endfor " }}%}
      {% raw %}<p>{% if post.description %}{{ post.description }}{% else %}{{ post.content | strip_html | strip_newlines | truncate: 120 }}{% endif %}</p>{% endraw %}
    </li>
    {{ "{% endfor " }}%}
  </ul>


  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>
```


## 覚えたliquidタグ

### for文の中でのカウンタ

`forloop.index`

### liquidタグのエスケープ

- `{{ "{% raw " }}%}{{ "{% endraw " }}%}`
- rowタグそのもののエスケープには、｛｛ ", " ｝｝を利用する (利用する際は、全角を半角に変換してください)

liquidタグを含んだhtmlをシンタックスハイライトを効かせるには、以下のとおり、rawタグで括る

```
{{ "{% raw %" }}}
liquidタグを含むHTML
{{ "{% endraw %" }}}
```


## 参考
<a href="http://jekyllrb-ja.github.io/docs/pagination/#section" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://jekyllrb-ja.github.io/docs/pagination/#section" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://jekyllrb-ja.github.io/docs/pagination/#section" target="_blank">ページネーション</a><a href="http://b.hatena.ne.jp/entry/http://jekyllrb-ja.github.io/docs/pagination/#section" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://jekyllrb-ja.github.io/docs/pagination/#section" alt="" /></a><br style="clear:both;" /><br>

