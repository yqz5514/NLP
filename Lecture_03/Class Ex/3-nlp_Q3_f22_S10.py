# ------------------Import Library----------------------------
#%%
import pandas as pd
import spacy
# ------------------Main Loop----------------------------
#%%

# ------------------Part i----------------------------
data = pd.read_excel(r'NER.xlsx',engine='openpyxl')
#%%
print(data)
#%%
data.columns
#%%
nlp = spacy.load("en_core_web_sm")
new_data = ' '.join(data[data['Sentences']])
#%%
print(new_data)
#%%
#doc = nlp(new_data)
# ------------------Part ii----------------------------
#%%
def get_replace(text):
 #for i in text:
     
    doc = nlp(text)
    redacted_sentences = []
    for ent in doc.ents:
        ent.merge()
    for token in doc:
        if token.ent_type_ == 'PERSON':
            redacted_sentences.append("[*]")
        elif token.ent_type_ == 'GPE':
            redacted_sentences.append("[*]")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)
#%%
redacted = get_replace(new_data)
# ------------------Part iii----------------------------
#%%
new_file = pd.DataFrame({'redacted': redacted})
new_file.to_excel('NLTK_Feature_Extraction.xlsx')


# %%
#1. Download and load the NER.xlsx a from BB read it through python.
# 2. Find all the location, names, cities and generally all entities and replace them with asterisk. 
# 3. Save all the redacted version of the sentence into a column and save it into a new excel file.