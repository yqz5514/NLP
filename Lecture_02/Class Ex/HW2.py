#%%
from itertools import count
from nltk import word_tokenize
import nltk
from nltk import Text

# E.1:
#In part of this exercise, you will use nltk to explore the Moby Dick text.
#i. Analyzing Moby Dick text. Load the moby.txt file into python environment. (Load the
#raw data or Use the NLTK Text object)
#%%
f = open('moby.txt', 'r', encoding='utf-8')
raw = f.read()

#ii. Tokenize the text into words. How many tokens (words and punctuation symbols) are in
#it?
#%%
token = word_tokenize(raw)
print(len(token))
#%%
from collections import Counter
print(Counter(token))
#iii. How many unique tokens (unique words and punctuation) does the text have?
#%%
uniq = set(token)
print(uniq)
print(len(uniq))
#iv. After lemmatizing the verbs, how many unique tokens does it have?
#%%
wnl = nltk.WordNetLemmatizer()
le_to = [wnl.lemmatize(t) for t in token]

print(len(set(le_to)))
#v. What is the lexical diversity of the given text input?
#%%
moby_diversity = float(len(uniq))/float(len(token))
moby_dicersity_lemm = float(len(set(le_to)))/float(len(le_to))
print(f'Moby.txt lexical diversity is: {round(moby_diversity * 100, 2)}%')
print(f'Moby.txt lexical diversity after lemmatiziation is: {moby_dicersity_lemm * 100}%')

#vi. What percentage of tokens is ’whale’or ’Whale’?
#%%
moby_frequencies = nltk.FreqDist(token)
whale = moby_frequencies['whale'] + moby_frequencies['Whale']
print(f'Percentage of whale is:{round(float(whale)*100/float(len(token)), 2)}%')

#vii. What are the 20 most frequently occurring (unique) tokens in the text? What is their
#frequency?
#%%
print(f'Top 20 most commont words:{moby_frequencies.most_common(20)}')
#viii. What tokens have a length of greater than 6 and frequency of more than 160?
#%%
import pandas as pd
#%%
moby_frequency_frame = pd.DataFrame(moby_frequencies.most_common(),
                                        columns=["token", "frequency"])
target = moby_frequency_frame[(moby_frequency_frame['frequency']>160) & (moby_frequency_frame.token.str.len() >6)]
print(target)
#ix. Find the longest word in the text and that word’s length.
#%%
longest_word_length = max(moby_frequency_frame.token.str.len())
#print(moby_frequency_frame[moby_frequency_frame['frequency'] == longest_word_length] )
longest = moby_frequency_frame.token.str.extractall("(?P<long>.{{{}}})".format(longest_word_length))
print(longest.long.iloc[0], longest_word_length)
# why there are many 23 length but looks shot str 

#x. What unique words have a frequency of more than 2000? What is their frequency?
# check wether words or not
#%%
moby_words = moby_frequency_frame[moby_frequency_frame.token.str.isalpha()]
common = moby_words[moby_words['frequency'] > 2000]
print(list(zip(common.token, common.frequency)))

#xi. What is the average number of tokens per sentence?
#%%
sents = nltk.sent_tokenize(raw)
counts = [len(nltk.word_tokenize(x)) for x in sents]
avg = sum(counts)/float(len(sents))
print(avg)

#xii. What are the 5 most frequent parts of speech in this text? What is their frequency?
#%%
tagged = nltk.pos_tag(token)
tag_fq = nltk.FreqDist(y for (x,y) in tagged)
print(tag_fq.most_common(5))
# %%
#E.2:
#Lets get some text file from the Benjamin Franklin wiki page.
#i. Write a function that scrape the web page and return the raw text file.

#%%
from urllib import request
from bs4 import BeautifulSoup
#%%
url = "https://en.wikipedia.org/wiki/Benjamin_Franklin(HTML_parser)"
html = request.urlopen(url)
#raw = response.read().decode('utf8')
#%%

raw = BeautifulSoup(html, 'html.parser').get_text()
tokens = word_tokenize(raw); print(tokens)
print(tokens[110:390])
#ii. Use BeautifulSoup to get text file and clean the html file.

#iii. Write a function called unknown, which removes any items from this set that occur in the
#Words Corpus (nltk.corpus.words).
#iv. Fins a list of novel words.
#v. Use the porter stemmer to stem all the items in novel words the go through the unknown
#function, saving the result as novel-stems.
#vi. Find as many proper names from novel-stems as possible, saving the result as propernames.

