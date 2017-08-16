---
title: "edinet xbrl chart of account"
date: 2017-07-02T12:08:52+09:00
lastmod: 2017-07-02T12:08:52+09:00
comments: true
category: ['']
tags: ['']
published: false
slug: edinet-xbrl-chart-of-account
img:
---

<!--more-->
{{% googleadsense %}}


## BS勘定科目

```
jppfs_cor_currentassetsabstract: 流動資産
jppfs_cor_noncurrentassetsabstract: 固定資産
jppfs_cor_liabilitiesabstract: 負債
jppfs_cor_netassetsabstract: 純資産
```

```python
def recursive(array, df, parent_elem_id):
    for val in df.to_element_id.loc[df.from_element_id == parent_elem_id].values:
        array.append(val)
        recursive(array, df, val)

array = []
recursive(array, df_xbrl_ps_cbs, 'jppfs_cor_liabilitiesabstract')


df_fi_cyi_caa = xp.get_specific_account_name(dat_fi_cyi, array).query("label_role == 'http://www.xbrl.org/2003/role/label'").drop_duplicates()
print(df_fi_cyi_caa[['label_string', 'amount']])
```


```json
series: [{
          name: '現金預金等',
          data: [1169409, null],
          stack: 'Credit'
      }, {
          name: '売掛金',
          data: [46840, null],
          stack: 'Credit'
      }, {
          name: '棚卸資産',
          data: [2627138, null],
          stack: 'Credit'
      }, {
          name: 'その他流動資産',
          data: [405844, null],
          stack: 'Credit'
      }, {
          name: '有形固定資産',
          data: [17990, null],
          stack: 'Credit'
      }, {
          name: '無形固定資産',
          data: [49806, null],
          stack: 'Credit'
      }, {
          name: 'その他固定資産',
          data: [19854, null],
          stack: 'Credit'
      }, {
          name: '買掛金',
          data: [4372, null],
          stack: 'Dedit'
      }, {
          name: '有利子負債',
          data: [521575, null],
          stack: 'Dedit'
      }, {
          name: 'その他流動負債',
          data: [864756, null],
          stack: 'Dedit'
      }, {
          name: 'その他固定負債',
          data: [0, null],
          stack: 'Dedit'
      }, {
          name: '純資産',
          data: [2950550, null],
          stack: 'Dedit'
      }, {
          name: '営業原価',
          data: [null, 4596029],
          stack: 'Credit'
      }, {
          name: '販管費',
          data: [null, 710028],
          stack: 'Credit'
      }, {
          name: '営業利益',
          data: [null, 1027949],
          stack: 'Credit'
      }, {
          name: '売上',
          data: [null, 6334008],
          stack: 'Dedit'
      }],
```


```
jppfs_cor_netsales: 売上高
jppfs_cor_costofsales: 売上原価
jppfs_cor_sellinggeneralandadministrativeexpenses: 販売費及び一般管理費
jppfs_cor_operatingincome: 営業利益又は営業損失（△）
```
