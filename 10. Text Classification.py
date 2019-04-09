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

# order from most common to least common words
all_words = nltk.FreqDist(all_words)
print(all_words)

# list of most common 3000 words
word_features = list(all_words.keys())[:3000]

# this function will search if most common words
# is present in document as well
# then append it to features list

def find_features(document):
    words = set(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
    return features

print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
