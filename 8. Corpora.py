from nltk.corpus import movie_reviews
from nltk.tokenize import sent_tokenize

sample = movie_reviews.raw("pos/cv000_29590.txt")

tok = sent_tokenize(sample)
print(tok[5:15])