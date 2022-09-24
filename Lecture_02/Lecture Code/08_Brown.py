#%%
from nltk.corpus import brown
import nltk
#%%

print(brown.categories())
#%%
print(brown.words(categories='news'))
# categorical means genre in brown cropus
#%%
print( brown.words(fileids=['cg22']))

#%%
print(brown.sents(categories=['news', 'editorial', 'reviews']))
#%%
#from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
#In NLP Modal Operators of Necessity relates to words, 
#which form the rules in our lives (should, must, have to, etc.)
# Modal Operator of Possibility relates to words that denote that which is considered possible (can, cannot, etc.).

for m in modals:
    print(m + ':', fdist[m], end=' ')
    #
#%%
fd = nltk.FreqDist((genre, word)
      for genre in brown.categories()
      for word in brown.words(categories=genre))
#%%
print(fd.most_common(5))

#%%
cfd = nltk.ConditionalFreqDist((genre, word)
            for genre in brown.categories()
            for word in brown.words(categories=genre))
#%%
print(cfd)
#%%

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
print(); print(cfd.tabulate(conditions=genres, samples=modals))
# %%
