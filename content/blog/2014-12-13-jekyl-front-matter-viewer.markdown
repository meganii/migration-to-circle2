---

title: "Jekyllのタグとカテゴリを整理するために、一覧表示するWebアプリ(個人用)をつくった"
date: 2014-12-13T18:15:00+09:00
comments: true
category: ['Tech']
tags: ['jekyll','ruby']
published: true
slug: jekyl-front-matter-viewer
img: "https://farm9.staticflickr.com/8650/16007934641_502fe07015_z.jpg"
---

カテゴリ名を一括変換したり、タグ名を整理する際に、今どうなっているか一覧にしたかったので、Railsで作ってみた。

無事一覧が出来たので気持ちいい。こういう庭いじり好きかも笑。

<p><a href="https://www.flickr.com/photos/35571855@N06/16007934641" title="JekyllFFViewer_and_posts_controller_rb____Work_Site_JekyllFFViewer_app_controllers__-_VIMby meganii, on Flickr"><img class="img-responsive" src="https://farm9.staticflickr.com/8650/16007934641_502fe07015_z.jpg" alt="JekyllFFViewer_and_posts_controller_rb____Work_Site_JekyllFFViewer_app_controllers__-_VIM"></a></p>

[https://github.com/meganii/JekyllFFviewer](https://github.com/meganii/JekyllFFviewer)



{{% googleadsense %}}


## Postsテーブル作成

`metadata`として、JekyllのFront Matterを格納する。

[Front Matter](http://jekyllrb.com/docs/frontmatter/)

### create_posts.rb

```ruby
require 'rubygems'
require 'sqlite3'

db = SQLite3::Database.new("/Users/meganii/Work/Site/JekyllFFViewer/db/development.sqlite3")
sql = <<SQL
CREATE TABLE Posts  (
id integer PRIMARY KEY AUTOINCREMENT,
filename String,
content Text,
metadata Text);
SQL
db.execute(sql)
db.close
```


## markdownの読込

Jekyllで利用しているMarkdownのファイルを読み込んで、SQLite3に入れる。

ActiveRecordを単品でも使えることがわかったので、利用する。

```ruby
class Post< ActiveRecord::Base
  serialize :metadata
end
```

配列やハッシュを上記のように、シリアライズすることで、読み込んだ際に、元のオブジェクト形式で読み込んでくれる。

[Rails4でserializeしてデータをDBに保存させる | EasyRamble](http://easyramble.com/rails-active-record-serialize.html)


YAML Front Matterと、記事本文を分離する正規表現は、以下参照。

[Jekyllのお勉強 -YAML部分と記事本文を分離する正規表現-](http://meganii.com/blog/2013/05/23/regexp-jekyll/)


### import_md.rb 
```ruby
require 'rubygems'
require 'active_record'
require 'english'

ActiveRecord::Base.establish_connection(
  "adapter" => "sqlite3",
  "database" => "/Users/meganii/Work/Site/JekyllFFViewer/db/development.sqlite3"
)

class Post< ActiveRecord::Base
  serialize :metadata
end

files = Dir.glob(File.join("/Users/meganii/Dropbox/Sites/meganii.com/_posts", "*"))

files.each do |f|
  ff = YAML.load_file(f)
  file = open(f)
  content = file.read

  if content =~ /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
    post_content = $POSTMATCH
  end

  filename = File.basename(f)
  unless filename =~ /~\z/
    post = Post.new
    post.filename = filename 
    post.metadata = ff
    post.content = post_content
    post.save
  end
end
```



## ソート

項目毎にソートされていた方が嬉しいので、ソート処理を実装してみる。

[Railsのテーブル並び替えを実装する | Scimpr Blog](http://blog.scimpr.com/2012/08/26/rails%E3%81%AE%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB%E4%B8%A6%E3%81%B3%E6%9B%BF%E3%81%88%E3%82%92%E5%AE%9F%E8%A3%85%E3%81%99%E3%82%8B/)

単純なソートであれば、取得時にソート処理をかませばよいのだが、今回は、ハッシュの配列を、あるキー値でソートしないといけないので注意が必要。





```ruby
  def index
    @posts = Post.all

    hash = []
    
    if params[:sort] != nil

      sortkey = params[:sort] 

      @posts.each do |post|
        hash << post.metadata
      end

      hash.each {|h| puts h }

      result = hash.sort {|a, b| compare(a[sortkey], b[sortkey]) }
      hash = result

    end


    a = []
    @posts.each do |post|
      data = post.metadata
      data.keys.each do |key|
        a << key
      end
    end
    @column = a.uniq.sort

    @posts = hash
  end


  def compare(a, b)
    return -1 unless b 
    return 1 unless a

    a = a[0] if a.instance_of? Array
    b = b[0] if b.instance_of? Array
    a <=> b
  end
```

## 今後・TODO

- 一覧上から修正して、再出力できるようにしたい
- 一括変換したい





