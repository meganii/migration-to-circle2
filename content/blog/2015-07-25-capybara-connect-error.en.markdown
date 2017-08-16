---
title: "Capybara「Request failed to reach server, check DNS and/or server status」"
date: 2015-07-25T17:29:00+09:00
lastmod: 2017-01-02T17:29:00+09:00
comments: true
category: ['Tech']
tags: ['capybara']
published: true
img: "https://images-na.ssl-images-amazon.com/images/I/51qDobozaNL._SL160_.jpg"
slug: capybara-connect-error
---


## Problem

I faced below error when capybara accessed https site by `visit('')` command.

`Request failed to reach server, check DNS and/or server status`

```
/usr/local/lib/ruby/gems/2.1.0/gems/poltergeist-1.6.0/lib/capybara/poltergeist/browser.rb:323:in `command': Request failed to reach server, check DNS and/or server status (Capybara::Poltergeist::StatusFailError)
	from /usr/local/lib/ruby/gems/2.1.0/gems/poltergeist-1.6.0/lib/capybara/poltergeist/browser.rb:31:in `visit'
	from /usr/local/lib/ruby/gems/2.1.0/gems/poltergeist-1.6.0/lib/capybara/poltergeist/driver.rb:95:in `visit'
	from /usr/local/lib/ruby/gems/2.1.0/gems/capybara-2.4.4/lib/capybara/session.rb:227:in `visit'
	from /usr/local/lib/ruby/gems/2.1.0/gems/capybara-2.4.4/lib/capybara/dsl.rb:51:in `block (2 levels) in <module:DSL>'
	from itunes.rb:24:in `login'
	from itunes.rb:61:in `<main>'
```

{{% googleadsense %}}


## Cause

It happened SSL certificate errors.

> The problem is most likely due to SSL certificate errors. If you start phantomjs with the --ignore-ssl-errors=yes option, it should proceed to load the page as it would if there were no SSL errors:
[screen scraping - PhantomJS failing to open HTTPS site - Stack Overflow](http://stackoverflow.com/questions/12021578/phantomjs-failing-to-open-https-site/24679134#24679134)


## Solution

I solved the problem in below way.

```
phantomjs_options: ['--ignore-ssl-errors=yes']
```


If you still have trouble, you try to below options.

`--load-images=no`, `--ssl-protocol=any`

```
Capybara.register_driver :poltergeist do |app|
  Capybara::Poltergeist::Driver.new(app, {
                    js_errors: false,
                    timeout: 1000,
                    phantomjs_options: [
                              '--load-images=no',
                              '--ignore-ssl-errors=yes',
                              '--ssl-protocol=any']})
end
```


## Reference

- [selenium - Ruby: Phantom.js blocked on specific site? - Stack Overflow](http://stackoverflow.com/questions/25706563/ruby-phantom-js-blocked-on-specific-site)
- [screen scraping - PhantomJS failing to open HTTPS site - Stack Overflow](http://stackoverflow.com/questions/12021578/phantomjs-failing-to-open-https-site/24679134#24679134)
- [Command Line Interface | PhantomJS](http://phantomjs.org/api/command-line.html)
