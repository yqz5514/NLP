# ------------------Import Library----------------------------
#%%
from nltk.corpus import brown
from nltk import FreqDist
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
from nltk import Text
from collections import Counter
from nltk import FreqDist
from nltk.corpus import wordnet as wn
from nltk.corpus import cmudict
from nltk.corpus import state_union
from nltk.book import *
from urllib import request
import pandas as pd




#-------------------Q1------------------------------
#%%

text = nltk.corpus.genesis.raw()
with open('G.txt', 'w',encoding='utf-8') as f:
    f.write(text)
f.close()


#-------------------Q2------------------------------
#%%
f = open('g.txt', 'r', encoding='utf-8')
raw = f.read()
token = nltk.word_tokenize(raw)
token_seny =  nltk.sent_tokenize(raw)


#-------------------Q3------------------------------
#%%
count_len_sent = [len(x) for x in token_seny]
count_word_sent = [len(nltk.word_tokenize(x)) for x in token_seny]
avg_len_word_sent = sum(count_word_sent)/float(len(count_len_sent))
#%%
sent_tag_frq = nltk.ConditionalFreqDist(token_seny.tagged_words())

conditions = sent_tag_frq.conditions()
for condition in conditions:
	if sent_tag_frq[condition]['NN'] == True:
		print(condition)



#-------------------Q4------------------------------

#%%
df = pd.DataFrame({'Length of the sentence':count_len_sent, 'Number of wordsn':count_word_sent, 'Avg_len_word':avg_len_word_sent,'noun':,'Num_of_noun':,})

df.to_excel('Q2.xlsx')



#-------------------Q5------------------------------

