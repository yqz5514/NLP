#**********************************

#%%
import nltk
import string
from spacy.lang.en import English
#**********************************
#==================================================================================================================================================================
# Q1:
# Use the following datframe as the sample data.
# Find the conditional probability occurrence of thw word given a sentiment.
#==================================================================================================================================================================

print(20*'-' + 'Begin Q2' + 20*'-')
#%%

import pandas as pd
df1 = pd.DataFrame({'Word': ['Good', 'Bad', 'Awesome', 'Beautiful', 'Terrible', 'Horrible'],
                     'Occurrence': ['One', 'Two', 'One', 'Three', 'One', 'Two'],
                     'sentiment': ['P', 'N', 'P', 'P', 'N', 'N'],})
df1

#%%
p_occ_sentiment = (p_sent_occ*P_occ)/p_sentiment
neg_p_occ_sent = (5/10)*10/(3/6)
postive_occ_sent = 10*(5/10)/(3/6)




#%%
print(20*'-' + 'End Q2' + 20*'-')

#==================================================================================================================================================================
# Q2:
# Use the following sentence as a sample text. and Answer the following questions.
# 1- Create binary BOW model by counting and remove stop words
# 2- The code should output the features and the vectors associated with the features.
# 3- How many url is in the text.
#==================================================================================================================================================================
print(20*'-' + 'Begin Q2' + 20*'-')
#%%
import pandas as pd

sentences = [
    "I try to get some features out.",
    "Featues can be represented as vectors.",
    "Vectors are easier to explain.",
]
df = pd.DataFrame({'sentences':sentences})
df
#%%
# remove the stop words
from nltk.corpus import stopwords
stop = stopwords.words('english')
def stop_words_removal(df):
    df['sentences_without_stop_words'] = df['sentences'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    print(df)

#%%
stop_words_removal(df)
# %%
#token
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
df['token'] = [tokenizer.tokenize(x) for x in df['sentences']]
print(df)
#%%
df
# %%
from collections import Counter
for i in range(3):
    bow = Counter(df['token'][i])
    print(bow)
#%%
text = ''.join(sentences)
type(text)
# %%
# find url
import re
pattern2 = re.compile(r'https?://\S+|www\.\S+')
matches = pattern2.finditer(text)
for match in matches:
    print(match)
    
#noothing returned, no url in it

