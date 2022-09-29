#%%
import spacy
#%%
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.label_)
# %%
# doc.ents : allow us to access the named entities predicted by model
# .label : print the entity text and entity label 
