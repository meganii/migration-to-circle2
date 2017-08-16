---
title: "PythonでTF-IDFによる文書推薦"
date: 2016-08-13T18:43:18+09:00
comments: true
category: ['Tech']
tags: ['TF-IDF','Python']
published: true
slug: tf-idf-recommendation
img: https://images-fe.ssl-images-amazon.com/images/I/51YzbphP0JL._SL160_.jpg
---



<!--more-->
{{% googleadsense %}}


```
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.metrics.pairwise import cosine_similarity

import MeCab
import re

from collections import OrderedDict, defaultdict

def mecabAnalyzer(doc, to_stem=True):
    p = re.compile(r'<.*?>')
    tagger = MeCab.Tagger('mecabrc')
    mecab_result = tagger.parse(p.sub("",doc))
    # mecab_result = tagger.parse(doc)
    info_of_words = mecab_result.split('\n')
    words = []
    for info in info_of_words:
        # macabで分けると、文の最後に’’が、その手前に'EOS'が来る
        if info == 'EOS' or info == '':
            break
            # info => 'な\t助詞,終助詞,*,*,*,*,な,ナ,ナ'
        info_elems = info.split(',')
        # 6番目に、無活用系の単語が入る。もし6番目が'*'だったら0番目を入れる
        if info_elems[6] == '*':
            # info_elems[0] => 'ヴァンロッサム\t名詞'
            words.append(info_elems[0][:-3])
            continue
        if to_stem:
            # 語幹に変換
            words.append(info_elems[6])
            continue
        # 語をそのまま
        words.append(info_elems[0][:-3])
    return words

def tf(doc):
    vectorizer = CountVectorizer(analyzer=mecabAnalyzer,token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(doc)
    terms = vectorizer.get_feature_names()
    return features, terms

def tfidf(docs):
    vectorizer = TfidfVectorizer(analyzer=mecabAnalyzer ,min_df=1, max_df=50, token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(docs)
    terms = vectorizer.get_feature_names()
    return features, terms

if __name__ == '__main__':
    docs = []
    file = open('contents.txt', 'r')
    lines = file.readlines()
    for line in lines:
        docs.append(re.sub(r"[0-9].+?|\/|\"|\(|\)","",line))

    features, terms = tfidf(docs)
    tfidf_mtx = features.toarray()

    target = 155
    cos_table = defaultdict(int)
    for i, tfidf in enumerate(tfidf_mtx):
        if i == target:
            continue
        cos = cosine_similarity(tfidf_mtx[target], tfidf)
        cos_table[i] = cos

    top_cos = sorted(cos_table.items(), key=lambda t:t[1], reverse=True)
    top_cos = filter(lambda t:t[1] > 0.05, top_cos)

    print("target:" + docs[target][0:100])
    for key, value in top_cos:
        print(key, value, docs[key][0:100])
```



## 結果

```
target:---  title: "[SQL実践入門]結合のアルゴリズム Nested Loops, Hash, Sort Merge" date: 2015-06-01T00:48:00+09:00 comm
115 [[ 0.55160702]] ---  title: "[SQL実践入門]内部結合と外部結合のイメージ" date: 2015-06-10T07:58:00+09:00 comments: true category: ['Tec
52 [[ 0.30073406]] --- title: 索引設計についてのまとめ date: 2013-10-02T21:45:00+09:00 category: ['Tech'] tags: ['索引設計','DB'] publi
```


```
target:--- title: "さくらVPSのCentOS6.4にh2oをAnsibleでビルド＆インストール" date: 2016-07-18T21:44:52+09:00 comments: true
105 [[ 0.25046155]] ---  title: "AnsibleでさくらVPSの初期設定" date: 2015-03-02T07:31:00+09:00 comments: true category: ['Tech']
173 [[ 0.22914362]] --- title: "http/2ベンチマークツール「h2load」をインストール" date: 2016-07-17T20:19:21+09:00 comments: true category:
146 [[ 0.17700005]] --- title: "El Capitanへのアップグレード時AppStoreに接続できなくなった場合(さらにキーチェーンアクセスでも対処できなかった時)の対処法 " date: 2016-01-2
145 [[ 0.1583195]] --- title: "Lets's Encryptでブログの常時SSL化にチャレンジ" date: 2016-01-17T22:44:45+09:00 comments: true category
```

