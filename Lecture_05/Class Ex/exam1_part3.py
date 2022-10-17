#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

#%%
# check data
test = pd.read_csv('Test.csv')
test.head(10)
# %%
train = pd.read_csv('Train.csv')
train.head(10)
# %%
test.isnull().sum()
#title               152
# %%
train.isnull().sum()
#title               560
# %%
train.info
# %%
test.info
# %%
test.dropna(how = 'any', inplace=True)
# %%
test.isnull().sum()

# %%
train.dropna(how = 'any', inplace=True)

# %%
# text ppreprocessing
train.groupby('urgency').describe()
#%%
test.groupby('urgency').describe()#0123
#%%
train1 = train.copy()
#%%
train1['text_len'] = train1.body.apply(len)
train1.head()
#%%
train1[train1.urgency==0].describe() # max text len:5154
#%%
train1[train1.urgency==1].describe() # max text len:5789
#%%
train1[train1.urgency==2].describe() # max text len:6867
#%%
train1[train1.urgency==3].describe() # max text len:7011
#%%
#sms[sms.message_len == 910].message.iloc[0]
train1[train1.text_len == 7011].body.iloc[0]

#%%
#remove dstopwords
import string
from nltk.corpus import stopwords
def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    STOPWORDS = stopwords.words('english') + ['u', 'ü', 'ur', '4', '2', 'im', 'dont', 'doin', 'ure']
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return ' '.join([word for word in nopunc.split() if word.lower() not in STOPWORDS])
# from kaggle notebook text_processing_use_nlp

#%%
train['clean_text'] = train.body.apply(text_process)

#%%
train.head()

#%%
#remove rare word
freq = pd.Series(' '.join(train['clean_text']).split()).value_counts()[-20:]
freq

#%%
freq = list(freq.index)
def rare_words_removal(df):
    df['clean_text'] = df['clean_text'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
    print(df['clean_text'].head())
#%%
rare_words_removal(train)

# %%
from collections import Counter
freq = pd.Series(' '.join(train['clean_text']).split()).value_counts()[:20]#take a look at top 10 words
#%%
freq= list(freq.index)
def frequent_words_removal(df):    
    df['clean_text'] = df['clean_text'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
    print(df['clean_text'].head())
# %%
frequent_words_removal(train)
# %%
# split x and y
X = train.clean_text
y = train.urgency
print(X.shape)
print(y.shape)
# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
# %%
from sklearn.feature_extraction.text import CountVectorizer

# instantiate the vectorizer
vect = CountVectorizer()
vect.fit(X_train)
#%%
X_train_dtm = vect.fit_transform(X_train)
#%%
X_test_dtm = vect.transform(X_test)
X_test_dtm

#%%
from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
tfidf_transformer.fit(X_train_dtm)
X_train_tfidf = tfidf_transformer.transform(X_train_dtm)
# %%
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)
X_test_tfidf = tfidf_transformer.transform(X_test_dtm)

y_pred_class = nb.predict(X_test_tfidf)
# %%
from sklearn import metrics
metrics.f1_score(y_test, y_pred_class,average='micro')
#84.13
# %%
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train_tfidf, y_train)
y_pred_class = logreg.predict(X_test_tfidf)
# %%
metrics.f1_score(y_test, y_pred_class,average='micro')
#0.85
# %%
# %%
################################################test data#################################################
test['clean_text'] = test.body.apply(text_process)
#%%
#lemma
import nltk

wnl = nltk.WordNetLemmatizer()
#print([wnl.lemmatize(t) for t in tokens])

def lemmatization(df):
    df['clean_text'] = df['clean_text'].apply(lambda x: " ".join([wnl.lemmatize(t) for t in x.split()]))
    print(df['clean_text'].head())
    
#%%
lemmatization(test)
#remove
#%%
#remove rare word
freq = pd.Series(' '.join(test['clean_text']).split()).value_counts()[-20:]
freq

#%%
freq = list(freq.index)
def rare_words_removal(df):
    df['clean_text'] = df['clean_text'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
    print(df['clean_text'].head())
#%%
rare_words_removal(test)

# %%
from collections import Counter
freq = pd.Series(' '.join(test['clean_text']).split()).value_counts()[:20]#take a look at top 10 words
#%%
freq= list(freq.index)
def frequent_words_removal(df):    
    df['clean_text'] = df['clean_text'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
    print(df['clean_text'].head())
# %%
frequent_words_removal(test)
#%%
# %%
# split x and y
X = test.clean_text
y = test.urgency
print(X.shape)
print(y.shape)
# %%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
# %%
from sklearn.feature_extraction.text import CountVectorizer

# instantiate the vectorizer
vect = CountVectorizer()
vect.fit(X_train)
#%%
X_train_dtm = vect.fit_transform(X_train)
#%%
X_test_dtm = vect.transform(X_test)
X_test_dtm

#%%
from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
tfidf_transformer.fit(X_train_dtm)
X_train_tfidf = tfidf_transformer.transform(X_train_dtm)
# %%
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)
X_test_tfidf = tfidf_transformer.transform(X_test_dtm)

y_pred_class = nb.predict(X_test_tfidf)
# %%
from sklearn import metrics
metrics.f1_score(y_test, y_pred_class,average='micro')
#82
#lemmazation decreased f1 score

# %%
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train_tfidf, y_train)
y_pred_class = logreg.predict(X_test_tfidf)
# %%
metrics.f1_score(y_test, y_pred_class,average='micro')
#84.6