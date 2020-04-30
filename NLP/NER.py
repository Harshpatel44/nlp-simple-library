__author__ = 'Harsh'
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

def do(input):
    ps = PorterStemmer()
    words = word_tokenize(input)
    return nltk.pos_tag(words)


"""
usage:

a=[]

from nltk.corpus import stopwords

ps=PorterStemmer()
sentence="what is the weather in Vadodara "
words=word_tokenize(sentence)
stop_words=set(stopwords.words("english"))
for i in words:
    if(i not in stop_words):
        a.append(ps.stem(i))
tagged=nltk.pos_tag(a)
print(tagged)
name_entity=nltk.ne_chunk(tagged,binary=False)      #Named Entity Representation
print(name_entity)
name_entity.draw()
result=list(name_entity)
"""

"""NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian"""