#%%
from nltk.book import text1
from nltk.book import text4
from nltk.book import text6

#%%
print(text1.concordance("monstrous"))
#NLTK provides the function concordance() to locate and print series of phrases that contain the keyword. However, the function only print the output. The user is not able to save the results for further processing unless redirect the stdout.

#%%
print(text1.similar("monstrous"))
#Using similar(token) returns a list of words that appear in the same context as token. In this case the the context is just the words directly on either side of token.

# one way find similarity, detect freq of the target words's front waord or after words, then detact similiar word by locate the before/after word with high freq 
#%%
print(text1.collocations())
#Collocations are two or more words that tend to appear frequently together,
#text1.common_contexts('','')
#%%
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
#Lexical dispersion is a measure of how frequently a word appears across the parts of a corpus. This plot notes the occurrences of a word and how many words from the beginning of the corpus it appears (word offsets).

#%%
print(text6.count("Very"))
print(text6.count('the') / float(len(text6)) * 100)
#%%
print(text4.count("bless"))
#%%
print(text4[100])
#%%
print(text4[0:10])
#%%
print(text4[3])
#%%
print(text4.index('the'))
#%%
print(text4[524])
print(text4.index('men'))
print(text4[0:len(text4)])



