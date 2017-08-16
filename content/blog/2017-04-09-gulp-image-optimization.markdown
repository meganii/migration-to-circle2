---
title: "gulpで画像の最適化"
date: 2017-04-09T12:11:44+09:00
lastmod: 2017-04-09T12:11:44+09:00
comments: true
category: ['Tech']
tags: ['Hugo','gulp']
published: true
slug: gulp-image-optimization
---

完全に自己満足かもしれませんが、以下の理由で画像の最適化に取り組みました。

- Google PageSpeed Insightsで毎回画像サイズが最適化されていないと毎回怒られる
- 画像ファイルのサイズが無駄に大きいため、iPhoneからアクセスした時に余計なパケットを消費するのが悔しい

画像の最適化を全て手動でやると挫折してしまうので、タスクランナーである`gulp`で自動化を行いました。

<!--more-->
{{% googleadsense %}}

## やりたいこと

1. Markdown形式のファイルに対して画像ファイルをドラッグ＆ドロップで画像リンク生成
2. 画像ファイルをレスポンス対応(srcsets)させるため、数種類のサイズにリサイズ
3. リサイズ後の画像ファイルを最適化(圧縮)

「1.」のドラッグ＆ドロップで画像リンク生成は、エディタのプラグインで実現することにし、「2.」「3.」を`gulp`のタスクで実現を目指しました。


## 画像のresponsive対応

なんとなく、320px,640px,1280px,オリジナルファイルという4種類にリサイズするようにしてみました。

```javascript
gulp.task('responsive', function(){
  return gulp.src(['src/images/**/*.jpg','src/images/**/*.png'], { base: 'src'})
        .pipe(responsive({
          // Resize all JPG images to three different sizes: 200, 500, and 630 pixels
          'images/**/*.jpg': [{
            width: 320,
            rename: { suffix: '-320x' },
          }, {
            width: 640,
            rename: { suffix: '-640x' },
          }, {
            width: 1280,
            rename: { suffix: '-1280x' },
          }, {
            // Compress, strip metadata, and rename original image
            rename: { suffix: '-o' },
          }],
          // Resize all PNG images to be retina ready
          'images/**/*.png': [{
            width: 250,
          }, {
            width: 250 * 2,
            rename: { suffix: '@2x' },
          }],
        }, {
          // Global configuration for all images
          // The output quality for JPEG, WebP and TIFF output formats
          quality: 70,
          // Use progressive (interlace) scan for JPEG and PNG output
          progressive: true,
          // Strip all metadata
          withMetadata: false,
      }))
      .pipe(gulp.dest('static/'));
});
```

