# =================================================================
# Class_Ex1:
# Write a function that checks a string contains only a certain set of characters
# (all chars lower and upper case with all digits).
# ----------------------------------------------------------------
#%%
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)
# =================================================================
# Class_Ex2:
# Write a function that matches a string in which a followed by zero or more b's.
# Sample String 'ac', 'abc', abbc'
# ----------------------------------------------------------------
#%%

import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')



print(20*'-' + 'End Q2' + 20*'-')
# =================================================================
# Class_Ex3:
# Write Python script to find numbers between 1 to 3 in a given string.

# ----------------------------------------------------------------
print(20*'-' + 'Begin Q3' + 20*'-')
# find numbers between length 1 to 3
import re
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))







print(20*'-' + 'End Q3' + 20*'-')
# =================================================================
# Class_Ex4:
# Write a Python script to find the a position of the substrings within a string.
# text = 'Python exercises, JAVA exercises, C exercises'
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q4' + 20*'-')

import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))







print(20*'-' + 'End Q4' + 20*'-')
# =================================================================
# Class_Ex5:
# Write a Python script to find if two strings from a list starting with letter 'C'.
# words = ["Cython CHP", "Java JavaScript", "PERL S+"]
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q5' + 20*'-')


import re


words = ["Cython CHP", "Java JavaScript", "PERL S+"]

for w in words:
        m = re.match("(C\w+)\W(C\w+)", w)
        # Check for success
        if m:
            print(m.groups())






print(20*'-' + 'End Q5' + 20*'-')

# =================================================================
# Class_Ex6:
# Write a Python script to remove everything except chars and digits from a string.
# USe sub method
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q6' + 20*'-')

#%%
import re
text1 = '2343#$% @@\ pythonregex 3949*(**)'
pattern = re.compile('[\W_]+')
print(pattern.sub('', text1))







print(20*'-' + 'End Q6' + 20*'-')
# =================================================================
# Class_Ex7:
# Scrape the the following website
# https://en.wikipedia.org/wiki/Natural_language_processing
# Find the tag which related to the text. Extract all the textual data.
# Tokenize the cleaned text file.
# print the len of the corpus and pint couple of the sentences.
# Calculate the words frequencies.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q7' + 20*'-')

#%%


import requests
from bs4 import BeautifulSoup

url = 'https://darksky.net/forecast/40.7127,-74.0059/us12/en'

html = requests.get(url)
html.encoding = 'utf-8' # Optional: requests infers this internally
raw = html.text
raw1 = BeautifulSoup(raw, 'html.parser').get_text()
#tokens = word_tokenize(raw) #print(tokens)




print(20*'-' + 'End Q7' + 20*'-')
# =================================================================
# Class_Ex8:
# Grab any text from Wikipedia and create a string of 3 sentences.
# Use that string and calculate the ngram of 1 from nltk package.
# Use BOW method and compare the most 3 common words.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q8' + 20*'-')

from nltk.corpus import brown
import nltk

#%%
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print(unigram_tagger.tag(brown_sents[2007]))
#the UnigramTagger finds the most likely tag for each word in a training corpus, 
# and then uses that information to assign tags to new tokens.

#%%
print(unigram_tagger.evaluate(brown_tagged_sents))
#Score the accuracy of the tagger against the gold standard.
#%%
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print(unigram_tagger.evaluate(test_sents))  









print(20*'-' + 'End Q8' + 20*'-')
# =================================================================
# Class_Ex9:
# Write a python script that accepts any string and do the following.
# 1- Tokenize the text
# 2- Doe word extraction and clean a text. Use regular expression to clean a text.
# 3- Generate BOW
# 4- Vectorized all the tokens.
# 5- The only package you can use is numpy and re.
# all sentences = ["sentence1", "sentence2", "sentence3",...]
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q9' + 20*'-')

from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
sentence = "The faster Harry got to the store, the faster Harry " \
           "the faster, would get home."
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())
print(tokens)

bag_of_words = Counter(tokens)
print(bag_of_words)









print(20*'-' + 'End Q9' + 20*'-')
# =================================================================
# Class_Ex10:
# Grab any text (almost a paragraph) from Wikipedia and call it text
# Preprocessing the text data (Normalize, remove special char, ...)
# Find total number of unique words
# Create an index for each word.
# Count number of the owrds.
# Define a function to calculate Term Frequency
# Define a function calculate Inverse Document Frequency
# Combining the TF-IDF functions
# Apply the TF-IDF Model to our text
# you are allowed to use just numpy and nltk tokenizer
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q10' + 20*'-')

