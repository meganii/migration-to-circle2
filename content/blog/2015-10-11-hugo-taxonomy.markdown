---
title: "Hugoソースコードリーディング〜Taxonomy〜"
date: 2015-10-11T22:03:56+09:00
comments: true
category: ['Tech']
tags: ['hugo']
slug: hugo-taxonomy
published: true
img: "/images/hugo_s.png"
---

## 目的
Hugoにおける、categoryとtagの生成箇所を特定して、テーマ作成に役立てる。


## 用語確認
- Taxonomy 分類
- Term 'Taxonomy'に含まれるキー
- Value Termに割り当てられたコンテンツの一つ


{{% googleadsense %}}


## Taxonomy Templated
http://gohugo.io/taxonomies/templates/

taxonomiesを利用する場合、2つ方法がある。

1. list template
2. taxonomy terms template


### 1.list template

`list template`は、複数のsingle html pageのコンテンツを描画する際に利用されるテンプレート。
この`list template`は、自動的にすべてのtaxonomy pagesを作成する。

### 2.taxonomy terms template

`taxonomy terms template`は、それぞれに与えたテンプレートで、termsのリストを生成する。


Taxonomyは、map[string]WeightedPages

.Get(term)  
.Count(term)





###Channel とは

>- Channel は goroutine 間でのメッセージパッシングをするためのもの
- メッセージの型を指定できる
- first class value であり、引数や戻り値にも使える
- send/receive でブロックする
- buffer で、一度に扱えるメッセージ量を指定できる
http://jxck.hatenablog.com/entry/20130414/1365960707


>Channel の close()
close() は組み込みの関数で、用の済んだ channel を閉じることができます。
そもそも channel の呼び出しは 2 つの値が受け取れます。

`message, ok := <-channel`
この 2 つめの ok は、 channel が閉じられているかを表す bool。
ok は、取っても取らなくても良い仕様になっている。



## site.go

```golang:

layouts := s.appendThemeTemplates(
			[]string{"taxonomy/" + t.singular + ".html", "indexes/" + t.singular + ".html", "_default/taxonomy.html", "_default/list.html"})
```

### 利用しているテンプレート

- "taxonomy/" + t.singular + ".html"
- "indexes/" + t.singular + ".html
- "_default/taxonomy.html"
- "_default/list.html"



### RenderTaxonomiesLists

```
 func (s *Site) RenderTaxonomiesLists() error {

	for singular, plural := range taxonomies {
		for key, pages := range s.Taxonomies[plural] {
			fmt.Println(key, pages, singular, plural)
			taxes <- taxRenderInfo{key, pages, singular, plural}
		}
	}
```

### categoryの場合
- key: categoryのkey
- pages: どのページに含まれているか
- singular: category
- plural: category


### tagの場合
- key: tagのkey
- pages: そのtagのkeyが含まれているページの配列
- singular: tag
- plural: tags


### site.go renderAndWritePage
```:golang:site.go
func (s *Site) renderAndWritePage(name string, dest string, d interface{}, layouts ...string) error {
	renderBuffer := bp.GetBuffer()
	defer bp.PutBuffer(renderBuffer)

	err := s.render(name, d, renderBuffer, layouts...)

	outBuffer := bp.GetBuffer()
	defer bp.PutBuffer(outBuffer)

	transformLinks := transform.NewEmptyTransforms()

	if viper.GetBool("RelativeURLs") || viper.GetBool("CanonifyURLs") {
		transformLinks = append(transformLinks, transform.AbsURL)
	}

	if viper.GetBool("watch") && !viper.GetBool("DisableLiveReload") {
		transformLinks = append(transformLinks, transform.LiveReloadInject)
	}

	var path []byte

	if viper.GetBool("RelativeURLs") {
		translated, err := s.PageTarget().(target.OptionalTranslator).TranslateRelative(dest)
		if err != nil {
			return err
		}
		path = []byte(helpers.GetDottedRelativePath(translated))
	} else if viper.GetBool("CanonifyURLs") {
		s := viper.GetString("BaseURL")
		if !strings.HasSuffix(s, "/") {
			s += "/"
		}
		path = []byte(s)
	}

	transformer := transform.NewChain(transformLinks...)
	transformer.Apply(outBuffer, renderBuffer, path)

	if err == nil {
		if err = s.WriteDestPage(dest, outBuffer); err != nil {
			return err
		}
	}
	return err
}
```

### bpって？
bp "github.com/spf13/hugo/bufferpool"
おそらく出力する際に、バッファリングしているのでは？



## site.go

RenderPages()の中で、go pageRenderer(s, pages, results, wg)を実施。


newTaxonomyNodeで、すでにbaseが作られている。


```
func (s *Site) newTaxonomyNode(t taxRenderInfo) (*Node, string) {
	key := t.key
	n := s.NewNode()
	if s.Info.preserveTaxonomyNames {
		key = helpers.MakePathToLower(key)
		// keep as is, just make sure the first char is upper
		n.Title = helpers.FirstUpper(t.key)
	} else {
		n.Title = strings.Replace(strings.Title(t.key), "-", " ", -1)
	}

	base := t.plural + "/" + key
	s.setURLs(n, base)
	if len(t.pages) > 0 {
		n.Date = t.pages[0].Page.Date
		n.Lastmod = t.pages[0].Page.Lastmod
	}
	n.Data[t.singular] = t.pages
	n.Data["Singular"] = t.singular
	n.Data["Plural"] = t.plural
	n.Data["Pages"] = t.pages.Pages()
	return n, base
}
```


## 参考
- [Introduction to Hugo](http://gohugo.io/overview/introduction/)
- [spf13/hugo](https://github.com/spf13/hugo)