[gulp\-responsive/multiple\-resolutions\.md at master · mahnunchik/gulp\-responsive](https://github.com/mahnunchik/gulp-responsive/blob/master/examples/multiple-resolutions.md)

### Tips 出力処理

`gulp.src`に`base`というオプションがあり、これを指定するとディレクトリ構造を維持して出力することができます。

```javascript
var gulp = require('gulp');

gulp.task('copy', function() {
    return gulp.src(
        ['src/images/**/.jpg', 'src/images/**/.png'],
        { base: 'src' }
    )
    .pipe(gulp.dest('static/'));
} );
```

## 画像の最適化

画像の最適化には、`gulp-imagemin`を利用しました。

```javascript
var imagemin = require('gulp-imagemin');
gulp.task('imagemin', function() {
  return gulp.src('src/images/**/*.jpg')
      .pipe(imagemin())
      .pipe(gulp.dest('static/'));
});
```


## 組み合わせた結果

Hugoのルートディレクトリで`gulp`を叩けば、jpg, pngを監視し、ファイルが追加されれば、画像フォルダに変換後の画像が作成されるようになります。

```javascript
gulp.task('default', function(cb) {
  var watcher = gulp.watch('src/images/**/*.{jpg,png}');
  watcher.on('change', function(event) {
    console.log(event);
    console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    const extname = event.path.split(".").pop(); // TODO error handle
    console.log(extname);
    if (extname === "jpg") {
      gulp.src(event.path, { base: 'src'})
          .pipe(responsive({
            // Resize all JPG images to three different sizes: 200, 500, and 630 pixels
            'images/**/*.jpg': [{
              width: 640,
            }, {
              width: 64,
              rename: { suffix: '-64x'},
            }, {
              width: 320,
              rename: { suffix: '-320x' },
            }, {
              width: 640,
              rename: { suffix: '-640x' },
            }, {
              width: 1280,
              rename: { suffix: '-1280x' },
            }, {
              // Compress, strip metadata, and rename original image
              rename: { suffix: '-o' },
            }],
          }))
        .pipe(imagemin())
        .pipe(gulp.dest('static/'));
    } else if (extname === "png") {
      gulp.src(event.path, { base: 'src'})
          .pipe(responsive({
            // Resize all PNG images to be retina ready TODO
            'images/**/*.png': [{
              width: 64,
              rename: { suffix: '-64x'}
            }, {
              width: 640,
            }, {
              width: 640 * 2,
              rename: { suffix: '@2x' },
            }],
          }, {
            // Global configuration for all images
            // The output quality for JPEG, WebP and TIFF output formats
            quality: 70,
            // Use progressive (interlace) scan for JPEG and PNG output
            progressive: true,
            // Strip all metadata
            withMetadata: false,
        }))
        .pipe(imagemin())
        .pipe(gulp.dest('static/'));
    } else {
      console.log("not jpg or png");
    }

  });

  // hugo
  exec('hugo server -t hugo-zen', function(err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    if (err) return cb(err); // return error
    cb(); // finished task
  });
});
```

## まとめ

画像の最適化は、手動だとめんどくさくてなかなか出来ないが、一度自動化してしまえば後は楽です。
少しずつメンテナンスを加えて使い勝手を良くしていきたいと思います。



## 参考

- [gulp でディレクトリ構造を維持したコピー – アカベコマイリ](http://akabeko.me/blog/2015/01/gulp-copy-keep-dir-structure/)
- [Gulpでディレクトリ構造を維持して出力する方法 \| Glatch（グラッチ） – 夫婦で活動するフリーランスWeb制作ユニット](http://glatchdesign.com/blog/web/coding/968)
- [Gruntとgulp\.jsでサイトパフォーマンスを向上させる \- ワザノバ \| wazanova](http://wazanova.jp/items/1128)
- [これからはじめるGulp \#12：gulp\-imageminプラグインを使ったJPEG,PNG,GIF,SVGの最適化 ｜ Developers\.IO](http://dev.classmethod.jp/client-side/javascript/gulp-solo-adv-cal-12/)
- [レスポンシブイメージで画像の表示を最適化 〜CSSもJSもいらないHTML 5\.1の新機能 \- ICS MEDIA](https://ics.media/entry/13324)
- [gulpで画像のロスレス圧縮を自動化する \- satoyan419\.com](http://satoyan419.com/optimizing-images-with-gulp/)
- [Gulpを使って特定のファイルが変更されたら自動的にタスクを実行する方法 \| 今村だけがよくわかるブログ](https://www.imamura.biz/blog/25968)
- [HugoとGulpを共存させて、ブランドデザインを刷新した \| Timegraphy](https://thetimegraphy.com/redesign-with-hugo-and-gulp/)
- [【追記あり】Gulpを利用して画像をロスレス圧縮する \- takedajs ログ](http://takedajs.hatenablog.jp/entry/2016/08/01/231609)
- [srcset属性について \- Qiita](http://qiita.com/C058/items/643a9ff2d23dfe3a0b37)
- [scalableminds/gulp\-image\-resize: Resizing images made easy \- thanks to imagemagick\.](https://github.com/scalableminds/gulp-image-resize)
