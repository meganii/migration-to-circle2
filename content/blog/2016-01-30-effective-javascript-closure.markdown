---
title: "[Effective JavaScript]クロージャ"
date: 2016-01-30T16:14:46+09:00
comments: true
category: ['Tech']
tags: ['JavaScript', 'Effective Javascript']
published: true
slug: effective-javascript-closure
img: "https://images-na.ssl-images-amazon.com/images/I/517tJs%2B%2B%2BnL._SL160_.jpg"
---

<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00EESW7JQ/meganii-22/" target="_blank" ><img src="https://images-na.ssl-images-amazon.com/images/I/517tJs%2B%2B%2BnL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00EESW7JQ/meganii-22/" target="_blank" >Effective JavaScript　JavaScriptを使うときに知っておきたい68の冴えたやり方[Kindle版]</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">Devid Herman 翔泳社 2013-04-13    </div><div class="booklink-link2"><div class="shoplinkkindle"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B00EESW7JQ/meganii-22/" target="_blank" >Kindle</a></div><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4798131113/meganii-22/" target="_blank" >Amazon[書籍版]</a></div>                              	  	  	      </div></div><div class="booklink-footer"></div></div>

いい加減、JavaScriptも使えるようになっておきたいので、お勉強。やっぱりよく分からないクロージャについて。

{{% googleadsense %}}

## 項目１１　クロージャと仲良くしよう

### ポイント１ JavaScriptでは現在の関数の外側で定義された関数を参照できる

内側の`make`関数は`magicIngredient`を参照しているが、これは外側の`makeSandwich`関数の中で定義されているもの。

```
function makeSandwich() {
  var magicIngredient = "peanut butter";
  function make(filling) {
    return magicIngredient + " and " + filling;
  }
  return make("jelly");;
}

console.log(makeSandwich());
console.log(makeSandwich());
```

これがクロージャーだーって言って身構えてパッと見るとよくわからないが、処理を追っていけば、


## ポイント２　関数は、その外側の関数がリターンした後になっても、まだ外側の関数内で定義された変数を参照できる

- 関数は、次のように、後で呼び出された時、内側の関数を返す形式で書くことができる

```
function sandwichMaker() {
  var magicIngredient = "peanut butter";
  function make(filling) {
    return magicIngredient + " and " + filling;
  }
  return make;
}

var f = sandwichMaker();
console.log(f("jelly"));
```

JavaScriptの関数値は、呼び出された時に必要となる情報を含む。
その関数を囲むスコープの中で定義されている変数を参照する可能性があれば、それらの変数も内部的に保存する。

このmake関数は、自分のコードでmagicIngredientとfillingという、２つの外側の変数を参照するクロージャーである。



以下の関数式には名前がない（anonymous）。名前をつける必要がないのはこの関数を、新しい関数値を生成するために評価するためだけに使っており、直接呼び出すつもりがないためである。

```
function sandwichMake(magicIngredient) {
  function make(filling) {
    return magicIngredient + " and " + filling;
  };
  return make;
}

var hamAnd = sandwichMake("ham");
console.log(hamAnd("cheese"));  //ham and cheese
console.log(hamAnd("mustard"));  //ham and cheese
var tukeyAnd = sandwichMake("turkey");
console.log(tukeyAnd("Swiss"));   //turkey and Swiss
console.log(tukeyAnd("Provolone"));   //turkey and Provolone
```




## ポイント３　クロージャは外側の変数を更新できる

- クロージャは、外側の変数へのリファレンスを保存するのであって、値をコピーするわけではない
- したがって、変数の更新は、それをアクセスする、すべてのクロージャに反映される

```
function box() {
  var val = undefined;
  return {
    set: function(newVal) { val = newVal; },
    get: function() { return val; },
    type: function() { return typeof val; }
  };
}

var b = box();
console.log(b.type());  // undefinded
b.set(98.6);
console.log(b.get());   // 98.6
console.log(b.type());  // number
```

これも、そういうもんなんだと思えば、身構える必要もないのかと。実際の利用例をもっと見てみたい。


## ポイント

- 関数は、その外側のスコープで定義された変数を参照できる
- クロージャは、自分を作成した関数よりも長生きすることができる
- クロージャは内部で、外側の変数へのリファレンスを保存する。その変数は、読むことも更新することもできる


<div class="booklink-box"><div class="booklink-image"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00EESW7JQ/meganii-22/" target="_blank" ><img src="https://images-na.ssl-images-amazon.com/images/I/517tJs%2B%2B%2BnL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info"><div class="booklink-name"><a href="http://www.amazon.co.jp/exec/obidos/asin/B00EESW7JQ/meganii-22/" target="_blank" >Effective JavaScript　JavaScriptを使うときに知っておきたい68の冴えたやり方[Kindle版]</a><div class="booklink-powered-date">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail">Devid Herman 翔泳社 2013-04-13    </div><div class="booklink-link2"><div class="shoplinkkindle"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/B00EESW7JQ/meganii-22/" target="_blank" >Kindle</a></div><div class="shoplinkamazon"><a href="http://www.amazon.co.jp/exec/obidos/ASIN/4798131113/meganii-22/" target="_blank" >Amazon[書籍版]</a></div>                              	  	  	      </div></div><div class="booklink-footer"></div></div>
