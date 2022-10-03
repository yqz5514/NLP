# =================================================================
# Class_Ex1:
# Import spacy abd from the language class import english.
# Create a doc object
# Process a text : This is a simple example to initiate spacy
# Print out the document text from the doc object.
# ----------------------------------------------------------------
#%%
from spacy.lang.en import English

#%%
nlp = English()
doc = nlp("Seventeen has 13 members.")
print(doc.text)


# =================================================================
# Class_Ex2:
# Solve Ex1 but this time use German Language.
# Grab a sentence from german text from any website.
# ----------------------------------------------------------------
#%%
from spacy.lang.de import German
#%%
nlp = German()
doc = nlp("Seventeen has 13 members.")
print(doc.text)

# =================================================================
# Class_Ex3:
# Tokenize a sentence using sapaCy.
# ----------------------------------------------------------------
#%%
doc = nlp("Seventeen has 13 members.")
token = [t for t in doc]
print(token)
# =================================================================
# Class_Ex4:
# Use the following sentence as a sample text. and Answer the following questions.
# "In 2020, more than 15% of people in World got sick from a pandemic ( www.google.com ). Now it is less than 1% are. Reference ( www.yahoo.com )"
# 1- Check if there is a token resemble a number.
# 2- Find a percentage in the text.
# 3- How many url is in the text.

# ----------------------------------------------------------------
#%%
import spacy
nlp = spacy.load("en_core_web_sm")

#%%
doc = ("In 2020, more than 15% of people in World got sick from a pandemic ( www.google.com ). Now it is less than 1% are. Reference ( www.yahoo.com )")

# =================================================================
# Class_Ex5:
# Load small web english model into spaCy.
# USe the following text as a sample text. Answer the following questions
# "It is shown that: Google was not the first search engine in U.S. tec company. The value of google is 100 billion dollar"
# 1- Get the token text, part-of-speech tag and dependency label.
# 2- Print them in a tabular format.
# ----------------------------------------------------------------
#%%







print(20*'-' + 'End Q5' + 20*'-')

# =================================================================
# Class_Ex6:
# Use Ex 5 sample text and find all the entities in the text.

# ----------------------------------------------------------------
print(20*'-' + 'Begin Q6' + 20*'-')








print(20*'-' + 'End Q6' + 20*'-')
# =================================================================
# Class_Ex7:
# Use SpaCy and find adjectives plus one or 2 nouns.
# Use th efollowinf Sample text.
# Features of the iphone applications include a beautiful design, smart search, automatic labels and optional voice responses.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q7' + 20*'-')









print(20*'-' + 'End Q7' + 20*'-')
# =================================================================
# Class_Ex8:
# Use spacy lookup table and find the hash id for a cat
# Text : I have a cat.
# Next use the id and and find the string.
# ----------------------------------------------------------------
#%%
cat_hashid = nlp.vocab.strings['cat']
cat_text = nlp.vocab.strings[cat_hashid]



# =================================================================
# Class_Ex9:
# Create a Doc object for the following sentence
# Spacy is a nice toolkit.
# Use the methods like text, token,... on the Doc and check the functionality.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q9' + 20*'-')
#%%








print(20*'-' + 'End Q9' + 20*'-')
# =================================================================
# Class_Ex10:
# Use spacy and process the following text.
# Newyork looks like a nice city.
# Find which token is proper noun and which one is a verb.
#

# ----------------------------------------------------------------
print(20*'-' + 'Begin Q10' + 20*'-')









print(20*'-' + 'End Q10' + 20*'-')
# =================================================================
# Class_Ex11:
# Read the list of countries in a json format.
# Use the following text as  sample text.
# Czech Republic may help Slovakia protect its airspace
# Use statistical method and rule based method to find the countries.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q11' + 20*'-')









print(20*'-' + 'End Q11' + 20*'-')
# =================================================================
# Class_Ex12:
# Use spacy attributions and answer the following questions.
# Define the getter function that takes a token and returns its reversed text.
# Add the Token property extension "reversed" with the getter function
# Process the text and print the results.
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q12' + 20*'-')

#%%
from spacy.tokens import Doc

doc = nlp("Seventeen has 13 members.")

# Register custom attribute on Doc class
get_reversed = lambda doc: doc.text[::-1]
Doc.set_extension("reversed", getter=get_reversed)
# Compute value of extension attribute with getter
doc._.reversed
# 'eulb si kroY weN revo yks ehT'




#%%
print(20*'-' + 'End Q12' + 20*'-')
# =================================================================
# Class_Ex13:
# Read the tweets json file.
# Process the texts and print the entities
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q13' + 20*'-')

#%%
import json

f = open ('tweets.json', "r")

#%%
# Reading from file
data = json.loads(f.read())
new_data = ' '.join(data) # convert a list of str to a single str
#%%
print(new_data)
#%%
doc = nlp(new_data)
token = [t for t in doc]
for ent in doc.ents:
    print(ent.text, ent.label_)



#%%

print(20*'-' + 'End Q13' + 20*'-')
# =================================================================
# Class_Ex14:
# Use just spacy tokenization. for the following text
# "Burger King is an American fast food restaurant chain"
# make sure other pipes are disabled and not used.
# Disable parser and tagger and process the text. Print the tokens
# ----------------------------------------------------------------
print(20*'-' + 'Begin Q14' + 20*'-')

#%%

with nlp.disable_pipes("tagger", "parser"):
    doc = nlp(text)
    print(doc.text)



print(20*'-' + 'End Q14' + 20*'-')

# =================================================================


