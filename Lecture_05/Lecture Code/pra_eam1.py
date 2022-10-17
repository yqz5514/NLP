##Library
##preview of data
##count number of words
def num_of_words(df):
    df['word_count'] = df['tweet'].apply(lambda x : len(str(x).split(" ")))
    print(df[['tweet','word_count']].head())
#for each row

##count number of characters
def num_of_chars(df):
    df['char_count'] = df['tweet'].str.len() ## this also includes spaces
    print(df[['tweet','char_count']].head())

##average word length
def avg_word(sentence):
    words = sentence.split()    
    return (sum(len(word) for word in words)/len(words))

def avg_word_length(df):
    df['avg_word'] = df['tweet'].apply(lambda x: avg_word(x))
    print(df[['tweet','avg_word']].head())
    
##find long(junk) word in text
l = data.split(sep='')
w_more_than_8 = [x for x in l if len(x) > 15]
#remove it 

##number of stop words
def stop_words(df):
    df['stopwords'] = df['tweet'].apply(lambda x: len([x for x in x.split() if x in stop]))
    print(df[['tweet','stopwords']].head())
##number of special char
##
def num_numerics(df):
    df['numerics'] = df['tweet'].apply(lambda x: len([x for x in x.split() if x.isdigit()]))
    print(df[['tweet','numerics']].head())
    
##lower casing
def lower_case(df):
    df['tweet'] = df['tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    print(df['tweet'].head())

##remove punctuation
def punctuation_removal(df):
    df['tweet'] = df['tweet'].str.replace('[^\w\s]','')
    print(df['tweet'].head())
#check punctuation again

##remove stop words
from nltk.corpus import stopwords
stop = stopwords.words('english')
def stop_words_removal(df):
    df['tweet'] = df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    print(df['tweet'].head())
    
##frequent words removal?
from collections import Counter
freq = pd.Series(' '.join(train['tweet']).split()).value_counts()[:10]#take a look at top 10 words
freq = list(freq.index)
def frequent_words_removal(df):    
    df['tweet'] = df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
    print(df['tweet'].head())
    
##rare words remove?
freq = pd.Series(' '.join(train['tweet']).split()).value_counts()[-10:]# maybe can take a llok at 20?
freq = list(freq.index)
def rare_words_removal(df):
    df['tweet'] = df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))
    print(df['tweet'].head())

##remove all
def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    # remove evrythiing text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    return text

train['text'] = train['text'].apply(lambda x:clean_text(x))
train['selected_text'] = train['selected_text'].apply(lambda x:clean_text(x))

## tokenizTION
from nltk.tokenize import RegexpTokenizer#
tokenizer = RegexpTokenizer(r'\w+|$[0-9.]+|\S+')
sentence ='Thomas Jefferson began building Monticello at theage of 26.'
print(tokenizer.tokenize(sentence))

from nltk.tokenize import TreebankWordTokenizer# based on wall street journal
sentence = "Monticello wasn't designated as UNESCO World Heritage Site until 1987."
tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize(sentence))

from nltk.tokenize.casual import casual_tokenize
message = "RT @TJMonticello Best day everrrrrrr at Monticello." \
          "Awesommmmmmeeeeeeee day :*)"
print(casual_tokenize(message))
print(casual_tokenize(message, reduce_len=True, strip_handles=True))

##stem 
from nltk.stem import PorterStemmer
st = PorterStemmer()
def stemming(df):
    return df['tweet'][:5].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

##lemma
import nltk
from nltk import word_tokenize

raw = """DENNIS: Listen, strange women lying in ponds distributing swords
 is no basis for a system of government.  Supreme executive power derives from
a mandate from the masses, not from some farcical aquatic ceremony."""

tokens = word_tokenize(raw)
#%%
wnl = nltk.WordNetLemmatizer()
print([wnl.lemmatize(t) for t in tokens])

def lemmatization(df):
    df['tweet'] = df['tweet'].apply(lambda x: " ".join([wnl.lemmatize(t) for t in x.split()]))
    print(df['tweet'].head())
    
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("better", pos="n"))

## remove unkown words from the test but not in train ???

##TF
def term_frequency(df):
    tf1 = (df['tweet'][1:2]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()
    tf1.columns = ['words','tf']
    return tf1.head()

##tfidf
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',
 stop_words= 'english',ngram_range=(1,1))
train_vect = tfidf.fit_transform(train['tweet'])
train_vect

#BOW
from sklearn.feature_extraction.text import CountVectorizer
bow = CountVectorizer(max_features=1000, lowercase=True, ngram_range=(1,1),analyzer = "word")
train_bow = bow.fit_transform(train['tweet'])
train_bow

#%%
# how to define X and y (from the SMS data) for use with COUNTVECTORIZER
X = sms.clean_msg
y = sms.label_num
print(X.shape)
print(y.shape)
# split X and y into training and testing sets 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.feature_extraction.text import CountVectorizer

# instantiate the vectorizer
vect = CountVectorizer()
vect.fit(X_train)
# learn training data vocabulary, then use it to create a document-term matrix
X_train_dtm = vect.transform(X_train)
# equivalently: combine fit and transform into a single step
X_train_dtm = vect.fit_transform(X_train)
# examine the document-term matrix
X_train_dtm
# transform testing data (using fitted vocabulary) into a document-term matrix
X_test_dtm = vect.transform(X_test)
X_test_dtm
from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer()
tfidf_transformer.fit(X_train_dtm)
tfidf_transformer.transform(X_train_dtm)

### building and evaluating model]
# import and instantiate a Multinomial Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
# train the model using X_train_dtm (timing it with an IPython "magic command")
%time nb.fit(X_train_dtm, y_train)

# make class predictions for X_test_dtm
y_pred_class = nb.predict(X_test_dtm)
# calculate accuracy of class predictions
from sklearn import metrics
metrics.accuracy_score(y_test, y_pred_class)
# print the confusion matrix
metrics.confusion_matrix(y_test, y_pred_class)
X_test.shape

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

pipe = Pipeline([('bow', CountVectorizer()), 
                 ('tfid', TfidfTransformer()),  
                 ('model', MultinomialNB())])
pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)
metrics.accuracy_score(y_test, y_pred)
metrics.confusion_matrix(y_test, y_pred)

#logis
# import an instantiate a logistic regression model
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(solver='liblinear')

# train the model using X_train_dtm
%time logreg.fit(X_train_dtm, y_train)

# make class predictions for X_test_dtm
y_pred_class = logreg.predict(X_test_dtm)
# calculate predicted probabilities for X_test_dtm (well calibrated)
y_pred_prob = logreg.predict_proba(X_test_dtm)[:, 1]
y_pred_prob

# calculate accuracy
metrics.accuracy_score(y_test, y_pred_class)

##
#Tp FN
#FP TN
# p = tp/tp+fp
# r = tp/tp+fn
def simple_preprocessing(text):
    heading = re.findall("^.+(?=\n)", text) # Extract the first line as heading
    text = re.sub(heading[0], '', text) # Remove the heading
    text = re.sub('\n', ' ', text) # Replace newline character with whitespace
    text = re.sub('[$(.%),;!?]+','', text) # Remove common punctuations
    text = text.strip() # Remove leading and training whitespaces
    return (heading[0], text)

news_and_heading = [simple_preprocessing(txt.lower()) for txt in df['news']]

