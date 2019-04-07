import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_tokenizer.tokenize(sample_text)

def process_text():
    try:
        for words in tokenized[:5]:
            tokenized_words=nltk.tokenize(words)
            part_of_speech_tag = nltk.pos_tag(tokenized_words)
            print(part_of_speech_tag)

    except Exception as e:
        print(str(e))


process_text