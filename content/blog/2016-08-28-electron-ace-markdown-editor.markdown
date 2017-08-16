---
title: "AceエディタをElectronに組み込む"
date: 2016-08-28T09:02:38+09:00
comments: true
category: ['Tech']
tags: ['JavaScript','Electron']
published: true
slug: electron-ace-markdown-editor
img: "https://farm9.staticflickr.com/8537/29243326176_ea1c871651_s.jpg"

---

![electron-ace-markdown-editor](https://farm9.staticflickr.com/8537/29243326176_ea1c871651_z.jpg)


<!--more-->
{{% googleadsense %}}


前回作成したときに課題として残っていたAceエディタの導入を行なった。

## Ace Editor

[Ace \- The High Performance Code Editor for the Web](https://ace.c9.io/#nav=about)

Aceとは、JavaScriptのライブラリで、高機能なエディタを提供している。自分のアプリケーションのエディタとして組み込むためには、以下のnpmライブラリを組み込めば良い。

[https://www.npmjs.com/package/brace](https://www.npmjs.com/package/brace)

### 導入
```
npm install brace
```

```
var ace = require('brace');
require('brace/mode/javascript');
require('brace/theme/monokai');
 
var editor = ace.edit('javascript-editor');
editor.getSession().setMode('ace/mode/javascript');
editor.setTheme('ace/theme/monokai');
```

### React+Reduxの例

以下は、id `editor`のエレメントに対してAce Editorを有効にする例です。

```javascript
class Editor extends Component {

    componentDidMount () {
      this.editor = ace.edit('editor');
      this.editor.$blockScrolling = Infinity;
      this.editor.getSession().setMode('ace/mode/markdown');
      this.editor.getSession().setUseWrapMode(true);
      this.editor.setTheme('ace/theme/github');
      this.editor.setFontSize(14);
      this.editor.setValue(this.props.store.getState().markdown, -1);
      this.editor.on('change', this.onChange.bind(this));
      this.editor.setOption('maxLines', 99999);
      this.editor.setOption('minLines', 50);
      this.editor.setOption('highlightActiveLine', true);
      this.editor.setShowPrintMargin(false);
      this.editor.focus();
      if(process.platform == 'darwin') { // Ctrl+Pが効かない問題に対処
        this.editor.commands.bindKey("Ctrl-P", "golineup");
      }
      // FIXME
      this.interval = setInterval(() => this.editor.resize(), 100);
    }

    componentWillReceiveProps (nextProps) {
      if (this.editor.getValue() !== nextProps.store.getState().markdown) {
        this.editor.setValue(nextProps.store.getState().markdown, -1)
      }
    }

    componentWillUnmount () {
      this.editor.destroy()
      clearInterval(this.interval)
    }

    onChange() {
      const value = this.editor.getValue();
      this.props.store.dispatch.bind(this)({
        type: 'UPDATE',
        markdown: value,
        html: { __html: markup(value) }
      });
    }

    render () {
      return (
        <div
          onChange={this.onChange}
          id="editor"
          value={this.props.store.getState().markdown}
        />
      );
    }
  }
```

Ctrl+Pでのカーソル移動が効かない問題に対処するために、以下の設定を追加している。

```
    if(process.platform == 'darwin') { // Ctrl+Pが効かない問題に対処
        this.editor.commands.bindKey("Ctrl-P", "golineup");
    }
```

## 参考

- [テキストエディターを作ってElectronの基礎を学ぼう！ HTML5でPCアプリ開発入門](https://ics.media/entry/8401)






