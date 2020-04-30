__author__ = 'Harsh'
from nltk.tokenize import sent_tokenize,word_tokenize

"""
Usage: 

sentence="This is the world that you all were expecting from me mr. Smith. You Should not worry about too way too much."
print(sent_tokenize(sentence))
print(word_tokenize(sentence))
for i in word_tokenize(sentence):
    print(i)

str=' '.join(i for i in word_tokenize(sentence))    Converting List TO string Again
print(str)
"""

def do_word(input):
    return word_tokenize(input)
def do_sent(input):
    return sent_tokenize(input)