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

                chunkgram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""  # specifying what to chunk using reg ex
                chunkparser = nltk.RegexpParser(chunkgram)  # creating a parser
                chunked = chunkparser.parse(tagged)  # using the parser
            return chunked
        except Exception as e:
            print(str(e))
    return process_content()

"""
Usage:
train_data=state_union.raw("2005-GWBUSH.txt")   #takes data from file
sample_data= state_union.raw("2006-GWBUSH.txt")
data1=PunktSentenceTokenizer(train_data)
data2=data1.tokenize(sample_data)
def process_content():
    try:
        for i in data2:             #taking in as sentences from the paragraphs
            words=nltk.word_tokenize(i)    #to words from sentences
            tagged=nltk.pos_tag(words)     #parts of speech tagging

            chunkgram=r"Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"     #specifying what to chunk using reg ex
            chunkparser=nltk.RegexpParser(chunkgram)      #creating a parser
            chunked=chunkparser.parse(tagged)             #using the parser
            print(chunked)
    except Exception as e:
        print(str(e))
process_content()
"""



#a small example
# import nltk
# example="my name is Harsh Patel and i am not a criminal and am beautiful"
# tokenized=nltk.word_tokenize(example)
# tag=nltk.pos_tag(tokenized)
# print(tag)
# chunkgram=r"""FOUND: {<NN.?>*<JJ>*<VB.?>*}"""
# chunkparser=nltk.RegexpParser(chunkgram)
# chunked=chunkparser.parse(tag)
# print(chunked)
# chunked.draw()