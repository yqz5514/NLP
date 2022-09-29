#%%
import spacy

#%%
nlp = spacy.load("en_core_web_sm")
doc = nlp("She ate the pizza")
for token in doc:
    print(token.text, token.pos_)
    
# in spacy, attributes that return strings usually end with underscore_(pos_)
# attributes without underscore return an interger ID value
# pos_ predict tags ...
# %%
