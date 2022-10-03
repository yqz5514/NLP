
#%%
# library
import pandas as pd
import spacy
#from spacy.lang.en import English

#E.1:
#In part of this exercise, you will use Spacy software to explore the unrealistic news dataset
#called data.txt.
#i. Use pandas to load the data.csv data.
#ii. Use Spacy to find the word level attributions ( Tokenized word, StartIndex, Lemma,
#punctuation,white space ,WordShape, PartOfSpeech, POSTag). Use one of the titles
#in the dataframe and create a dataframe which rows are the word and the columns are
#attributions.
#iii. Use spacy and find entities on the text in part ii.
#iv. Grab a different title and use spacy to chunk the noun phrases, label them and finally find
#the roots of each chunk.
#v. Use SPacy to analyzes the grammatical structure of a sentence, establishing relationships
#between ”head” words and words which modify those heads. Hint: Insatiate the nlp doc
#and then look for text, dependency, head text, head pos and children of it.
#vi. Use spacy to find word similarly measure. Spacy has word vector model as well. So we
#can use the same to find similar words. Use spacy large model to get a decent results.

#%%
df = pd.read_csv('data.csv')
df.head()
#%%
df.dtypes
#%%

#conts = [x for x in df['title'][2]]
#print(conts)
##%%
#conts1 = [x for x in df['title'].values]
#type(conts1[1])
##%%
#type(conts[2])
#%%
print(df['title'][2])
#%%
nlp = spacy.load("en_core_web_sm")
doc = nlp("BREAKING: Weiner Cooperating With FBI On Hillary Email Investigation")
#%%
# lexical attributes
Index = [token.i for token in doc]
Text = [token.text for token in doc]
is_alpha = [token.is_alpha for token in doc]
is_punct = [token.is_punct for token in doc]
like_num = [token.like_num for token in doc]
lemma = [token.lemma_ for token in doc]
space = [token.is_space for token in doc]
shape = [token.shape_ for token in doc]
pos = [token.pos_ for token in doc]
taggs = [token.tag_ for token in doc]
#token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        #    token.shape_, token.is_alpha, token.is_stop

enti = [ent.label_ for ent in doc.ents]
#%%
for ent in doc.ents:
    print(ent.text, ent.label_)
#%%
title_2 = pd.DataFrame({'words': Text, 'Index': Index, 'Alpha':is_alpha,'Punct':is_punct,'Number':like_num,
                        'Lemma':lemma, 'White Space': space, 'Word Shape':shape, 'POS':pos,'Taggs':taggs,'Entity Name': enti})

#%%
title_2
#%%
doc = nlp(df['title'][3])
#%%
text = [token.text for token in doc]
dep = [token.dep_ for token in doc]
root = [token.head.text for token in doc]

title_3 = pd.DataFrame({'tokens': text, 'Dep':dep, 'Root':root})

#%%
title_3
#%%
#E.2:
#In part of this exercise, you will use Spacy software to explore the tweets dataset called
#data1.txt.
#i. Use pandas to load the data1.csv data.
#ii. Let’s look at some examples of real world sentences. Grab a tweet and explain the text
#entities.
#iii. One simple use case for NER is redact names. This is important and quite useful. Find a
#tweet which has a name in it and then redact it by word [REDACTED].
print(spacy.explain("GPE"))

#%%
# Function to Sanitize/Redact Names
def sanitize_names(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'PERSON':
            redacted_sentences.append("[REDACTED]")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)

#%%
#E.3:
#Use spacy to answer all the following questions.
#i. Apply part of speech Tags methods in spacy on a sentence.
#ii. Apply syntactic dependencies methods in spacy on same sentence that you used on part i.
#iii. Apply named entities methods in spacy on the following sentence ”Apple is looking at
#buying U.K. startup for 1 billion dollar”.
#iv. Apply document similarity on two separate document (2 sentences).
print(doc1.similarity(doc2))