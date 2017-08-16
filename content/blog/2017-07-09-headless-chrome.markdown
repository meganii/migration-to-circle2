---
title: "Docker環境のCapybaraでHeadless Chromeを試してみた"
date: 2017-07-09T22:30:00+09:00
lastmod: 2017-07-09T22:30:00+09:00
comments: true
category: ['Tech']
tags: ['Capybara','Ruby']
published: true
slug: headless-chrome
img:
---


- [Dockerを使ってHeadless Chromeを動かしてみる \- Qiita](http://qiita.com/dd511805/items/dfe03c5486bf1421875a)
- [\[2017/6最新\]RubyとSeleniumでHeadless chromeを動かす on Ubuntu/Linux \- Qiita](http://qiita.com/meguroman/items/41ca17e7dc66d6c88c07)


<!--more-->
{{% googleadsense %}}


## Dockerfile

```
FROM ubuntu:trusty

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install software-properties-common wget git curl xvfb unzip

# deps for ruby
RUN apt-get -y install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev

# ruby ppa
RUN add-apt-repository -y ppa:brightbox/ruby-ng

# chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

RUN apt-get update

RUN apt-get -y install ruby2.4 ruby2.4-dev google-chrome-unstable

# Dependencies to make "headless" chrome/selenium work:
RUN apt-get -y install xvfb gtk2-engines-pixbuf
RUN apt-get -y install xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable

# chrome driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/
RUN chmod ugo+rx /usr/bin/chromedriver

RUN gem install bundler nokogiri

# for pg install
RUN apt-get -y install libpq-dev imagemagick
RUN gem install pg
RUN gem install mini_magick


RUN mkdir /noto

ADD https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip /noto

WORKDIR /noto

RUN unzip NotoSansCJKjp-hinted.zip && \
    mkdir -p /usr/share/fonts/noto && \
    cp *.otf /usr/share/fonts/noto && \
    chmod 644 -R /usr/share/fonts/noto/ && \
    fc-cache -fv

WORKDIR /
RUN rm -rf /noto


RUN mkdir /app
WORKDIR /app
ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN bundle install
ADD . /app
RUN mkdir -p /app/tmp/sockets

ADD docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

# Expose volumes to frontend
VOLUME /app/public
VOLUME /app/tmp

CMD bundle exec puma
```


### Before

```ruby
Capybara.configure do |config|
    config.run_server = false
    config.current_driver = :poltergeist
    config.app_host = 'http://www.hogehoge.net/'
    config.default_max_wait_time = 30
    config.javascript_driver = :poltergeist
  end

  Capybara.register_driver :poltergeist do |app|
    options = {
      js_errors: false,
      timeout: 5000,
      debug: false,
      phantomjs_options: [
        '--load-images=yes',
        '--ignore-ssl-errors=yes',
        '--ssl-protocol=any'
      ]
    }
    Capybara::Poltergeist::Driver.new(app, options)
  end
  @session = Capybara::Session.new(:poltergeist)
```


### After

`chromeOptions`の`binary`には、Dockerに入れたChromeのパスを指定する。

```ruby
Capybara.configure do |config|
  config.run_server = false
  config.current_driver = :headless_chrome
  config.app_host = 'http://www.cosme.net/'
  config.default_max_wait_time = 30
  config.javascript_driver = :headless_chrome
end

@http_client ||= Selenium::WebDriver::Remote::Http::Default.new(open_timeout: 5000, read_timeout: 5000)

Capybara.register_driver :chrome do |app|
  Capybara::Selenium::Driver.new(app, browser: :chrome)
end

Capybara.register_driver :headless_chrome do |app|
  caps = Selenium::WebDriver::Remote::Capabilities.chrome(
    'chromeOptions' => {
      'binary' => '/usr/bin/google-chrome',
      'args' => %w[headless disable-gpu no-sandbox window-size=1200x600]
    }
  )
  Capybara::Selenium::Driver.new(app, {:browser => :chrome, :http_client => @http_client, :desired_capabilities => caps})
end
@session = Capybara::Session.new(:headless_chrome)
```


## imagemagick周りでハマった点

rmagickは、ImageMagik7系に対応していないみたい。

[bundle install "rmagick" でインストールができない \- Qiita](http://qiita.com/sho012b/items/362abe993248c686fcf4)


mini_magick


## apline linexを使ってハマった点

### `gem install therubyracer`を有効にしたら、こけた。


> therubyracerはlibv8というgemに依存しており、インストール時にlibv8に含まれるv8のライブラリにリンクされます。ここで、libv8は（ドキュメントにもあるのですが）通常だとコンパイル済みのバイナリで、Linuxの場合にはglibcにリンクされたものがインストールされるようになっているということのようです。そしてAlpine linuxではglibcではなくmusl libcがベースになっているという事情から、そのままでは動かないということでした。

[therubyracerをAlpine linuxでも動くようにするDockerfileを書きました \- blog\.taaas\.jp](http://blog.taaas.jp/tips/therubyracer-docker/)


諦めて、`apk install node.js`に変更した。


## ubuntu

最新版のChromeと、最新版のChromedriverを用いても、なぜかXVFB関連のエラーが発生した。下記URLによると、chromedriver側の問題のようだ。

[Chromedriver running against canary chrome w/ headless flag requires XVFB for sendKey interactions	](https://bugs.chromium.org/p/chromedriver/issues/detail?id=1772)

> I rented a huge server on AWS and cut a 2.31 release with this patch in it for `linux_64`. The binary is available on github here https://github.com/davidthornton/chromedriver-2.31

chromedriverのバグフィックス版を使わせていただいたところ、問題が解消した。
https://github.com/davidthornton/chromedriver-2.31




## PoltergeistとHeadless Chromeの違い

- Chromeだと画面全体、要素のみのスクリーンショットが取れない


[How to take full\-page screenshots with Selenium and Google Chrome in Ruby](https://gist.github.com/elcamino/5f562564ecd2fb86f559#file-full-page-screenshots-selenium-chrome-rb-L20)



## unknown error: Element is not clickable at point (625, 886)

画面外のリンクをクリックしているときに発生するみたい。

[Selenium WebDriver : How do I set capabilities elementScrollBehavior to 1 for a FireFox configuration in rails? \- Stack Overflow](https://stackoverflow.com/questions/36439701/selenium-webdriver-how-do-i-set-capabilities-elementscrollbehavior-to-1-for-a)

### 暫定回避

`chromeOptions`に`window-size`を渡してあげて、全ての画面が見えるようにする。

```ruby
Capybara.register_driver :headless_chrome do |app|
  caps = Selenium::WebDriver::Remote::Capabilities.chrome(
    'chromeOptions' => {
      'binary' => '/usr/bin/google-chrome',
      'args' => %w[headless disable-gpu no-sandbox window-size=1200x3000]
    },
    'elementScrollBehavior' => 1
  )
  options = {
    browser: :chrome,
    http_client: @http_client,
    desired_capabilities: caps
  }
  Capybara::Selenium::Driver.new(app, options)
end
```