```
target:---  title: "春の松島、秋の宮島、冬の天橋立〜日本三景巡り〜" date: 2014-12-17T21:19:00+09:00 comments: true category: ['Tra
101 [[ 0.23335708]] ---  title: "札幌・すすきの「だるま」ジンギスカンと「開陽亭」でウニ・イクラ・イカの踊りを食べてきた!!" date: 2015-01-26T23:37:00+09:00 comments
31 [[ 0.17691893]] ---  title: 晴れの屋久島。雨の屋久島。屋久島旅行記 date: 2013-05-07T07:13:00+09:00 category: ['Travel'] tags: ['屋久島','t
162 [[ 0.08934358]] --- title: "「犬も歩けばBAR(バル)に当たる」スペイン・バルセロナ旅行記2016" date: 2016-05-05T12:38:27+09:00 comments: true cate
51 [[ 0.07399384]] --- title: 初めての北アルプス 〜涸沢ヒュッテ、奥穂高岳〜 date: 2013-08-25T21:21:00+09:00 category: ['Travel'] tags: ['登山',
```


```
target:--- title: "「システムインテグレーション崩壊」を読んで生存戦略を考える" date: "2015-08-31T23:53:00+09:00" comments: true category
136 [[ 0.31483654]] --- title: "「「納品」をなくせばうまくいく」を読んで生存戦略を考える" date: 2015-10-25T14:25:07+09:00 comments: true category: [
143 [[ 0.24363777]] --- title: "CIOとは何者？" date: 2015-12-08T19:55:40+09:00 comments: true category: ['Tech'] tags: ['IT']
100 [[ 0.12402966]] ---  title: "達人に学ぶSQL, DB設計をぽちった" date: 2014-12-24T23:34:00+09:00 comments: true category: ['Tech']
129 [[ 0.11944831]] --- title: "マーケティング22の法則を図解してみた" date: "2015-08-29T17:13:12+09:00" comments: true category: ['Book']
117 [[ 0.09873303]] ---  title: "scrum boot camp the book" date: 2015-06-21T20:20:00+09:00 comments: true category: ['Te
```


```
target:--- title: "JekyllからHugoへの移行ポイント" date: "2015-08-30T11:56:00+09:00" comments: true category: ['Tech'
159 [[ 0.21217108]] --- title: "Hugo-ZenをベースにHugoのデザインを変えてみた" date: 2016-04-17T19:57:49+09:00 comments: true category: [
135 [[ 0.16134027]] --- title: "Hugoソースコードリーディング〜Taxonomy〜" date: 2015-10-11T22:03:56+09:00 comments: true category: ['T
23 [[ 0.15218758]] ---  title: はてなダイアリーからJekyllへお引越し date: 2013-02-03T10:47:00+09:00 category: ['Tech'] tags: ['jekyll'
173 [[ 0.14863093]] --- title: "http/2ベンチマークツール「h2load」をインストール" date: 2016-07-17T20:19:21+09:00 comments: true category:
81 [[ 0.11394251]] ---  title: "Jekyllでページ分割する -pagenation-" date: 2014-10-21T07:37:00+09:00 comments: true category: [
113 [[ 0.11065529]] ---  title: "Middlemanで静的サイト構築 -Middlemanで複数ブログを構築-" date: 2015-05-10T09:05:00+09:00 comments: true
```



```
target:--- title: "Electronでデスクトップアプリ作成" date: 2016-01-25T07:15:22+09:00 comments: true category: ['Tech']
155 [[ 0.55232748]] --- title: "ElectronでAmazonアフィリエイトリンクビルダーを作った" date: 2016-02-20T17:51:18+09:00 comments: true catego
157 [[ 0.34286418]] --- title: "Electron + Mithril.jsでFlickrアプリを作成する" date: 2016-02-28T22:13:24+09:00 comments: true cat
```


