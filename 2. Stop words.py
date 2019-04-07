from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "Hello Miss. Purva Singh! How are you? We are very excited to meet you !!!!"
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

meaningful_words = []

for w in words:
    if w not in stop_words:
        meaningful_words.append(w)

print("meaningful words filtered are :: ", meaningful_words)

# meaningful words filtered are ::  ['Hello', 'Miss', '.', 'Purva', 'Singh', '!', 'How', '?', 'We', 'excited', 'meet', '!', '!', '!', '!']