from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
sentence = "The faster Harry got to the store, the faster Harry " \
           "the faster, would get home."
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())
print(tokens)

bag_of_words = Counter(tokens)
print(bag_of_words)


from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
sentence = "The faster Harry got to the store, the faster Harry " \
           "the faster, would get home."
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())
bag_of_words = Counter(tokens)
print(bag_of_words.most_common(4))

times_harry_appears = bag_of_words['harry']
num_unique_words = len(bag_of_words)
tf = times_harry_appears / num_unique_words; print(tf)







print(20*'-' + 'End Q10' + 20*'-')
# =================================================================
# Class_Ex11:
# Grab arbitrary paragraph from any website.
# Creat  a list of stopwords manually.  Example :  stopwords = ['and', 'for', 'in', 'little', 'of', 'the', 'to']
# Create a list of ignore char Example: ' :,",! '
# Write a LSA class with the following functions.
# Parse function which tokenize the words lower cases them and count them. Use dictionary; keys are the tokens and value is count.
# Clac function that calculate SVD.
# TFIDF function
# Print function which print out the TFIDF matrix, first 3 columns of the U matrix and first 3 rows of the Vt matrix
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q11' + 20*'-')









print(20*'-' + 'End Q11' + 20*'-')
# =================================================================
# Class_Ex12:
# Use the following doc
# doc = ["An intern at OpenAI", "Developer at OpenAI", "A ML intern", "A ML engineer" ]
# Calculate the binary BOW.
# Use LSA method and distinguish two different topic from the document. Sent 1,2 is about OpenAI and sent3, 4 is about ML.
# Use pandas to show the values of dataframe and lsa components. Show there is two distinct topic.
# Use numpy take the absolute value of the lsa matrix sort them and use some threshold and see what words are the most important.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q12' + 20*'-')







print(20*'-' + 'End Q12' + 20*'-')
# =================================================================














#%%
#E.1: In part of this exercise, you will use regular expression. 
# i. Load Email.txt dataset. 
#%%
with open('email.txt', 'r') as f:
    text = f.read()

text[5]
# ii. Find all email addresses in the text file. 
#%%
import re
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(text)
for m in matches:
    print(m.groups())

# iii. Verify the results. An email address usually follows these rules: 
# • Upper or lower case letters or digits • Starting with a letter 
# • Followed by a the at sign symbol. • Followed by a string of alphanumeric characters. No spaces are allowed 
# • Followed by a the dot “.” symbol • Followed by a domain extension(e.g.,“com”, “edu”, “net”.) 

#%%
# E.2: In part of this exercise, you will use regular expression. 
# i. Load war and peace by By Leo Tolstoy. 
#%%
with open('war.txt', 'r') as f:
    text = f.read()
text[5]
# ii. Check line by line and find any proper name ending with ”..ski” then print them all. 
#%%
import re
pattern = re.compile(r'[A-Z]([a-z]+|\.)ski')#([a-z]+|\.)
ms = pattern.finditer(text)
list = []
for match in ms:
    value = match.group()

    list.append(value)
print(list)
#%%
sum(1 for _ in re.finditer(pattern,text))#'[A-Z]{1}\w*ski'#511
#[A-Z]([a-z]+|\.)ski 510

#%%
# iii. Put all the names into a dictionary and sort them. 
from collections import OrderedDict, Counter, defaultdict

#%%
count = Counter(list)
#%%
dict2 = OrderedDict(count)
print(dict2)
#%%
type(count)
#type(dict)
#%%
dict1 = {}
dict1.update(count)
print(dict1)
#%%
type(dict1)
#%%
print({k: v for k, v in sorted(dict1.items(), key=lambda item: item[1], reverse = True)})

#%%
# E.3: In part of this exercise, you will use regular expression. 
# i. Write a program with regular expression that joins numbers if there is a space between them 
#%%
# (e.g., ”12 0 mph is a very high speed in the 6 6 interstate.” to ”120 mph is a very high speed in the 66 interstate.” ) 
# ii. Write a program with regular expression that find the content in the parenthesise and replace it with ”(xxxxx)” 
# iii. Write a program that find any word ends with ”ly”. 
# iv. Write a program that finds all the quotes in the text and prints the strings in between. 
# v. Write a program that finds all words which has 3,4,5 charters in the text. v. Write a program that replaces a comma with a hyphen. 
# vi. Write a program that extract year, month and date from any url which has date init which follows by forward slashes. ”
# https://www.yahoo.com/news/football/wew/2021/09/02/odellfamer-rrrr-on-one-tr-littleball–norman-stupid-author/”