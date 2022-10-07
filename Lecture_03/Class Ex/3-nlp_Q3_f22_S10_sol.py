#%%
import pandas as pd
import spacy

#%%
nlp = spacy.load("en_core_web_sm")
df = pd.read_excel('NER.xlsx').head(100)

def replace_ner(mytxt):
    clean_text = mytxt
    doc = nlp(mytxt)
    for ent in reversed(doc.ents):
        clean_text = clean_text[:ent.start_char] + '******' + clean_text[ent.end_char:]
    return clean_text

df['Redacted'] = df['Sentences'].apply(lambda x:replace_ner(x) )
df.to_excel('NER_redacted.xlsx')
print(df)
# %%
