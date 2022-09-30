#%%
import spacy

nlp = spacy.load("en_core_web_sm")

#%%
print(nlp.vocab.strings.add("text"))
# .vocab: shared vocabs
#.string: for save memory purpose, all strings are encoded to has IDs, dont need to save multi times when the occurance of word is more than 1
# nlp.vocab.string: is a look up table works in both direction(ID or str)??
#%%
type(nlp.vocab.strings.add("text"))
#%%
coffee_hash = nlp.vocab.strings["text"] #output:15099781594404091470

coffee_string = nlp.vocab.strings[coffee_hash]
print(coffee_string)# output: text
#%%
print(coffee_hash)#output:15099781594404091470


# %%
