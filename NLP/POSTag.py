__author__ = 'Harsh'

import nltk
from nltk.corpus import state_union                      #taking the data from state union
from nltk.tokenize import PunktSentenceTokenizer

def do(input):
    train_data = state_union.raw("2005-GWBUSH.txt")  # takes data from file
    data1 = PunktSentenceTokenizer(train_data)
    data2 = data1.tokenize(input)

    def process_content():
        try:
            for i in data2:  # taking in as sentences from the paragraphs
                words = nltk.word_tokenize(i)  # to words from sentences
                tagged = nltk.pos_tag(words)  # parts of speech tagging
            return tagged
        except Exception as e:
            print(str(e))

    return process_content()


"""
usage:
train_data = state_union.raw("2005-GWBUSH.txt")  # takes data from file
sample_data= state_union.raw("2006-GWBUSH.txt")
data1 = PunktSentenceTokenizer(train_data)
data2 = data1.tokenize(sample_data)

def process_content():
    try:
        for i in data2:  # taking in as sentences from the paragraphs
            words = nltk.word_tokenize(i)  # to words from sentences
            tagged = nltk.pos_tag(words)  # parts of speech tagging
            print(tagged)
    except Exception as e:
        print(str(e))

process_content()
"""

"""  
Basic mathod to use parts of speech
example="This is the best thing condider to do for you and the way it feels to make me feel."
words=nltk_work.word_tokenize(example)      #tokenizing
tagged=nltk_work.pos_tag(words)             #using parts of speech tagging
print(tagged)
"""

# Approach2: simple method
# data="The author walked in the city with Jane"
# words=nltk.word_tokenize(data)    #to words from sentences
# tagged=nltk.pos_tag(words)     #parts of speech tagging
# print(tagged)


"""
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'f
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when

"""