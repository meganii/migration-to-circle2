---
title: "JekyllからHugoへの移行ポイント"
date: "2015-08-30T11:56:00+09:00"
comments: true
category: ['Tech']
tags: ['jekyll','hugo']
published: true
slug: migration-jekyll-to-hugo
img: "/images/hugo_s.png"
---

Hugoが爆速であること、HugoがGolangで作られていて読みながら勉強したいという理由からJekyllからHugoに移行することにした。

基本的には、`_post`ディレクトリにあるものを、Hugoでいう`content/post`ディレクトリに配置すればよい。テーマを指定せずに、`hugo`としても何も出力されないのでそこは注意すること。

JekyllからHugoに移行する際にハマった点を残しておく。

{{% googleadsense %}}

## 日付フォーマットの変更

```yaml:2015-08-30-post.markdown
---
title: "タイトル"
date: "2015-08-29T17:13:12+09:00"
---
```

jekyll だと、`2015-08-30 10:30`で認識していたが、Hugoで読み取る日付フォーマットは、以下の通り。

- 2006-01-02T15:04:05Z07:00
- 2006-01-02T15:04:05
- Mon, 02 Jan 2006 15:04:05 -0700
- Mon, 02 Jan 2006 15:04:05 MST
- 02 Jan 06 15:04 -0700
- 02 Jan 06 15:04 MST
- Mon Jan _2 15:04:05 2006
- Mon Jan _2 15:04:05 MST 2006
- Mon Jan 02 15:04:05 -0700 2006
- 2006-01-02 15:04:05Z07:00
- 02 Jan 06 15:04 MST
- 2006-01-02
- 02 Jan 2006
- 2006-01-02 15:04:05 -07:00
- 2006-01-02 15:04:05 -0700

`hugo new`で作成されるのは、おそらく`2006-01-02T15:04:05Z07:00`の形式(実際には、2015-08-29T17:13:12+09:00のようになる)のため、この形式に変換する必要がある。

別に、作成したときの秒まで管理する必要はなく、年月日だけでよいのであれば、`2006-01-02`とかでよいだろう。


ワンライナーで、変更する。

```
find . -type f | xargs gsed -i -e 's/date: \([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}\) \([0-9]\{2\}:[0-9]\{2\}\).*$/date: \1T\2:00+09:00/g'
```


### 不要frontmatterの削除

`layout:`を削除する。

```
find . -type f | xargs gsed -i -e 's/layout:.*$//g'
```

### 日付をparseしている箇所

```golang:github.com/spf13/cast/caste.go
// StringToDate casts an empty interface to a time.Time.
func StringToDate(s string) (time.Time, error) {
	return parseDateWith(s, []string{
		time.RFC3339,
		"2006-01-02T15:04:05", // iso8601 without timezone
		time.RFC1123Z,
		time.RFC1123,
		time.RFC822Z,
		time.RFC822,
		time.ANSIC,
		time.UnixDate,
		time.RubyDate,
		"2006-01-02 15:04:05Z07:00",
		"02 Jan 06 15:04 MST",
		"2006-01-02",
		"02 Jan 2006",
		"2006-01-02 15:04:05 -07:00",
		"2006-01-02 15:04:05 -0700",
	})
}

func parseDateWith(s string, dates []string) (d time.Time, e error) {
	for _, dateType := range dates {
		if d, e = time.Parse(dateType, s); e == nil {
      fmt.Println(dateType)
			return
		}
	}
	return d, fmt.Errorf("Unable to parse date: %s", s)
}
```


[time - The Go Programming Language](http://golang.org/pkg/time/#pkg-constants)



## URLを決める

Jekyllのときは、`http://meganii.com/blog/2015/08/30/title/`のようなURL形式だったため、その形式に合わせる。

合わせ方は、config.ymlで定義する。

```yml:config.yml
---
baseurl: "http://meganii.com"
permalinks:
  post: "/blog/:year/:month/:day/:slug/"
---
```

```
permalinks:
  post: "/blog/:year/:month/:day/:slug/"
```

baseurlからみた、URL形式を`post:`で定義する。

`:slug`は、frontmatterで定義しないと使えないため、以下のように、各記事に`slug`を埋め込む。


```
---
title: "マーケティング22の法則を図解してみた"
date: "2015-08-29T17:13:12+09:00"
category: ['Book']
tags: ['book','マーケティング']
slug: marketing-22-raws
---
```

自分は、[Swiftで初めてのMacOSXアプリケーション-FFViewer- | じょーぶん部](http://meganii.com/blog/2015/07/04/building-cocoa-os-x-application-with-swfit-in-xcode/)で作成したソフトを利用して、frontmatterを埋め込んでいった。

ファイル名から判断して、slugを決めるようにした。


## テーマ Robustを利用する上で直したポイント

### Summaryにimgタグも含まれてしまう問題。

`\<!--more--\>`だと、それ以前の文言を全て、Summaryとして扱う。その結果、Summaryに、imgタグが含まれてしまうため、デザインが崩れてしまった。

記事に含まれる`<\!--more--\>`を全て削除した。

[Summaries](https://gohugo.io/content/summaries/)


### includeをshortcodeに変更

google adsenseなどをincludeしていたが、shortcodeに変更する。

```
layouts
└── shortcodes
    └── googleadsense.html
```




[Shortcodes](http://gohugo.io/extras/shortcodes/)



## ソースコードをインストール
Hugoでは、git, Mercurialが必要なためインストール

```
brew install mercurial
go get -v github.com/spf13/hugo
```

アップデートの場合は、以下のコマンドを実行するみたい。

```
go get -u -v github.com/spf13/hugo
```



## タグとカテゴリの関係

Taxonomyあたりが関係している。

```
taxonomies:
  tag: "tags"
  category: "category"
```

上記の指定をすることで、いわゆるタグと、カテゴリに使用する名称を定義する。ここでは、タグを`tags`、カテゴリを`category`とした。
(各記事のfrontmatterで利用している名称と一致させること)

http://gohugo.io/templates/terms/

tag,categoryのページを生成する際は、list.htmlが呼ばれる。


## gsedのインストール
Macのsedは、挙動が違うらしいので、`brew install gsed`でインストール



## 課題
- {% raw %}{% endraw %}が残っているため削除する
- categoryとtagsのページレイアウトが仮のため、作成する(おそらくlist.htmlをいじればよい)
- h2,h3に色を付けたい
- imgをつけていく。
- 広告をつけていく
- baseは、/blog/だから、categoryとtagsもそれに追随してほしい(直接hugoのソースをみてみる)
- デザインをフォークする


## 参考
- https://github.com/spf13/hugo
- [OctopressからHugoに移行した マルチコアをもっと使いTai - LT駆動開発12 | そんなこと覚えてない](http://blog.eiel.info/blog/2015/03/07/octopress-to-hugo/)
- [ブログをOctopressからHugoに移行した | Unresolved](http://yet.unresolved.xyz/blog/2015/01/04/migrate-blog-to-hugo-from-octopress/)
- [OctopressからHugoへ移行した | SOTA](http://deeeet.com/writing/2014/12/25/hugo/)
