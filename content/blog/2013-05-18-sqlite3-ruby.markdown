---
title: sqlite3-rubyを使ってSQLite3ファイルからの検索結果をHashとして読み込む
date: 2013-05-18T12:06:00+09:00
category: ['Tech']
tags: ['ruby','sqlite3']
published: true
slug: sqlite3-ruby
---

sqlite3-rubyを使って、SQLite3にアクセスしてデータの取得、加工がしたい。

db.executeした際に配列が帰ってきた。カラム名でアクセス出来る方法がないか探したところ、
results_as_hash = trueにすれば、Hashで返ってくることがわかった。


{{% googleadsense %}}

[SQLite3/Ruby FAQ](http://sqlite-ruby.rubyforge.org/sqlite3/faq.html)

##I’d like the rows to be indexible by column name.
>By default, each row from a query is returned as an Array of values. This means that you can only obtain values by their index. Sometimes, however, you would like to obtain values by their column name.

>The first way to do this is to set the Database property “results_as_hash” to true. If you do this, then all rows will be returned as Hash objects, with the column names as the keys. (In this case, the “fields” property is unavailable on the row, although the “types” property remains.)

デフォルトだと配列で返ってくるので、results_as_hashをtrueにすれば、ハッシュとして返却され、カラム名でアクセスできる。

```
  db.results_as_hash = true
  db.execute( "select * from table" ) do |row|
    p row['column1']
    p row['column2']
  end
```

>The other way is to use Ara Howard’s ArrayFields module. Just require “arrayfields”, and all of your rows will be indexable by column name, even though they are still arrays!

```
  require 'arrayfields'

  ...
  db.execute( "select * from table" ) do |row|
    p row[0] == row['column1']
    p row[1] == row['column2']
  end

```


## sqlite3ファイルから読み込み
```
require 'rubygems'
require 'sqlite3'

db = SQLite3::Database.new("development.sqlite3")
db.results_as_hash = true

sql = "select * from entries"

db.execute(sql) do |row|
	p row
end
```

## 参考
- [ruby - Add a new line in file? - Stack Overflow](http://stackoverflow.com/questions/3518329/add-a-new-line-in-file)
