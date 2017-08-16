---
title: "slack-apiを利用してRubyからSlackへメッセージとファイルをポストする方法"
date: 2016-02-10T07:17:11+09:00
comments: true
category: ['Tech']
tags: ['Slack']
published: true
slug: post-to-slack
---

Slackで、Rubyからメッセージとファイルをポストする方法についてのメモ。

以下の`slack-api`を利用する。
[aki017/slack-ruby-gem: A Ruby wrapper for the Slack API](https://github.com/aki017/slack-ruby-gem)

{{% googleadsense %}}

ファイルの組み立て方(?)が分からなかったのでFaradayにお任せした。

```
require 'slack'
require 'faraday'

Slack.configure do |config|
  config.token = "USER SLACK TOKEN"
end

## channelにメッセージをPostする
Slack.chat_postMessage(
  channel: '#general',
  username: 'kenchan',
  text: 'point'
)

## channelにファイルをアップロードする
Slack.files_upload(
  file: Faraday::UploadIO.new('stamp.png', 'image/png'),
  channels: '#general',
  initial_comment: 'file upload'
)

```
