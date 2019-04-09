import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(file_id)), category)
             for category in movie_reviews.categories()
             for file_id in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print(all_words)