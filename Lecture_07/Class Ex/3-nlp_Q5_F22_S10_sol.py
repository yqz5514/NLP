# =================================================================
# Consider the following 5 sentences.
# sent 1 : 'This is a sentence one, and I want to all data here.',
# sent 2 :  'Natural language processing has nice tools for text mining and text classification. I need to work hard and try a lot of exericses.',
# sent 3 :  'Ohhhhhh what',
# sent 4 :  'I am not sure what I am doing here.',
# sent 5 :  'Neural Network is a power method. It is a very flexible architecture'

# Train ADALINE network to find  a relationship between POS (just verbs and nouns) and the length of the sentences.
# ----------------------------------------------------------------
from nltk import  pos_tag
from nltk import word_tokenize
import numpy as np
import matplotlib.pyplot as plt
# ----------------------------------------------------------------


Corp = ['This is a sentence one and this is a sample text.',
        'Natural language processing has nice tools for text mining and text classification. I need to work hard and try to learn it by doing exericses.',
        'Ohhhhhh what',
        'I am not sure what I am doing is right.',
        'Neural Network is a powerful method. It is a very flexible architecture']

len_sent = [len(x.split()) for x in Corp]

zz = [ pos_tag(word_tokenize(x)) for x in Corp]
verbs = [y[0] for x in zz  for y in x if y[1].startswith('V') ]
nonuns = [y[0] for x in zz  for y in x if y[1].startswith('N') ]

l_v = [x for x in Corp if x in verbs]
l_v = [len(set(x.split()).intersection(set(verbs))) for x in Corp]

l_n = [x for x in Corp if x in nonuns]
l_n = [len(set(x.split()).intersection(set(nonuns))) for x in Corp]



w=np.random.rand(2)
b=np.random.rand(1)
alpha = 0.1
epoch = 1000

# ['I', 'am', 'excited', 'about', 'classifier', 'with', 'real', 'data']
p=np.array([l_v, l_n ])/6
t=np.array(len_sent)/25

E = np.zeros(p.shape[1])
SSE = np.zeros(epoch)
for k in range(epoch):
    for i in range(p.shape[1]):
        n=w.dot(p[:,i])+b
        E[i]=t[i]-n
        w= w + 2 * alpha * E[i] * p[:,i]
        b= b + 2* alpha * E[i]
    SSE[k] = E.T @ E

plt.figure()
plt.plot(SSE)
plt.show()

print(w)
print(b)

line = w[0]* p + b
line1 = w[1]* p + b
plt.figure()
plt.scatter(p, line, marker='x')
plt.scatter(p, line1, marker='^')
plt.legend(['Verb','Noun','Verb vs Noun'])
plt.show()


