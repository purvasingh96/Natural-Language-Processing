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


