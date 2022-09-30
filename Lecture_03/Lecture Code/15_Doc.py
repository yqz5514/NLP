#%%
from spacy.lang.en import English
nlp = English()

from spacy.tokens import Doc
# Doc is one of the central data structures in spaCy
# and it's created auto when you process a text with nlp object
# doc = nlp('Hello world !) used in preivous notes
#%%
words = ["Hello", "world", "!"]
spaces = [True, False, False] # boolean values indicate whether the word is followed by a space

doc = Doc(nlp.vocab, words=words, spaces=spaces)
# class Doc : takes 3 arguments(shared vocab, the words, spaces)
# %%
print(doc)#Hello world!
# %%
type(doc)#spacy.tokens.doc.Doc
# %%
