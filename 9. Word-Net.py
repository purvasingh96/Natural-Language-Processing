from nltk.corpus import wordnet

# synonyms of funny - funny_story, amusing, curious, fishy, funny
synonym = wordnet.synsets("funny")

# prints entire set
print(synonym)

# prints just the word - funny_story
print(synonym[0].lemmas()[0].name())

#prints definition
# funny_story -  an account of an amusing incident (usually with a punch line)
print(synonym[0].definition())

#prints examples
# ['she told a funny story', 'she made a funny']
print(synonym[0].examples())

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
        # if lemma.antonyms:
        #     antonyms.append(lemma.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

w1 = wordnet.synset("good.n.01")
w2 = wordnet.synset("better.n.01")

print("similarity percent")
print(w1.wup_similarity(w2))