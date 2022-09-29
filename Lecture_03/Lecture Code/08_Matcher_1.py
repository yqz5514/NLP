#%%
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")

#%%
matcher = Matcher(nlp.vocab)# initialized with shared vocab : nlp.vocab
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern]) # use .add() to add pattern 
# in .add(), the first argument is unique ID to identify which pattern was matched
# the second argument is pattern 

doc = nlp("Upcoming iPhone X release date leaked")

matches = matcher(doc)

# %%
print(matches)
# output: [(9528407286733565721, 1, 3)] # tuple
# [(match ID, the starte index of matched span, the end index of matched span)]
# %%
