---

title: abコマンド実行時のエラーを回避する
date: 2013-05-27T19:29:00+09:00
category: ['Tech']
tags: ['unix']
published: true
slug: benchmark-apache
---

```
ab -c 10 -n 100 http://hostname.com/
```

ベンチマークを取ろうと、上記のようなabコマンドを実行すると、毎回怒られる。以下、エラー内容。

```
This is ApacheBench, Version 2.3 <$Revision: 655654 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking havelog.ayumusato.com (be patient)...Send request failed!
apr_socket_recv: Connection reset by peer (54)
Total of 1 requests completed
```


{{% googleadsense %}}

調べてみると、Versionの問題みたい。

- [osx lion - Apache Bench test error on OS X: &quot;apr_socket_recv: Connection reset by peer (54)&quot; - Super User](http://superuser.com/questions/323840/apache-bench-test-erroron-os-x-apr-socket-recv-connection-reset-by-peer-54)
- [Mac OS X Lionでabを実行する際にエラー：Connection reset by peerが発生する際の対処方法 | Web活メモ帳](http://blog.verygoodtown.com/2012/05/apache-bench-test-erroron-os-x-apr-socket-recv-connection-reset-by-peer-54/)
- [nginxにLion付属のab（ApacheBench）を実行したら失敗するときの解決ログ ::ハブろぐ](http://havelog.ayumusato.com/develop/others/e477-lion_bundled_ab_nginx.html)

[http://apache.mirrors.pair.com/httpd/](http://apache.mirrors.pair.com/httpd/)から最新版の httpdをダウンロード。

上記のページを参考にしながら、最新版にアップロードする。


```
wget http://apache.mirrors.pair.com/httpd/httpd-2.4.4.tar.bz2
brew install pcre
tar xzvf httpd-2.4.4.tar.bz2
cd httpd-2.4.4
./configure
make
```


```
$ ab -c 10 -n 100 http://hostname.com/
This is ApacheBench, Version 2.3 <$Revision: 1430300 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking meganii.com (be patient).....done


Server Software:        Apache
Server Hostname:        meganii.com
Server Port:            80

Document Path:          /
Document Length:        18215 bytes

Concurrency Level:      10
Time taken for tests:   3.071 seconds
Complete requests:      100
Failed requests:        0
Write errors:           0
Total transferred:      1847200 bytes
HTML transferred:       1821500 bytes
Requests per second:    32.56 [#/sec] (mean)
Time per request:       307.123 [ms] (mean)
Time per request:       30.712 [ms] (mean, across all concurrent requests)
Transfer rate:          587.36 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       55   75  15.6     70     118
Processing:   137  220 148.2    179    1438
Waiting:       62  107  45.8     97     338
Total:        206  295 157.9    249    1556

Percentage of the requests served within a certain time (ms)
  50%    249
  66%    270
  75%    278
  80%    293
  90%    534
  95%    574
  98%    598
  99%   1556
 100%   1556 (longest request)
```

出来た！読み方を押さえておこう。

## 参考
<a href="http://blog.verygoodtown.com/2012/05/apache-bench-ab/" target="_blank"><img class="alignleft" align="left" border="0" src="http://capture.heartrails.com/150x130/shadow?http://blog.verygoodtown.com/2012/05/apache-bench-ab/" alt="" width="150" height="130" /></a><a style="color:#0070C5;" href="http://blog.verygoodtown.com/2012/05/apache-bench-ab/" target="_blank">Apache Benchを使った負荷テストのやり方 | Web活メモ帳</a><a href="http://b.hatena.ne.jp/entry/http://blog.verygoodtown.com/2012/05/apache-bench-ab/" target="_blank"><img border="0" src="http://b.hatena.ne.jp/entry/image/http://blog.verygoodtown.com/2012/05/apache-bench-ab/" alt="" /></a><br style="clear:both;" /><br>

