#%%
from spacy.lang.en import English
#%%
nlp = English() # english() contains the processing pipeline and usually assign to variable named nlp

doc = nlp("Hello world!")# aply this pipeline to str will let us access information in structure way

for token in doc:
    print(token.text) # .text shows the contents in where apply
#%%
token = doc[1] # find specicifc position, index into the doc
print(token.text)

#%%
span = doc[1:3]# slice of doc, contain >= 1 tokens
print(span.text)
#%%
doc = nlp("It costs $5.")

# lexical attributes
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])
print("is_alpha:", [token.is_alpha for token in doc])
print("is_punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])
# is_alpha,is_punct,like_num return boolean values
# %%
