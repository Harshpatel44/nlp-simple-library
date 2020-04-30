import NLP.Tokenize as Tokenize
import NLP.StopWords as StopWords
import NLP.Stem as Stem
import NLP.POSTag as POSTag
import NLP.NER as NER
import NLP.Lemmatize as Lemmatize
import NLP.Chunk as Chunk
import NLP.Chink as Chink

class process():
    def __init__(self):
        pass
    def word_tokenize(input):
        return Tokenize.do_word(input)
    def sent_tokenize(input):
        return Tokenize.do_sent(input)
    def stopwords(input):
        return StopWords.do(input)
    def stem(input):
        return Stem.do(input)
    def pos_tag(input):
        return POSTag.do(input)
    def ner(input):
        return NER.do(input)
    def lemmatize(input):
        return Lemmatize.do(input)
    def chunk(input):
        return Chunk.do(input)
    def chink(input):
        return Chink.do(input)