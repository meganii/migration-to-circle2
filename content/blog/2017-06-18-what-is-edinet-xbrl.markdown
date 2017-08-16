---
title: "EDINETとXBRLとは何か？Pythonで財務諸表のデータを取得する"
date: 2017-06-18T21:54:26+09:00
lastmod: 2017-06-18T21:54:26+09:00
comments: true
category: ['Tech']
tags: ['FinTech','EDINET','Python']
published: true
slug: what-is-edinet-xbrl
---

## EDINETとは？

- Electronic Disclosure for Investor's NETworkの略
- EDINETは、金融庁により運用されている「金融商品取引法に基づく有価証券報告書等の開示書類に関する電子開示システム」
- 2008年のリニューアルで、財務諸表をXBRL形式による提出が義務付けられた

<!--more-->
{{% googleadsense %}}


## XBRLとは?

- eXtensible Business Reporting Languageの略
- 財務諸表データの表現用途に特化したXMLベースの言語
- 米国の企業情報開示システムEDGARでも採用されていて、財務諸表電子化のグローバルスタンダードな規格


### XBRLの特徴

財務諸表は会計基準・会計規則と密に関係するため、国・地域・業種が異なれば、財務諸表の構成も大きく違うという性質がある。

- 財務諸表の多様性に対応するため、XBRLは柔軟な拡張性を備えている
- XML Schema, XLinkといったXMLの技術を用いて、財務データをタクソノミ(Taxsonomy)とインスタンス(Instance)に二分して表現している
- XBRLのおかげで、XBRLデータを分析システム等に直接取り込むことが可能となり、事務負担の軽減やより高度な財務分析を行うことができる

タクソノミ・・・財務報告の電子的ひな形
インスタンス・・・財務報告内容そのもの


##  EDINETからダウンロードした.xbrl, .xsd, .xmlについて

- .xbrlファイルは「報告書インスタンス」であり、財務諸表の値が記録されている
- 残りの.xsd, .xmlファイルは、「企業別タクソノミ」


## XBRLから流動資産を抽出するサンプルプログラム

