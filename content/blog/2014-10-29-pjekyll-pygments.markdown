---

title: "JekyllでPygmentsを使ってのシンタックスハイライト"
date: 2014-10-29T23:15:00+09:00
comments: true
category: ['Tech']
tags: ['jekyll','blog']
published: true
slug: pjekyll-pygments
---

シンタックスハイライトに、Pygmentsを使いたくなったので変更する。



{{% googleadsense %}}

### 1.`pygments`をインストールする。

```bash
pip install pygments 
```

### 2. 以下のコマンドでcssを生成する。

```bash
pygmentize -a .highlight -S monokai -f html > css/monokai.css
```

### 3. Gemfileにpygmentsを追加

```
gem 'pygments.rb'
```

### 4. _config.ymlに、以下の記載を追加する。

```yaml
highlighter: pygments
```

### 5. デプロイする。



## こんなかんじになりました

```Ruby
def hoge
  puts "test"
end
```


## 参考
- [Pygments 利用ノート](http://www.geocities.jp/showa_yojyo/note/python-pygments.html)
- [Jekyll と pygments.rb で Auto-regeneration が遅い - Qiita](http://qiita.com/tachesimazzoca/items/e175035e2e8e5369029e)
- [ブログをGitHubに移行しました。 | blog.makitasako.com](http://blog.makitasako.com/posts/2013-04-13-makingmyblog/)
