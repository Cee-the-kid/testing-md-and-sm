import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

word1 = nlp("computer")
word2 = nlp("robot")
word3 = nlp("human")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

"""The closest match is between cat and monkey as they are both animals, it is assumed that monkeys like 
to eat bananas that is way that pair is more similar than a cat and a banana"""

"""When using 'en_core_web_md, the similarities were higher than when using 'en_core_web_sm'. 
Upon reading the notes in the terminal after running the program, the smaller module SM does not come 
with word vectors hence not as good as performance as 'md'"""

