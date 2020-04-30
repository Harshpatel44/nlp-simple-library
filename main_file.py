
import NLP.NLP as nlp

print("Word Tokenization: ", nlp.process.word_tokenize("this is my NLP library and it does basic nlp processing."))
# Word Tokenization:  ['this', 'is', 'my', 'NLP', 'library', 'and', 'it', 'does', 'basic', 'nlp', 'processing', '.']

print("Sentence Tokenization:", nlp.process.sent_tokenize("this is my NLP library and it does basic nlp processing."))
# Sentence Tokenization: ['this is my NLP library and it does basic nlp processing.']

print("Stopwords Removal:", nlp.process.stopwords("this is my NLP library and it does basic nlp processing."))
# Stopwords Removal: ['NLP', 'library', 'basic', 'nlp', 'processing', '.']

print("Stemming: ", nlp.process.stem("this is my NLP library and it does basic nlp processing."))
# Stemming:  ['thi', 'is', 'my', 'nlp', 'librari', 'and', 'it', 'doe', 'basic', 'nlp', 'process', '.']

print("POS tagging: ", nlp.process.pos_tag("this is my NLP library and it does basic nlp processing."))
"""
POS tagging:  [('this', 'DT'), ('is', 'VBZ'), ('my', 'PRP$'), ('NLP', 'JJ'), ('library', 'NN'), ('and', 'CC'), 
('it', 'PRP'), ('does', 'VBZ'), ('basic', 'JJ'), ('nlp', 'NN'), ('processing', 'NN'), ('.', '.')] 
"""

print("lemmatizing: ", nlp.process.lemmatize("this is my NLP library and it does basic nlp processing."))
# lemmatizing:  this is my NLP library and it does basic nlp processing.

print("Chunking: ", nlp.process.chunk("this is my NLP library and it does basic nlp processing."))
"""
Chunking:  (S
  this/DT
  is/VBZ
  my/PRP$
  NLP/JJ
  library/NN
  and/CC
  it/PRP
  does/VBZ
  basic/JJ
  nlp/NN
  processing/NN
  ./.)
  """





