#%%
from spacy.tokens import Doc, Span
from spacy.lang.en import English
nlp = English()
#%%

words = ["Hello", "world", "!"]
spaces = [True, False, False]

#doc = nlp('Hello World!')
doc = Doc(nlp.vocab, words=words, spaces=spaces)
span = Span(doc, 0, 2)
span_with_label = Span(doc, 0, 2, label="GREETING")# label is optional 
doc.ents = [span_with_label]; print(doc.ents)
# doc.ents : allow us to access the named entities predicted by model
# doc.ents is  writbe, can add entities manually by overwritting it with a list of spans
# %%
print(doc.label_)
# %%