```
target:--- title: "D3.jsで東京の地価データを可視化する" date: 2016-02-07T19:42:50+09:00 comments: true category: ['Tech']
150 [[ 0.17437764]] --- title: "D3.jsチュートリアル" date: 2016-02-06T12:46:18+09:00 comments: true category: ['Tech'] tags: ['
147 [[ 0.16424267]] --- title: "Electronでデスクトップアプリ作成" date: 2016-01-25T07:15:22+09:00 comments: true category: ['Tech']
157 [[ 0.13608335]] --- title: "Electron + Mithril.jsでFlickrアプリを作成する" date: 2016-02-28T22:13:24+09:00 comments: true cat
155 [[ 0.12556532]] --- title: "ElectronでAmazonアフィリエイトリンクビルダーを作った" date: 2016-02-20T17:51:18+09:00 comments: true catego
```


## うーん

この当たりは、見当違いなものが推薦されてしまっている。
Amazonリンクのせいかと思い、htmlタグを除去し、数字だけのもの(/[0-9].+?/)を覗いたところ、意図した結果となった。

```
target:---  title: "初めてのテント泊ライブ。初めてのRISING SUN ROCK FESTIVAL 2015(ライジングサン)" date: "2015-08-17T08:12:12+09:0
89 [[ 0.43161444]] ---  title: "万年筆LAMY safariのインク洗浄・交換" date: 2014-11-16T23:59:00+09:00 comments: true category: ['Sta
50 [[ 0.41216943]] ---  title: ビジュアル　ロジカル・シンキング date: 2013-07-10T00:11:00+09:00 category: ['Art'] tags:  published: tru
119 [[ 0.39994994]] ---  title: "ワールドカフェの問いを作るには？" date: 2015-06-28T11:27:00+09:00 comments: true category: ['Life'] tag
39 [[ 0.38293162]] ---  title: sublime-vim date: 2013-05-28T21:02:00+09:00 category: ['Tech'] tags:  published: true sl
170 [[ 0.35087206]] --- title: "腰痛におすすめの「やわこ」でのセルフマッサージ" date: 2016-06-25T22:04:38+09:00 comments: true category: ['Life
33 [[ 0.34292003]] ---  title: 屋久島に行くのにあってよかったもの、困ったこと date: 2013-05-15T00:01:00+09:00 category: ['Travel'] tags: ['屋久島
104 [[ 0.32923401]] ---  title: "モレスキンからミドリMDノートに乗り換え(万年筆の利用、価格の観点)" date: 2015-03-01T08:22:00+09:00 comments: true cate
```


<div class="booklink-box" style="text-align:left;padding-bottom:20px;font-size:small;/zoom: 1;overflow: hidden;"><div class="booklink-image" style="float:left;margin:0 15px 10px 0;"><a href="http://www.amazon.co.jp/exec/obidos/asin/4844380605/meganii-22/" target="_blank" ><img src="https://images-fe.ssl-images-amazon.com/images/I/51YzbphP0JL._SL160_.jpg" style="border: none;" /></a></div><div class="booklink-info" style="line-height:120%;/zoom: 1;overflow: hidden;"><div class="booklink-name" style="margin-bottom:10px;line-height:120%"><a href="http://www.amazon.co.jp/exec/obidos/asin/4844380605/meganii-22/" target="_blank" >Python機械学習プログラミング 達人データサイエンティストによる理論と実践 (impress top gear)</a><div class="booklink-powered-date" style="font-size:8pt;margin-top:5px;font-family:verdana;line-height:120%">posted with <a href="http://yomereba.com" rel="nofollow" target="_blank">ヨメレバ</a></div></div><div class="booklink-detail" style="margin-bottom:5px;">Sebastian Raschka インプレス 2016-06-30    </div><div class="booklink-link2" style="margin-top:10px;">                                          	  	  	  	</div></div><div class="booklink-footer" style="clear: left"></div></div>
