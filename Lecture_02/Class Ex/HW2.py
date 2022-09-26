#%%
from itertools import count
#%%
from nltk import word_tokenize
import nltk
from nltk import Text
from collections import Counter
from nltk import FreqDist
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
from bs4 import BeautifulSoup
#%%
import requests
#%%
url = "https://en.wikipedia.org/wiki/Benjamin_Franklin"
html = requests.get(url)

#%%
html.status_code
#%%
html.encoding = 'utf-8' # Optional: requests infers this internally
raw = html.text
#%%
print(raw[:75])

#ii. Use BeautifulSoup to get text file and clean the html file.
#%%

raw1 = BeautifulSoup(raw, 'html.parser').get_text()
tokens = word_tokenize(raw) #print(tokens)
#print(tokens[110:390])
#iii. Write a function called unknown, which removes any items from this set that occur in the
#Words Corpus (nltk.corpus.words).
#%%
words = nltk.corpus.words.words()
#print(words[:20])
#%%
unknown = [x for x in tokens if x not in words ]

#%%
#print(unknown[:10])
#unknown1 = tokens - words

#iv. Fins a list of novel words.
#%%
#print(nltk.corpus.novel.fileids())
#v. Use the porter stemmer to stem all the items in novel words the go through the unknown
#function, saving the result as novel-stems.
porter = nltk.PorterStemmer()
#lancaster = nltk.LancasterStemmer()
# the lancaster stemmer is significantly more aggressive than the porter stemmer
print([porter.stem(t) for t in tokens])

#vi. Find as many proper names from novel-stems as possible, saving the result as propernames.
names = nltk.corpus.names

# %%
from nltk.corpus import brown
print(brown.categories())
# %%
#E.3:
#In part of this exercise, you will use the twitter data.
#i. Load the data and view the first few sentences.
tp = open('twt.txt', 'r', encoding='utf-8')
raw = tp.read()
l = raw.split(sep='.')
print(raw.split(sep='.'))
#ii. Split data into sentences using ”\n” as the delimiter.
sent = raw.split(sep='\n')
#iii. Tokenize sentences (split a sentence into a list of words). Convert all tokens into lower
#case so that words which are capitalized
#%%
sents =  nltk.sent_tokenize(raw)
print(sents[0])
#iv. Split data into training and test sets.
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.05, random_state=0)
#v. Count how many times each word appears in the data.


# %%
