from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# pretty
print(lemmatizer.lemmatize("pretty"))

# drawing
print(lemmatizer.lemmatize("drawing", pos='a'))

# good
print(lemmatizer.lemmatize("better", pos='a'))

# better
print(lemmatizer.lemmatize("better"))
