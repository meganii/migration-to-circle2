---

title: "Jekyllにタグクラウドを実装する"
date: 2014-12-01T07:46:00+09:00
comments: true
category: ['Tech']
tags: ['jekyll']
published: true 
slug: jekyll-tag-cloud
---



タグクラウドが欲しくなったので、以下のページを参考にタグクラウドタグを実装した。

<a href="http://www.catrio.net/article/develop-jekyll-tag-cloud-plugin.html" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://www.catrio.net/article/develop-jekyll-tag-cloud-plugin.html" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://www.catrio.net/article/develop-jekyll-tag-cloud-plugin.html" target="_blank">Jekyllのタグクラウドプラグインを開発する</a><a href="http://b.hatena.ne.jp/entry/http://www.catrio.net/article/develop-jekyll-tag-cloud-plugin.html" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://www.catrio.net/article/develop-jekyll-tag-cloud-plugin.html" alt="" /></a><br style="clear:both;" /><br>



{{% googleadsense %}}

### tag_generator.rb

```ruby
module Jekyll

  class TagPage < Page
    def initialize(site, base, dir, tag)
      @site = site
      @base = base
      @dir = dir
      @name = 'index.html'

      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'tag_index.html')
      self.data['tag'] = tag

      tag_title_prefix = 'Tag: '
      self.data['title'] = "#{tag_title_prefix}#{tag}"
    end
  end

  
  class TagPageGenerator < Generator
    safe true

    def generate(site)
      if site.layouts.key? 'tag_index'
        dir = site.config['tag_path'] || 'tag'
        site.tags.keys.each do |tag|
          site.pages << TagPage.new(site, site.source, File.join(dir, tag), tag)
        end
      end
    end
  end


end

```

### tag_index.html


```
---

---

{% raw %}{% assign posts = site.tags[page.tag] %}{% endraw %}

<h1>Tag: {{page.tag}}</h1>

<ul class="posts">
{% raw %}{% for post in posts %}{% endraw %}
  <li>
    <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
    <a href="{{ post.url }}" class="post-link">{{ post.title }}</a>
    <p>{{ post.content | strip_html | strip_newlines | truncate: 100 }}</p>
  </li>
{% raw %}{% endfor %}{% endraw %}
</ul>

```

### tagcloud.rb

```ruby
module Jekyll
  class TagCloud < Liquid::Tag

    def initialize(tag_name, text, tokens)
      super
    end

    def render(context)
      tag_array = []
      site = context.registers[:site]
      site.tags.each do |tag, tag_pages|
        tag_array << tag
      end
      tag_array.sort!

      tagcloud = ""
      tag_array.each do |tag|
        tagcloud << "<span><a href='#{site.baseurl}/blog/tag/#{tag}/'>#{tag}</a></span>\n"
      end
      "#{tagcloud}"
    end
  end
end

Liquid::Template.register_tag('tag_cloud', Jekyll::TagCloud)

```


### 利用箇所

```
{% raw %}{% tag_cloud %}{% endraw %}
```


## TODO

このままだと、タグがそのまま羅列されているだけなので、カテゴリ別に出力するように変更する。





