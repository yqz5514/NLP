#%%
from nltk.book import *
import nltk

print(text1.vocab())
print(type(text1))
print(len(text1))


#%%

from nltk.corpus import gutenberg
print(gutenberg.fileids())# what kind of gutenberg project we are working on 
print(nltk.corpus.gutenberg.fileids())
hamlet = gutenberg.words('shakespeare-hamlet.txt')
print(hamlet[0:20])
#%%
hamlet.sp

#%%

from nltk.corpus import inaugural
print(inaugural.fileids())
print(nltk.corpus.inaugural.fileids())
from nltk.text import Text
former_president = Text(inaugural.words(inaugural.fileids()[-1]))
print(' '.join(former_president.tokens[0:1000]))
#The join() method provides a flexible way to create strings from iterable objects. It joins each element of an iterable (such as list, string, and tuple) by a string separator (the string on which the join() method is called) and returns the concatenated string.
