# ------------------Import Library----------------------------
import pandas as pd
import nltk
from nltk import word_tokenize , sent_tokenize
#-------------------Q1------------------------------
from nltk.book import *
all =' '.join(text3.tokens)
f = open('text4_from_nltk.txt', 'w+', encoding='utf-8')
f.write(all)
f.close()
#-------------------Q2------------------------------
f = open('data.txt', 'r')
data = f.read()
tokens = word_tokenize(data)
sents = sent_tokenize(data)
#-------------------Q3------------------------------
sent_len = [len(x) for x in sents]
word_count = [len(x.split()) for x in sents]
word_average_len = [sum(map(len, x.split()))/len( x.split()) for x in sents]
#-------------------Q4------------------------------
nouns_list = [list(filter(lambda x:x[1] == 'NN', nltk.pos_tag(word_tokenize(x)))) for x in sents]
nouns_len = [len(list(filter(lambda x:x[1] == 'NN', nltk.pos_tag(word_tokenize(x))))) for x in sents]
#-------------------Q5------------------------------
df = pd.DataFrame({'Sents':sents, 'Sent_len':sent_len, 'Words Count':word_count, "Average Word Length":word_average_len,
                   'Nouns List ':nouns_list ,'Nouns Length':nouns_len,})

df.to_excel('NLTK_Feature_Extraction.xlsx') 
