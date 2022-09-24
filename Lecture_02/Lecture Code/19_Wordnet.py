#%%
from nltk.corpus import wordnet as wn
#%%
print(wn.synsets('motorcar'))
#%%
print(wn.synset('car.n.01').lemma_names())
#%%
print(wn.synset('car.n.01').definition())
#%%
print(wn.synset('car.n.01').examples())
#%%
print(wn.synset('car.n.01').lemmas())
#%%
print(wn.lemma('car.n.01.automobile'))
#%%
print(wn.lemma('car.n.01.automobile').synset())
#%%
print(wn.lemma('car.n.01.automobile').name())
#%%
print(wn.synsets('car'))
#%%

for synset in wn.synsets('car'):
    print(synset.lemma_names())
#%%
print(wn.lemmas('car'))

#%%
motorcar = wn.synset('car.n.01'); print(motorcar)
#%%
types_of_motorcar = motorcar.hyponyms()
#%%
sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())
#%%
print(motorcar.hypernyms())
#%%
paths = motorcar.hypernym_paths()
#%%
print([synset.name() for synset in paths[0]])
#%%
print([synset.name() for synset in paths[1]])
# %%
