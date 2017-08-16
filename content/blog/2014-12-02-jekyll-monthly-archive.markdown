---

title: "Jekyllに月別アーカイブを実装する"
date: 2014-12-02T07:54:00+09:00
comments: true
category: ['Tech']
tags: ['jekyll']
published: true
slug: jekyll-monthly-archive
---



以下のページを参考に、月別アーカイブを実装した。

## 参考
[Octopress - 月別アーカイブ！ - mk-mode BLOG](http://www.mk-mode.com/octopress/2013/02/15/octopress-monthly-archives/)

[shigeya/jekyll-monthly-archive-plugin](https://github.com/shigeya/jekyll-monthly-archive-plugin)

## 用途
- monthly_archive_plugin.rb 月別アーカイブページを生成
- monthly_archive.html 月別アーカイブページのレイアウト
- monthly_archive.rb 月別アーカイブの出力カスタムタグ



{{% googleadsense %}}

### monthly_archive_plugin.rb

```Ruby
module Jekyll

  module MonthlyArchiveUtil
    def self.archive_base(site)
      site.config['monthly_archive'] && site.config['monthly_archive']['path'] || '/blog'
    end
  end

  # Generator class invoked from Jekyll
  class MonthlyArchiveGenerator < Generator
    def generate(site)
      posts_group_by_year_and_month(site).each do |ym, list|
        site.pages << MonthlyArchivePage.new(site, MonthlyArchiveUtil.archive_base(site),
                                             ym[0], ym[1], list)
      end
    end

    def posts_group_by_year_and_month(site)
      site.posts.each.group_by { |post| [post.date.year, post.date.month] }
    end

  end

  # Actual page instances
  class MonthlyArchivePage < Page

    ATTRIBUTES_FOR_LIQUID = %w[
      year,
      month,
      date,
      content
    ]

    def initialize(site, dir, year, month, posts)
      @site = site
      @dir = dir
      @year = year
      @month = month
      @archive_dir_name = '%04d/%02d' % [year, month]
      @date = Date.new(@year, @month)
      @layout =  site.config['monthly_archive'] && site.config['monthly_archive']['layout'] || 'monthly_archive'
      self.ext = '.html'
      self.basename = 'index'
      self.content = <<-EOS
{% for post in page.posts %}<li><a href="{{ post.url }}"><span>{{ post.title }}</span></a></li>
{% endfor %}
      EOS
      self.data = {
          'layout' => @layout,
          'type' => 'archive',
          'title' => "Monthly archive for #{@year}/#{@month}",
          'posts' => posts,
          'url' => File.join('/',
                     MonthlyArchiveUtil.archive_base(site),
                     @archive_dir_name, 'index.html')
      }
    end

    def render(layouts, site_payload)
      payload = {
          'page' => self.to_liquid,
          'paginator' => pager.to_liquid
      }.merge(site_payload)
      do_layout(payload, layouts)
    end

    def to_liquid(attr = nil)
      self.data.merge({
                               'content' => self.content,
                               'date' => @date,
                               'month' => @month,
                               'year' => @year
                           })
    end

    def destination(dest)
      File.join('/', dest, @dir, @archive_dir_name, 'index.html')
    end

  end
end


```

### monthly_archive.html

```html
---

---
<div class="monthly-archive">
  <div>
    <span class="title">Monthly archive for {{page.year}}/{{page.month}}</span>
  </div>
  <div>
    <ul>
{{ content }}
    </ul>
  </div>
</div>

```

### monthly_archive.rb

```Ruby
module Jekyll
  class MonthlyArchive < Liquid::Tag
    def initialize(tag_name, markup, tokens)
      @opts = {}
      if markup.strip =~ /\s*counter:(\w+)/i
        @opts['counter'] = ($1 == 'true')
        markup = markup.strip.sub(/counter:(\w+)/i, '')
      end
      super
    end

    def render(context)
      html = ""
      posts = context.registers[:site].posts.reverse
      posts = posts.group_by{|c| {"month" => c.date.month, "year" => c.date.year}}
      posts.each do |period, post|
        month_dir = "/blog/#{period["year"]}/#{"%02d" % period["month"]}/"
        html << "<li><a href='#{month_dir}'>#{period["year"]}-#{"%02d" % period["month"]}"
        html << "  (#{post.count})" if @opts['counter']
        html << "</a></li>"
      end
      html
    end
  end
end


Liquid::Template.register_tag('tag_monthly_archive', Jekyll::MonthlyArchive)

```

### 利用箇所
```
     <div class="sidebar-module">
        <h4>月別アーカイブ</h4>
       {% raw %}{% tag_monthly_archive %}{% endraw %}
     </div>

```


