#%%
import spacy

#%%
nlp = spacy.load("en_core_web_sm")
doc = nlp("She ate the pizza")
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

# .dep attribute returns the predicted dependency label
# .head returns the syntactic head token(parent token this word is attached )
#The verb is usually the head of the sentence(root). All other words are linked to the headword.
#Dependency parsing define the dependency relationship between headwords and their dependents. 