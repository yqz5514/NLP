import spacy
#%%
nlp = spacy.load("en_core_web_sm")

doc = nlp("I love natural language processing.")
lexeme = nlp.vocab["natural"]
#%%
print(lexeme)

#%%
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
# lexeme object is an entry in the vocalbulary
# %%
# lexeme object is an entry in the vocalbulary
# lexemes expose features 
# Difference between token: no POS tags, dependencies or entity labels
