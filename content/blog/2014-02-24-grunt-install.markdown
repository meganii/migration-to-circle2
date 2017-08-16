---
title: Gruntのインストール
date: 2014-02-24T23:01:00+09:00
category: ['Tech']
tags: ['grunt']
published: false
slug: grunt-install
---

## Grunt Install

```
npm install -g grunt-cli
npm install grunt --save-dev
```

早速、`grunt`って叩くと、怒られた。

```
$ grunt
>> Local Npm module "grunt-contrib-clean" not found. Is it installed?
>> Local Npm module "grunt-contrib-jshint" not found. Is it installed?
>> Local Npm module "grunt-contrib-uglify" not found. Is it installed?
>> Local Npm module "grunt-contrib-watch" not found. Is it installed?
>> Local Npm module "grunt-recess" not found. Is it installed?
>> Local Npm module "grunt-contrib-imagemin" not found. Is it installed?
>> Local Npm module "grunt-svgmin" not found. Is it installed?
Warning: Task "clean" not found. Use --force to continue.

Aborted due to warnings.
```

それぞれインストールしていく。

```
npm install grunt-contrib-clean --save-dev
npm install grunt-contrib-jshint --save-dev
npm install grunt-contrib-uglify --save-dev
npm install grunt-contrib-watch --save-dev
npm install grunt-recess --save-dev
npm install grunt-contrib-imagemin --save-dev
npm install grunt-svgmin --save-dev
```

これでやっと `grunt`を実行できた。


## メモ

- `--save-dev`をつけると、package.jsonにインストールした情報が記述される
- `package.json`にインストールしたいプラグインを書くことで`npm install`でインストール出来る。


## 参考

- [Grunt.jsの始め方 -インストール編- | css | basara669.com](http://basara669.com/frontend/gruntjs_first_step2/)
- [Web制作で面倒な作業を自動化するビルドツール、Grunt v0.4 入門｜Web Design KOJIKA17](http://kojika17.com/2013/03/grunt.js-memo.html)
