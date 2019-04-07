from nltk.tokenize import sent_tokenize, word_tokenize



example_text = "Hello Miss. Purva Singh! How are you? We are very excited to meet you !!!!"

print("SENTENCE TOKENIZER")
for i in sent_tokenize(example_text):
    print(i)

print("WORD TOKENIZER")
for i in word_tokenize(example_text):
    print(i)