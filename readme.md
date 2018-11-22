### This is a Chinese nlp repo, which can extract key phrase from texts.

## installation
```
pip install cocoNLP
```

## Directly from the repository

```
git clone https://github.com/fighting41love/cocoNLP.git
python setup.py install
```

## Quick start
```
from cocoNLP import rake
r = rake.Rake()

r.extract_keywords_from_text(texts, 2, 4)

# Extraction given the list of strings where each string is a sentence.
r.extract_keywords_from_sentences(['我是一个兵,热爱祖国，热爱人民。我特别热爱人民。','我是一个好人'])

# To get keyword phrases ranked highest to lowest.
ranked_words = r.get_ranked_phrases()

print(ranked_words)

# To get keyword phrases ranked highest to lowest with scores.
ranked_words_score = r.get_ranked_phrases_with_scores()
for ele in ranked_words_score:
    print(ele)
```


## References

This is a python implementation of the algorithm as mentioned in paper [Automatic keyword extraction from individual documents by Stuart Rose, Dave Engel, Nick Cramer and Wendy Cowley](https://www.researchgate.net/profile/Stuart_Rose/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents/links/55071c570cf27e990e04c8bb.pdf)
