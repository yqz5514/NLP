#%%
# Question 1:
# • Consider the following 5 sentences:
# - This is a sentence one and this is a sample text.
# - Natural language processing has nice tools for text
# mining and text classification. I need to work hard
# and try to learn it by doing exericses.
# - Ohhhhhh what
# - I am not sure what I am doing is right.
# - Neural Network is a powerful method. It is a very flexible
# architecture
# 1. Find a length of sentences.
# 2. Find all nouns and verbs in the sentences.
# 3. Train an ADALINE network and plot the SSE.
# 4. Find the relationship between nouns, verbs and the length of sentences.
sent1 = 'This is a sentence one and this is a sample text.'
sent2 = 'Natural language processing has nice tools for text mining and text classification. I need to work hard and try to learn it by doing exericses.'
sent3 = 'Ohhhhhh what'
sent4 = 'I am not sure what I am doing is right.'
sent5 = 'Neural Network is a powerful method. It is a very flexible architecture'

#%%
# find length of sentences
sent = [sent1, sent2, sent3, sent4, sent5]
x = [len(i) for i in sent]
print(x)
#%%
type(x)
# # %%
# test = sent2.split(sep = '.')
# print(len(test))
# %%
#2
import spacy
from collections import Counter

#%%
nlp = spacy.load("en_core_web_sm")
# #%%

# cnt_nouns = []
# cnt_verbs = []
# for sents in sent:
#    doc = nlp(sents)
#    for token in doc:
#       if (token.pos_ == 'NOUN') or (token.pos_ == 'VERB'):
#          nouns = token
#          cnt_nouns.append(len(nouns))
#          verbs = token
#          cnt_verbs.append(len(verbs))
         
# print(cnt_nouns, cnt_verbs)

#%%
cnt_nouns = []
cnt_verbs = []
for sents in sent:
   doc = nlp(sents)
   nouns = [x for x in doc if x.pos_ == 'NOUN']
   verbs = [x for x in doc if x.pos_ == 'VERB']
   
   #print(doc, len(nouns), len(verbs))
   cnt_nouns.append(len(nouns))
   cnt_verbs.append(len(verbs))
print(cnt_nouns, cnt_verbs)
         

#%%
# doc = nlp()
# tokens = []
# for token in doc:
#     if (token.pos_ == 'NOUN') or (token.pos_ == 'VERB'):
#       print(token.text, token.pos_)
import pandas as pd     
df = pd.DataFrame({'Sentence':sent, 
                   'Num_Verb':cnt_verbs,
                   'Num_Noun':cnt_nouns, 
                   'Length':x,
                   })
df


# %%
#3. Train an ADALINE network and plot the SSE.

import numpy as np

class AdaptiveLinearNeuron(object):
   def __init__(self, rate = 0.01, niter = 10):
      self.rate = rate
      self.niter = niter

   def fit(self, X, y):
      """ Fit training data
      X : Training vectors, X.shape : [#samples, #features]
      y : Target values, y.shape : [#samples]
      """

      # weights
      self.weight = np.zeros(1 + X.shape[1])

      # Number of misclassifications
      self.errors = []

      # Cost function
      self.cost = []

      for i in range(self.niter):
         output = self.net_input(X)
         errors = y - output
         self.weight[1:] += self.rate * X.T.dot(errors)
         self.weight[0] += self.rate * errors.sum()
         cost = (errors**2).sum() / 2.0
         self.cost.append(cost)
      return self

   def net_input(self, X):
      """Calculate net input"""
      return np.dot(X, self.weight[1:]) + self.weight[0]

   def activation(self, X):
      """Compute linear activation"""
      return self.net_input(X)

   def predict(self, X):
      """Return class label after unit step"""
      return np.where(self.activation(X) >= 0.0, 1, -1)

#%%
df1 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)


#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


y = df.Length.values
#y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [1, 3]].values

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

# learning rate = 0.01
aln1 = AdaptiveLinearNeuron(0.01, 10).fit(X,y)

ax[0].plot(range(1, len(aln1.cost) + 1), np.log10(aln1.cost), marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaptive Linear Neuron - Learning rate 0.01')

# learning rate = 0.01
aln2 = AdaptiveLinearNeuron(0.0001, 10).fit(X,y)

ax[1].plot(range(1, len(aln2.cost) + 1), aln2.cost, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('Sum-squared-error')
ax[1].set_title('Adaptive Linear Neuron - Learning rate 0.0001')
plt.show()
# %%
