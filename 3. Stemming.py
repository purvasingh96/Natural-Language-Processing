from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["draw", "drawing", "drew", "draws"]
example_text = "Purva was making her drawing. She drew the sketch beautifully. She draws her sketches in the evenings only. Purva likes to draw"

print("stemming for example words")
for w in example_words:
    print(ps.stem(w))

print("stemming for example text")
tokenized_words=word_tokenize(example_text)
for w in tokenized_words:
    print(ps.stem(w))