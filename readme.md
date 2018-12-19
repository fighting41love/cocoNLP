## This is a Chinese nlp package, which can extract information from texts.

[![pypiv](https://img.shields.io/pypi/v/rake-nltk.svg)](https://pypi.org/project/cocoNLP/)
[![Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://www.zhihu.com/people/mountain-blue-64/posts)

## It is developed for a public welfare program, a weibo robot [@寻人微博](https://weibo.com/xrwbyangyangfuture).

## installation
It works well on macOS Mojave with python=3.6.
```
pip install cocoNLP
```

## Directly from the repository

```
git clone https://github.com/fighting41love/cocoNLP.git
cd cocoNLP
python setup.py install
```

## Quick start

### Extract basic information from texts
```
>>> from cocoNLP.extractor import extractor

>>> ex = extractor()

>>> text = '急寻特朗普，男孩，于2018年11月27号11时在陕西省安康市汉滨区走失。丢失发型短发，...如有线索，请迅速与警方联系：18100065143，132-6156-2938，baizhantang@sina.com.cn 和yangyangfuture at gmail dot com'

# 抽取邮箱
>>> emails = ex.extract_email(text)
>>> print(emails)

['baizhantang@sina.com.cn', 'yangyangfuture@gmail.com.cn']
```

```
# 抽取手机号
>>> cellphones = ex.extract_cellphone(text,nation='CHN')
>>> print(cellphones)

['18100065143', '13261562938']
```

```
# 抽取手机归属地、运营商
>>> cell_locs = [ex.extract_cellphone_location(cell,'CHN') for cell in cellphones]
>>> print(cell_locs)

cellphone_location [{'phone': '18100065143', 'province': '上海', 'city': '上海', 'zip_code': '200000', 'area_code': '021', 'phone_type': '电信'}]
```

```
# 抽取地址信息
>>> locations = ex.extract_locations(text)
>>> print(locations)
['陕西省安康市汉滨区', '安康市汉滨区', '汉滨区']
```
```
# 抽取时间点
>>> times = ex.extract_time(text)
>>> print(times)
time {"type": "timestamp", "timestamp": "2018-11-27 11:00:00"}
```
```
# 抽取人名
>>> name = ex.extract_name(text)
>>> print(name)
特朗普

```
### Extract phrases from texts
```
>>> from cocoNLP.config.phrase import rake

>>> r = rake.Rake()

>>> # Extraction given the list of strings where each string is a sentence.
>>> r.extract_keywords_from_sentences(['2015年5月11日，“奶茶妹妹”章泽天分别起诉北京搜狐互联网信息服务有限公司、华某（25岁）名誉权纠纷及成某（38岁）名誉权纠纷二案，要求被诉人公开赔礼道歉、恢复名誉、删除相关视频、断开转载该视频的链接，赔偿经济损失、精神损害抚慰金共计170万元。北京市海淀法院已经受理了这两起案件。原告章泽天诉称，她被许多网友称为“奶茶妹妹”，在网络上获得相当的关注度。2014年4月18日，北京搜狐互联网信息服务有限公司的“搜狐视频娱乐播报调查”节目制作并发布了名为“奶茶妹妹恋情或为炒作，百万炒作团队浮出水面”的视频，该段视频捏造包括“奶茶妹妹走红，实为幕后商业策划”、“100万，奶茶妹妹花巨资，请人策划走红”、“奶茶妹妹在清华大学挂科、作弊、想方设法地转学院”等等。华某在上述节目中捏造了大量的对原告的虚假言论，包括声称其就是原告聘请的“幕后推手和炒作专家”，原告曾花100万聘请其为之宣传策划，原告与刘强东的恋情系两者合作的结果等等。
'],2,4)

>>> # To get keyword phrases ranked highest to lowest.
>>> ranked_words = r.get_ranked_phrases()

>>> # To get keyword phrases ranked highest to lowest with scores.
>>> ranked_words_score = r.get_ranked_phrases_with_scores()

>>> for ele in ranked_words_score:
>>>     print(ele)

(16.0, '要求 被诉人 公开 赔礼道歉')
(15.0, '上述 节目 中 捏造')
(14.5, '该段 视频 捏造 包括')
(14.0, '实为 幕后 商业 策划')
(14.0, '奶茶 妹妹 花 巨资')
(9.5, '删除 相关 视频')
(9.0, '请人 策划 走红')
(9.0, '网络 上 获得')
(9.0, '想方设法 地转 学院')
(9.0, '奶茶 妹妹 走红')
(9.0, '名誉权 纠纷 及成')
(9.0, '名誉权 纠纷 二案')
(8.5, '奶茶 妹妹 恋情')
(8.5, '原告 章泽天 诉称')
(6.0, '奶茶 妹妹')
(5.0, '节目 制作')
(5.0, '幕后 推手')
(5.0, '宣传 策划')
```


## References

This is a python implementation of the algorithm as mentioned in paper [Automatic keyword extraction from individual documents by Stuart Rose, Dave Engel, Nick Cramer and Wendy Cowley](https://www.researchgate.net/profile/Stuart_Rose/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents/links/55071c570cf27e990e04c8bb.pdf)
