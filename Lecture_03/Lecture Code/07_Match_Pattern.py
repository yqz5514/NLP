# match on Doc objects, not just string
# match on tokens and token attributes
# more flecible: can seach for texts , also other lexical attributes
# also can write rules that uses the model's predictions

#%%
# Match exact token texts
[{"TEXT": "iPhone"}, {"TEXT": "X"}] # match exact token texts

# Match lexical attributes
[{"LOWER": "iphone"}, {"LOWER": "x"}] # match lexical attributes

# Match any token attributes
[{"LEMMA": "buy"}, {"POS": "NOUN"}] # match any token attributes 
# %%
# match patterns are list of dicts, one dict describe one token.
