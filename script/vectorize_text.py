# -*- coding: utf-8 -*-

''' vector2word '''
import re
from collections import defaultdict
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def mecab_analyzer(doc, to_stem=True):
    ''' mecab '''
    ptn = re.compile(r'<.*?>')
    tagger = MeCab.Tagger('mecabrc')  # 別のTaggerを使ってもいい
    mecab_result = tagger.parse(ptn.sub("", doc))
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

#pylint:disable=C0103
def tf(doc):
    ''' TF '''
    vectorizer = CountVectorizer(analyzer=mecab_analyzer, token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(doc)
    terms = vectorizer.get_feature_names()
    return features, terms

def tfidf(docs):
    ''' TF-IDF '''
    vectorizer = TfidfVectorizer(
        analyzer=mecab_analyzer,
        min_df=1,
        max_df=50,
        token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(docs)
    terms = vectorizer.get_feature_names()
    return features, terms

def get_docslist(filepath):
    ''' Get docslist'''
    file = open(filepath, 'r')
    lines = file.readlines()
    return [re.sub(r"[0-9].+?|\/|\"|\(|\)", "", l) for l in lines]

def get_filelist(filepath):
    ''' Get file list '''
    file = open(filepath, 'r')
    lines = file.readlines()
    return [l.replace('\n', '').split('\t') for l in lines]

def get_related_posts(docs, tfidf_mtx):
    '''
    それぞれのドキュメントに類似するドキュメントの２次元配列を返す。
    [
     [docNo, docNo],
     []
     ...
    '''
    cos_table = []
    for index in range(0, len(docs)):
        s = defaultdict(int)
        for i, tfidfv in enumerate(tfidf_mtx):
            if i == index:
                s[i] = 0
                continue
            cos = cosine_similarity(tfidf_mtx[index].reshape(1, -1), tfidfv.reshape(1, -1))
            s[i] = cos
        top_cos = sorted(s.items(), key=lambda t: t[1], reverse=True)
        top_cos = filter(lambda t: t[1] > 0.05, top_cos)
        cos_table.append(list(top_cos))
    return cos_table

def main():
    ''' main '''
    filelist = get_filelist('tmp/filenamelist.txt')
    docs = get_docslist('tmp/contents.txt')

    features, _ = tfidf(docs)
    tfidf_mtx = features.toarray()

    relatedposts = get_related_posts(docs, tfidf_mtx)

    yml = open('data/relatedposts.yml', 'w')
    yml.write('Url:\n')

    try:
        for i, posts in enumerate(relatedposts):
            if len(posts) > 0:
                yml.write('  ')
                yml.write(filelist[i][0])
                yml.write(':\n')
                cnt = 1
                for key, _ in posts:
                    yml.write("    {0}:\n".format(cnt))
                    yml.write("      title: {0}\n".format(filelist[key][2]))
                    yml.write("      link: {0}\n".format(filelist[key][1]))
                    cnt += 1
    except:
        print("error")
    finally:
        print("end")
        yml.close()

if __name__ == '__main__':
    main()
