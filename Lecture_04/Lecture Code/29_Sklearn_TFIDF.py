#%%
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?',
 ]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)# TF*IDF
#print(vectorizer.get_feature_names())
#print(X.shape)
# embedding
# number of features 9
# what is meaning about TFIDF??????

# %%
vectorizer.get_feature_names()
#%%
print(X)
# %%
type(vectorizer.get_feature_names())
# %%
