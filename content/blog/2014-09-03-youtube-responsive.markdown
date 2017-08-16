---

title: "YouTube埋め込みタグをレスポンシブ化する"
date: 2014-09-03T23:26:00+09:00
comments: true
category: ['Tech']
tags: ["youtube", "design", "jekyll"]
published: true 
slug: youtube-responsive
---


せっかくのレスポンシブデザインなので、YouTubeの埋め込みもレスポンシブ化してみた。


{{% googleadsense %}}

### main.css
```
.youtubeWrapper{
position: relative ;
margin-top: 1.2em ;
margin-bottom: 1.2em ;
padding-top: 69px ;
padding-bottom: 50% ;
overflow: hidden ;
}

.youtubeWrapper iframe {
position: absolute ;
top: 0 ;
left: 0 ;
height: 100% ;
width: 100% ;
}
```


### default.html
```
<div class="youtubeWrapper">
<iframe width="560" height="315" src="//www.youtube.com/embed/PRI0bA5VSL8" frameborder="0" allowfullscreen></iframe>
</div>
```

以下は、レスポンシブ化されたYouTube埋め込みタグです。

<div class="youtubeWrapper">
<iframe width="560" height="315" src="//www.youtube.com/embed/PRI0bA5VSL8" frameborder="0" allowfullscreen></iframe>
</div>


## 参考
[「埋め込み動画のサイズをレスポンシブにする方法」 | 有限会社ワイバーン](http://www.wivern.com/report20130802.html)
