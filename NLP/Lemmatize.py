__author__ = 'Harsh'
from nltk.stem import WordNetLemmatizer


def do(input):
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(input)

"""
Usage

lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("better",pos='a'))
print(lemmatizer.lemmatize("London"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("run",'v'))
print(lemmatizer.lemmatize("geese"))
"""
