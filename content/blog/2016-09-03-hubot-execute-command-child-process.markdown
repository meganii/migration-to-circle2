---
title: "Hubotで外部コマンドを実行する"
date: 2016-09-03T09:53:38+09:00
comments: true
category: ['Tech']
tags: ['Hubot','JavaScript']
published: true
slug: hubot-execute-command-child-process
img: "https://farm9.staticflickr.com/8168/28820861054_3f40884614_z.jpg"

---

![slack](https://farm9.staticflickr.com/8168/28820861054_3f40884614_z.jpg)


Node.jsで外部コマンドを実行するために、`Child Process`を利用する。

[Child Process \| Node\.js v6\.5\.0 Documentation](https://nodejs.org/api/child_process.html#child_process_child_process_exec_command_options_callback)

```javascript
const exec = require('child_process').exec;
exec('cat *.js bad_file | wc -l', (error, stdout, stderr) => {
  if (error) {
    console.error(`exec error: ${error}`);
    return;
  }
  console.log(`stdout: ${stdout}`);
  console.log(`stderr: ${stderr}`);
});
```


## Hubotの例

```javascript
child_process = require 'child_process'

module.exports = (robot) ->
  robot.hear /ruby/i, (res) ->
    child_process.exec "ruby -v", (error, stdout, stderr) ->
      if !error
        output = stdout+''
        res.send output
      else
        res.send 'error'
```


## 参考
- [Child Process \| Node\.js v6\.5\.0 Documentation](https://nodejs.org/api/child_process.html)
- [Hubot で外部コマンドを実行する \- Qiita](http://qiita.com/tbpgr/items/758c957ba07a71869604)