[EDINETからXBRLファイルをダウンロード\(個人的メモ\) \- Qiita](http://qiita.com/shima_x/items/c1955743cb5784505ac9)を参考に、まずはPython3に書き換えた。

```python
'''
XBRLから流動資産を抽出するサンプルプログラム
'''

import os
import re
from collections import defaultdict
import xml.etree.ElementTree as ET
from xbrl import XBRLParser
import pandas as pd
import requests


class XbrlParser(XBRLParser):
    def __init__(self, xbrl_filename):
        self.xbrl_filename = xbrl_filename
        self.base_filename = xbrl_filename.replace('.xbrl', '')

    def parse_xbrl(self, namespaces):
        result = defaultdict(dict)
        result['facts'] = self.get_facts_info()

        label_file_name = self.base_filename+'_lab.xml'
        ET.register_namespace('', 'http://www.w3.org/2005/Atom')
        labels = ET.parse(label_file_name)

        # get enterprise taxonomy
        extended_labels = self.get_label_info(namespaces, labels)

        # get base link
        base_labels = self.get_base_label_info(namespaces)

        extended_labels = extended_labels.append(base_labels, ignore_index=True)
        result['labels'] = extended_labels
        result['presentation'] = self.get_presentation_info(namespaces)
        return result

    def get_base_label_info(self, namespaces):
        base_file_path = os.getcwd()+'/base_labels/'
        if not os.path.exists(base_file_path):
            os.mkdir(base_file_path)
        base_labels = None

        # get common taxonomy
        for link_base in self.get_link_base(namespaces):
            file_path = base_file_path + link_base.strip().split('/')[-1]

            if os.path.exists(file_path):
                tmp_base_labels = pd.read_csv(file_path)
            else:
                print('creating ', link_base, 'base label data...')
                response = requests.get(link_base)
                html = response.text
                ET.register_namespace('', 'http://www.xbrl.org/2003/linkbase')
                labels = ET.fromstring(html)
                labels = labels.findall('.//link:labelLink', namespaces=namespaces)[0]

                tmp_base_labels = self.get_label_info(namespaces, labels)
                tmp_base_labels.to_csv(file_path, index=False)
            if base_labels is not None:
                base_labels = base_labels.append(tmp_base_labels, ignore_index=True)
            else:
                base_labels = tmp_base_labels
        return base_labels

    def concat_dictionary(self, dict1, dict2):
        for key in dict1.keys():
            dict1[key] = dict1[key]+dict2[key]
        return dict1

    def get_facts_info(self):
        """
        return(element_id, amount, context_ref, unit_ref, decimals)
        """
        # parse xbrl file
        xbrl = XBRLParser.parse(open(self.xbrl_filename)) # beautiful soup type object
        facts_dict = defaultdict(list)

        #print xbrl
        name_space = 'jp*'
        for node in xbrl.find_all(name=re.compile(name_space+':*')):
            if 'xsi:nil' in node.attrs:
                if node.attrs['xsi:nil'] == 'true':
                    continue

            facts_dict['element_id'].append(node.name.replace(':', '_'))
            facts_dict['amount'].append(node.string)

            facts_dict['context_ref'].append(self.get_attrib_value(node, 'contextref'))
            facts_dict['unit_ref'].append(self.get_attrib_value(node, 'unitref'))
            facts_dict['decimals'].append(self.get_attrib_value(node, 'decimals'))
        return pd.DataFrame(facts_dict)

    def get_attrib_value(self, node, attrib):
        if attrib in node.attrs.keys():
            return node.attrs[attrib]
        else:
            return None

    def get_link_base(self, namespaces):
        label_file_name = self.base_filename+'.xsd'
        ET.register_namespace('', 'http://www.w3.org/2001/XMLSchema')
        labels = ET.parse(label_file_name)
        linkbases = labels.findall('.//link:linkbaseRef', namespaces=namespaces)

        link_base = []
        for link_node in linkbases:
            link_href = link_node.attrib['{'+namespaces['xlink']+'}href']
            if '_lab.xml' in link_href and 'http://' in link_href:
                link_base.append(link_href)
        return link_base

    def get_label_info(self, namespaces, labels):
        """
        return(element_id, label_string, lang, label_role, href)
        """
        label_dict = defaultdict(list)

        #label_file_name = self.base_filename+'_lab.xml'
        #ET.register_namespace('','http://www.w3.org/2005/Atom')
        #labels = ET.parse(label_file_name)

        for label_node in labels.findall('.//link:label', namespaces=namespaces):
            label_label = label_node.attrib['{'+namespaces['xlink']+'}label']

            for labelArc_node in labels.findall('.//link:labelArc', namespaces=namespaces):
                if label_label != labelArc_node.attrib['{'+namespaces['xlink']+'}to']:
                    continue

                for loc_node in labels.findall('.//link:loc', namespaces=namespaces):
                    loc_label = loc_node.attrib['{'+namespaces['xlink']+'}label']
                    if loc_label != labelArc_node.attrib['{'+namespaces['xlink']+'}from']:
                        continue

                    lang = label_node.attrib['{'+namespaces['xml']+'}lang']
                    label_role = label_node.attrib['{'+namespaces['xlink']+'}role']
                    href = loc_node.attrib['{'+namespaces['xlink']+'}href']

                    label_dict['element_id'].append(href.split('#')[1].lower())
                    label_dict['label_string'].append(label_node.text)
                    label_dict['lang'].append(lang)
                    label_dict['label_role'].append(label_role)
                    label_dict['href'].append(href)
        return pd.DataFrame(label_dict)

    def get_presentation_info(self, namespaces):
        """
        return(element_id, label_string, lang, label_role, href)
        """
        type_dict = defaultdict(list)

        label_file_name = self.base_filename+'_pre.xml'
        ET.register_namespace('', 'http://www.w3.org/2005/Atom')
        types = ET.parse(label_file_name)

        for type_link_node in types.findall('.//link:presentationLink', namespaces=namespaces):
            for type_arc_node in type_link_node.findall('.//link:presentationArc',
                                                        namespaces=namespaces):
                type_arc_from = type_arc_node.attrib['{'+namespaces['xlink']+'}from']
                type_arc_to = type_arc_node.attrib['{'+namespaces['xlink']+'}to']

                matches = 0
                for loc_node in type_link_node.findall('.//link:loc', namespaces=namespaces):
                    loc_label = loc_node.attrib['{'+namespaces['xlink']+'}label']

                    if loc_label == type_arc_from:
                        if '{'+namespaces['xlink']+'}href' in loc_node.attrib.keys():
                            href_str = loc_node.attrib['{'+namespaces['xlink']+'}href']
                            type_dict['from_href'].append(href_str)
                            type_dict['from_element_id'].append(href_str.split('#')[1].lower())
                            matches += 1
                    elif loc_label == type_arc_to:
                        if '{'+namespaces['xlink']+'}href' in loc_node.attrib.keys():
                            href_str = loc_node.attrib['{'+namespaces['xlink']+'}href']
                            type_dict['to_href'].append(href_str)
                            type_dict['to_element_id'].append(href_str.split('#')[1].lower())
                            matches += 1
                    if matches == 2: break

                role_id = type_link_node.attrib['{'+namespaces['xlink']+'}role']
                arcrole = type_arc_node.attrib['{'+namespaces['xlink']+'}arcrole']
                order = self.get_xml_attrib_value(type_arc_node, 'order')
                closed = self.get_xml_attrib_value(type_arc_node, 'closed')
                usable = self.get_xml_attrib_value(type_arc_node, 'usable')
                context_element = self.get_xml_attrib_value(type_arc_node, 'contextElement')
                preferred_label = self.get_xml_attrib_value(type_arc_node, 'preferredLabel')

                type_dict['role_id'].append(role_id)
                type_dict['arcrole'].append(arcrole)
                type_dict['order'].append(order)
                type_dict['closed'].append(closed)
                type_dict['usable'].append(usable)
                type_dict['context_element'].append(context_element)
                type_dict['preferred_label'].append(preferred_label)
        return pd.DataFrame(type_dict)

    def get_xml_attrib_value(self, node, attrib):
        if attrib in node.attrib.keys():
            return node.attrib[attrib]
        else:
            return None

    def extract_target_data(self, df, element_id=None, label_string=None, \
                                lang=None, label_role=None, href=None):
        if element_id is not None:
            df = df.ix[df['element_id'] == element_id, :]
        if label_string is not None:
            df = df.ix[df.label_string.str.contains(label_string), :]
        if lang is not None:
            df = df.ix[df['lang'] == lang, :]
        if label_role is not None:
            df = df.ix[df.label_role.str.contains(label_role), :]
        if href is not None:
            df = df.ix[df['href'] == href, :]
        return df

    def gather_descendant(self, df, parent):
        children = df.to_element_id.ix[df.from_element_id == parent]
        return children.append(children.apply(lambda x: self.gather_descendant(df, x)))

    def get_specific_account_name_info(self, dat_fi, df_descendant):
        result = None
        for label_id in df_descendant.ix[:, 0].values:
            if result is None:
                result = dat_fi.ix[dat_fi.element_id == label_id, :]
            else:
                result = result.append(dat_fi.ix[dat_fi.element_id == label_id, :],
                                       ignore_index=True)
        return result

def main(namespaces):
    base_path = os.getcwd()+'/xbrl_files/'
    _dir = 'S100AFWB/XBRL/PublicDoc/'
    xbrl_filename = base_path+_dir+'jpcrp030000-asr-001_E05651-000_2017-03-31_01_2017-06-23.xbrl'

    # get data
    xp = XbrlParser(xbrl_filename)

    print('getting data...')
    xbrl_persed = xp.parse_xbrl(namespaces)
    print('done')

    df_xbrl_facts = xbrl_persed['facts'] # 金額の定義及び文書情報の定義情報
    df_xbrl_labels = xbrl_persed['labels'] # 名称リンク情報
    df_xbrl_presentation = xbrl_persed['presentation'] # 表示リンク情報

    # extract labels data
    df_xbrl_labels = xp.extract_target_data(df_xbrl_labels, lang='ja')
                            #label_role='http://www.xbrl.org/2003/role/documentation')
                            #label_role='documentation')

    # De-duplication of labels data
    df_xbrl_labels = df_xbrl_labels.drop_duplicates()

    dat_fi = pd.merge(df_xbrl_labels, df_xbrl_facts, on='element_id', how='inner')

    # specify duration
    dat_fi_cyi = dat_fi.ix[dat_fi.context_ref == 'CurrentYearInstant'] # 当期 時点
    # 流動資産のelement_idのみ取得
    parent = df_xbrl_labels.element_id.ix[df_xbrl_labels.label_string.str
                                          .contains('^流動資産$')].drop_duplicates()
    print('\n', parent, '\n') # 流動資産のelement_idを表示
    # B/Sの流動資産に関する情報のみ取得
    parent = 'jppfs_cor_currentassetsabstract'
    df_xbrl_ps_cbs = df_xbrl_presentation.ix[df_xbrl_presentation.role_id.str
                                             .contains('rol_ConsolidatedBalanceSheet'), :]
    # 再帰的に流動資産の子要素以下の要素を取得
    df_descendant = xp.gather_descendant(df_xbrl_ps_cbs, parent).dropna() # delete nan
    # 特定の勘定科目の情報のみ取得
    df_fi_cyi_caa = xp.get_specific_account_name_info(dat_fi_cyi, df_descendant)
    # ラベルと金額情報のみ表示
    print(df_fi_cyi_caa[['label_string', 'amount']].drop_duplicates())

if __name__ == '__main__':
    main({
        'link': 'http://www.xbrl.org/2003/linkbase',
        'xml':'http://www.w3.org/XML/1998/namespace',
        'xlink':'http://www.w3.org/1999/xlink',
        'xsi':'http://www.w3.org/2001/XMLSchema-instance'
        })
```


## 参考
- [EDINET](https://disclosure.edinet-fsa.go.jp/EKW0EZ0007.html#2_0)
- [Xbrlについて調べてみた \- Qiita](http://qiita.com/MAIMAI816/items/c9baf4a4e27c146df7c6)
- [EDINETのXBRLファイルから情報抽出 \- Qiita](http://qiita.com/shima_x/items/58634a838ab37c3607b5)
- [EDINETからXBRLファイルをダウンロード\(個人的メモ\) \- Qiita](http://qiita.com/shima_x/items/c1955743cb5784505ac9)
- [金融データ解析の基礎 (シリーズ Useful R 8) ] (https://www.amazon.co.jp/%E9%87%91%E8%9E%8D%E3%83%87%E3%83%BC%E3%82%BF%E8%A7%A3%E6%9E%90%E3%81%AE%E5%9F%BA%E7%A4%8E-%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-Useful-R-8/dp/4320123719/ref=as_li_ss_tl?s=books&ie=UTF8&qid=1498907653&sr=1-1&keywords=%E9%87%91%E8%9E%8D%E3%83%87%E3%83%BC%E3%82%BF%E8%A7%A3%E6%9E%90%E3%81%AE%E5%9F%BA%E7%A4%8E&linkCode=ll1&tag=meganii-22&linkId=d737c50c30bfb1b8803fd9e5b649a9bf)

<a href="https://www.amazon.co.jp/%E9%87%91%E8%9E%8D%E3%83%87%E3%83%BC%E3%82%BF%E8%A7%A3%E6%9E%90%E3%81%AE%E5%9F%BA%E7%A4%8E-%E3%82%B7%E3%83%AA%E3%83%BC%E3%82%BA-Useful-R-8/dp/4320123719/ref=as_li_ss_il?s=books&ie=UTF8&qid=1498907653&sr=1-1&keywords=%E9%87%91%E8%9E%8D%E3%83%87%E3%83%BC%E3%82%BF%E8%A7%A3%E6%9E%90%E3%81%AE%E5%9F%BA%E7%A4%8E&linkCode=li2&tag=meganii-22&linkId=30686364fa1aef12885a4501adcb3e0b" target="_blank"><img border="0" src="//ws-fe.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=4320123719&Format=_SL160_&ID=AsinImage&MarketPlace=JP&ServiceVersion=20070822&WS=1&tag=meganii-22" ></a><img src="https://ir-jp.amazon-adsystem.com/e/ir?t=meganii-22&l=li2&o=9&a=4320123719" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
