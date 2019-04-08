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

*let example = "Hello Miss. Purva Singh! How are you? We are very excited to meet you !!!!"*<br/>
*let example_words = ("draw", "drawing", "drew", "draws") <br/>*

| S.No. | Terminology | Description                                                                                                                                          | Python Library                                                                    | Examples                                                                                                                                                                                                      |
|-------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.    | Tokenizing  | Tokenizing can be considered as a form of grouping a charecter sequence. They are of 2 types -  1. Sentence Tokenizer  2. Word Tokenizer             | ```sent_tokenize(example) word_tokenize(example) ```                   | **SENTENCE TOKENIZER -**<br/>Hello Miss.<br/>Purva Singh!<br/>How are you?<br/>We are very excited to meet you !!!!<br/>  **WORD TOKENIZER -** 'Hello','Miss','.','Purva','Singh','!','How','are','you','?','We','are', 'very','excited','to','meet','you','!','!','!','!'  |
| 2.    | Corpora     | Corpora refers to large collection of texts                                                                                                          | ```import nltk.corpus ```                                                  | medical journals, presidential speech, any English language                                                                                                                                                 |
| 3.    | Lexicon     | Lexicon refers to dictionary of  words and their meanings                                                                                            |                                                                                   | bull - To a financial investor,  the first meaning for the word "Bull"  is someone who <br/>is confident about the market <br/>bull - also an animal                                                                       |
| 4     | Stop Words  | Stop words refers to those set of extra words in  the sentence that we donot need.  They are filler words and w.r.t data analysis,  they are useless | ```from nltk.corpus  import stopwords``` <br/>```  set(stopwords.stop("english"))  ``` |'Hello', 'Miss', '.', 'Purva', 'Singh', '!', 'How', '?', 'We', 'excited', 'meet', '!', '!', '!', '!'                                                                                                                                                                                             |
| 5     | Stemming    | Sometimes words might have variations, due to their tenses. Stemming would normalize the sentences                                                   | ```from nltk.stem import PorterStemmer```<br/> ```ps = PorterStemmer()```                       | Stemming would give a set of **root words.** <br/><br/>ps.stem(example_words) = ("draw", "draw", "drew", "draw")                                         |
| 6     | Tagging     | Part of speech tagging refers to labeling words in a sentence as nouns,  adjectives, verbs, tenses etc.                                              | ```part_of_speech_tag = nltk.pos_tag(tokenized_words)```                                                                                   | (('PRESIDENT', 'NNP'),<br/>  ('members', 'NNS'),<br/>  ('W.', 'NNP'),<br/>  ('THE', 'DT'))<br/><br/>  1. NNP - proper noun<br/> 2. DT - determiner<br/> 3. NNS - noun plural                                                                   |
| 7     | Chunking    | Chunking can be referred  as grouping of words based upon  a regular expression.                                                                     | ```chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""``` | Chunk PRESIDENT/NNP GEORGE/NNP W./NNP BUSH/NNP)<br/> (Chunk ADDRESS/NNP)<br/> (Chunk A/NNP JOINT/NNP SESSION/NNP)                                                                                                     |
| 8     | Chinking    | Chinking can be referred  as exclusion of words, represented by outward curly braces - }(Chinking RegExp){.                                                                     | ```chunkGram = r"""Chunk: {<.*>+}<VB.?>*<NNP>+<NN>?{"""``` |  (Chunk THE/NNP<br/>  CONGRESS/NNP<br/>  ON/NNP<br/>  THE/NNP<br/>  STATE/NNP)                                                                                               |
| 9.    | Named entity  recognition | Main idea behind  Named entity recognition is to chunk "**entities**" such as people, places, things, locations,  monetary figures, and more                                                                      | ```named_entity = nltk.ne_chunk(tagged)```                                                                                                  | ORGANIZATION - Caplan and Gold, <br/>WHO PERSON - Purva Singh <br/> LOCATION - Bhilai, Bangalore <br/>DATE - June, 2019-06-29 <br/>TIME - two fifty a m, 1:30 p.m.                                                                   |
| 10    | Lemmatizing               | Lemmatizing is similar to stemming, but in former, every word  generated is an actual word unlike  stemming. Lemmatizer function takes  an optional parameter **"pos"(part of speech)** which by default is **noun**. | ```from nltk.stem import  WordNetLemmatizer```<br/>```  lemmatizer = WordNetLemmatizer()```<br/>  ```lemmatizer.lemmatize("pretty")```                           | # pretty<br/> print(lemmatizer.lemmatize("pretty"))<br/><br/>  # drawing <br/>print(lemmatizer.lemmatize("drawing", pos='a')) <br/><br/> # good<br/> print(lemmatizer.lemmatize("better", pos='a'))<br/><br/>  # better<br/> print(lemmatizer.lemmatize("better")) |




