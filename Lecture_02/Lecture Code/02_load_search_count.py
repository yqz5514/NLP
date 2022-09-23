#%%
from nltk.book import *
import nltk

print(text1.vocab())
print(type(text1))
print(len(text1))


#%%

from nltk.corpus import gutenberg
print(gutenberg.fileids())# what kind of gutenberg project we are working on 
#%%
print(nltk.corpus.gutenberg.fileids())
#%%
hamlet = gutenberg.words('shakespeare-hamlet.txt')
print(hamlet[0:20])


#%%

from nltk.corpus import inaugural
print(inaugural.fileids())
print(nltk.corpus.inaugural.fileids())
#%%
#Text. A wrapper around a sequence of simple (string) tokens, which is intended to support initial exploration of texts (via the interactive console). Its methods perform a variety of analyses on the text's contexts (e.g., counting, concordancing, collocation discovery), and display the results.

from nltk.text import Text
former_president = Text(inaugural.words(inaugural.fileids()[-1]))
print(former_president[0:20])
type(former_president)# different type from below without Text() function
#%%
former_president.tokens[0:10]
#%%
former_president = inaugural.words(inaugural.fileids()[-1])
print(former_president[0:20])
type(former_president)
#former_president.tokens[0:10] wont work becasue it's not text type

#%%
print(' '.join(former_president.tokens[0:1000]))
#The join() method provides a flexible way to create strings from iterable objects. It joins each element of an iterable (such as list, string, and tuple) by a string separator (the string on which the join() method is called) and returns the concatenated string.
