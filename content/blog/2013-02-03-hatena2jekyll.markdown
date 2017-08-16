---

title: はてなダイアリーからJekyllへお引越し
date: 2013-02-03T10:47:00+09:00
category: ['Tech']
tags: ['jekyll']
published: true
slug: hatena2jekyll
---

### 前提
- Octpressを利用してます

#### 参考ページ
- <a href="http://tech.nitoyon.com/ja/blog/2012/09/20/moved-completed/" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://tech.nitoyon.com/ja/blog/2012/09/20/moved-completed/" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://tech.nitoyon.com/ja/blog/2012/09/20/moved-completed/" target="_blank">俺の最強ブログ システムが火を噴くぜ - てっく煮ブログ</a><a href="http://b.hatena.ne.jp/entry/http://tech.nitoyon.com/ja/blog/2012/09/20/moved-completed/" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://tech.nitoyon.com/ja/blog/2012/09/20/moved-completed/" alt="" /></a><br style="clear:both;" /><br>

- <a href="http://gosyujin.github.com/2012/11/12/from-hatena-to-jekyll/" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://gosyujin.github.com/2012/11/12/from-hatena-to-jekyll/" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://gosyujin.github.com/2012/11/12/from-hatena-to-jekyll/" target="_blank">はてなダイアリーのエントリをJekyllへ移行する</a><a href="http://b.hatena.ne.jp/entry/http://gosyujin.github.com/2012/11/12/from-hatena-to-jekyll/" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://gosyujin.github.com/2012/11/12/from-hatena-to-jekyll/" alt="" /></a><br style="clear:both;" /><br>


{{% googleadsense %}}

### 1. てっく煮ブログをローカルで動作させる
まずは、Jekyllの存在を知った　てっく煮ブログ　さんのブログがローカルで動かせるか試してみる。

```
git clone https://github.com/nitoyon/tech.nitoyon.com.git
cd tech.nitoyon.com
jekyll --server --auto
```


hparserのライブラリがないと怒られたので、`gem install hparser`を試す

```
gem install haprser
jekyll --server --auto
```

`http://localhost:4000/ja/blog/`　から正常に動いていることを確認。

### 2. はてなダイアリーのデータをMarkdownに変換
- 管理ページ > ブログのエクスポート > はてなの日記データ形式からブログのエクスポートをする。
- 取得したブログのデータを `tech.nitoyon.com/_scripts` にコピーする。
- `_script/`フォルダの直下に `_posts` と `_caches` ディレクトリを作る
- 以下のように `convert_hatena_to_jekyll_posts.rb`を実行して、はてなエントリからmarkdownに変換する

```
ruby convert_hatena_to_jekyll_posts.rb HATENA_ID はてなのエントリ.xml
```

上手く行けば、`_posts/` の中に変換された **.htn ファイルが格納される。

### 3. 変換した*.htn をJekyllでサイト生成
`jekyll`コマンドで変換した`*.htn`ファイルからサイトを生成する。

- `tech.nitoyon.com/_plagins`から `tags/`、`converters/`のディレクトリを自分のJekyllサイトの`_plagins`にコピー

しかし、amazonリンクが張ってあると、変換に失敗する。もし、amazonへのリンクがある場合は、Amazon APIのキーが必要になってくる。

- ここらへんを参考に、Amazon APIを取得する。[Access Key IDとSecret Access Keyの取得 - Amazon Web サービス](http://www.ajaxtower.jp/ecs/pre/index1.html)

- (エラーメッセージを頼りに)Amazonリンク生成のための準備(`gem install amazon-ecs`、 `_caches/amazon`の作成, _amazon.ymlの作成とか)


### 4. 変換完了!!
あとは、`jekyll --server --auto`  なり、`rake preview` (octpressの場合)なりで、確認すれば完了!!
先人の人達のお陰で、変換できました。ありがとうございます。


### 問題
- タグの扱いをどうするか
- シンタックスハイライトをどうするか

