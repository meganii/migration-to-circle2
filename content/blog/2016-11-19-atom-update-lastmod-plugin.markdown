---
title: "Atomプラグインの作り方"
date: 2016-11-19T11:14:10+09:00
lastmod: 2016-11-19T11:27:50+09:00
slug: "creating-atom-plugin"
---

静的サイトジェネレータでサイトを管理するときに、作成日時だけでなく更新日時も管理したいときに、frontmatterに`lastmod`を追加したのだが、いちいち更新日時を手動で更新するのも面倒なのでatomプラグインで実現することにした。

## Atom pluginの作り方

Atomは、`Coffee Script`で書かれているので、今までは`Coffee Script`でしかpluginをかけないと思っていましたが、いつの間にかES2015でもかけるようになっていたので、チャレンジしてみました。

`ctrl + command + P`でコマンドパレットを起動して、Generate Pluginを選択する。




## テスト




## 参考

https://github.com/meganii/atom-update-lastmod-on-markdown
