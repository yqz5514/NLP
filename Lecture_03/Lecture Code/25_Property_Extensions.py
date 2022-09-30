#%%
from spacy.tokens import Token
import spacy
nlp = spacy.load("en_core_web_sm")
#%%
def get_is_color(token):
    colors = ["red", "yellow", "blue"]
    return token.text in colors

Token.set_extension("is_colour", getter=get_is_color) # getter functions only called when retrieve the sttribute

doc = nlp("The sky is blue.")
print(doc[3]._.is_colour, "-", doc[3].text)
# %%
