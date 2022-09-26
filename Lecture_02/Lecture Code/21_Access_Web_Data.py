#%%
from urllib import request
from nltk import word_tokenize
import  nltk

#%%

url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
#%%
raw = response.read().decode('utf8')
print(type(raw));print(len(raw));print(raw[:75])
#%%

tokens = word_tokenize(raw)
print(type(tokens))
#%%
print(tokens[:10])
#%%
text = nltk.Text(tokens)
#%%
print(type(text))
#%%
print(text[:10])
#%%
print(text.collocations())
#Collocations are two or more words that tend to appear frequently together,

# %%
raw1 = response.read().decode('utf8')
#%%
text1 = nltk.Text(raw1)
print(text1[:10])
# %%
print(raw1[:100])
# %%
