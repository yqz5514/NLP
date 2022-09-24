from nltk.corpus import brown
import nltk

#%%
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print(unigram_tagger.tag(brown_sents[2007]))
#the UnigramTagger finds the most likely tag for each word in a training corpus, 
# and then uses that information to assign tags to new tokens.

#%%
print(unigram_tagger.evaluate(brown_tagged_sents))
#Score the accuracy of the tagger against the gold standard.
#%%
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print(unigram_tagger.evaluate(test_sents))