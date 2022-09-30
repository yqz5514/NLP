# python -m spacy download en_core_web_md
#%%
import spacy
nlp = spacy.load("en_core_web_md")
# Doc, Token, Span objects have .similarity method
# it take another object and return floating num bwtween 0 and 1 indicating how similar they are

#%%
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))

#%%
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))
# %%
