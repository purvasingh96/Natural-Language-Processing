# Natural-Language-Processing 

## 1. Downloading NLTK
1. pip installation 
```python
pip install nltk
```
2. Downloading nltk's components 
```python
>>import nltk
>>nltk.download('all')
```

# Terminologies related to NLP
## 1. Tokenizing
Tokenizing can be considered as a form of grouping a charecter sequence. The groups are called *tokens*. They are of 2 types - 
1. Sentence Tokenizer (sent_tokenize) 
    * Recognizes every punctuation as separate word.
2. Word Tokenizer (word_tokenize) 
  a. Recognizes every punctuation as a separate word.

## 2. Corpora, Lexicon and Stop Words
* *Corpora* refers to large collection of texts. E.g- medical journals, presidential speech, any English language.  
* *Lexicon* refers to dictionary of words and their meanings.  
* *Stop words* refers to those set of extra words in the sentence that we donot need. They are filler words anfd w.r.t data analysis, the are useless. e.g. a, an, the, of


