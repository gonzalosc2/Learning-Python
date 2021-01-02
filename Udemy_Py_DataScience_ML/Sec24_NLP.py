# ###################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 24 - Natural Lenguage Processing
# datasets: (i) SMSSpamCollection (source: UCI) (ii) yelp reviews (source: Kaggle)
# ###################################

## NLP ###
# Serves a lot of use cases when we're dealing with text or unstructured text data.
# Example: we have 2 documents, (i) blue house, (ii) red house.
# We can featurized them based on word count:
#   Blue house -> (red,blue,house) -> (0,1,1)
#   Red house  -> (red,blue,house) -> (1,0,1)
#
# This way of representing a document as a vector of word counts is called a 'Bag of Words.
# Once we do that, we can use Cosine Similarity on the vector made to determine their 
# similarity, i.e., sim(A,B) = cos(\theta)= (A x B)/ (||A|| x ||B||).
# 
# We can improve on Bag of Words by adjusting word counts based on their frequency in corpus
# (the group of all the documents)
    # We can use Term Frequency - Inverse Document Frequency (TF-IDF):
    #   TF measures the importance of the term within the document. 
    #   TF(d,t) = number of occurences of term t in document d 
    #   IDF measures the importance of the term in the corpus
    #   IDF(t) = log(D/t) where
    #       D = total number of documents
    #       t = number of documents with the term
# 
# Then TF-IDF is
#   w(x,y) = TF(x,y) x log[D/t(x)], where y is the document and x the term


# %% 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import string
from nltk.corpus import stopwords
from sklearn import pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
#from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

#%matplotlib inline

os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/nlp_data')
# %%
# Downloading a data set from the nltk librabry
nltk.download_shell()  # write 'stopwords'

# %%
# Loading the dataset and checking its format
messages = [line.rstrip() for line in open('sms_spam_collection/SMSSpamCollection')]
print('Number of SMS messages: ', str(len(messages)))
print('\nExample of one SMS message: ',messages[0])

# %%
# Checking the first 10 messages and their structure
for mess_no, message in enumerate(messages[:10]):
    print(mess_no,message)
    print('n')

# %%
# Reloading the dataset in a proper way
messages = pd.read_csv('sms_spam_collection/SMSSpamCollection',sep='\t',names=['label','message'])
messages.head()

# %%
## EXPLORATORY DATA ANALYSIS
# Describing the dataset
messages.describe()

# %%
# Describing it by label
messages.groupby('label').describe()

# %%
# Checking how long are the text messages (a good feature)
messages['length'] = messages['message'].apply(len)
messages['length'].plot.hist(bins=50)
# Comment: there is a bi-modal behaviour with very short messages and others 
#          others around 180 characters. Notice there are very long messages as well.

# %%
# What is the actual length distribution?
messages['length'].describe()

# %%
# What is the longest message about?
messages[messages['length']==910]['message'].iloc[0]

# %%
# Is the length of a message a good feature to distinguish between ham and spam?
# Checking the lenght distribution by label
messages.hist(column='length',by='label',bins=60,figsize=(12,4))
# Comment: spam messages tend to have more characters!

# %%
## TEXT PROCESSING
# Removing punctuation
    # example
        # mess = 'Sample message! Notice: it has punctuation.'
        # nopunc = [c for c in mess if c not in string.punctuation]
        # nopunc = ''.join(nopunc)

# Removing common words (stop words) [these are not helpful to distinguish between both labels]
    # example
        # clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# Mixing all into a function
def text_process(mess):
    """
    1. remove punc
    2. remove stop words
    3. return list of clean text words
    """

    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    nopunc.split()

    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# %%
# Tokenizing messages (converting a normal text string into a list of tokens)
messages['message'].head(5).apply(text_process)

# Notice, we can do a lot more, such as using stemming (not useful on this dataset, though)

# %%
## VECTORIZATION
    # 1. Count how many times does a word occur in each message (TF).
    # 2. Weigh the counts, so that frequent tokens get lower weight (IDF).
    # 3. Normalize the vector to unit length, to abstract from the original text lenght (L2 norm).

# STEP 0: Using CountVectorizer to convert a collection of text documents to a matrix of token counts.
#         We can imagine this as s 2-dimensional matrix, where the 1-dimension is the
#         entire vocabulary (1 row per word) and the other dimension are the actual 
#         documents (in this case a column per text message).
#         [since there are so many messages, we can expect a lot of zero counts for the
#         the presence of that word in that document. Because of this, SciKit Learn will
#         output a Sparse Matrix]

bow_transformer = CountVectorizer(analyzer = text_process).fit(messages['message'])

# %%
# Checking the number of words in our vocabulary
print(len(bow_transformer.vocabulary_))

# %%
# Transforming messages into vectors
    # example
        # mess4 = messages['message'][3]
        # print('Sample message: ',mess4)
        # bow4 = bow_transformer.transform([mess4])
        # print('\nBag of words: \n',str(bow4))
        # print('\nBow 4 shape: ', str(bow4.shape))
        # # Comment: bow contains 11,425 words, but only seven appear in the message

# Checking the word that appear in a sample word vector. In this case the toke 4068
        # bow_transformer.get_feature_names()[4068]

# %%
#Transforming messages into vectors
messages_bow = bow_transformer.transform(messages['message'])

# %%
# Checking the shape of the sparse matrix, nonzero accurances and sparsity
print('\nShape of Sparse Matrix: ', messages_bow.shape)
print('\nNonZero occurances: ', messages_bow.nnz)
sparsity = (100 * messages_bow.nnz / (messages_bow.shape[0]*messages_bow.shape[1]))
print('\nSparsity: {}'.format(sparsity))

# %%
# STEP 1-2:
# Instantiating TF-IDF
tfidf_transformer = TfidfTransformer().fit(messages_bow)

# %%
# Calculating TF and IDP
    # example
        # tfidf4 = tfidf_transformer.transform(bow4)
        # print(tfidf4)
        # Checking the idf value for a specific word
        # tfidf_transformer.idf_[bow_transformer.vocabulary_['university']]

messages_tfidf = tfidf_transformer.transform(messages_bow)

# %%
## MODEL FOR DETECTING SPAM OR HAM
# Splitting the data between train and test data 
msg_train, msg_test, label_train, label_test = train_test_split(messages['message'],messages['label'],test_size = 0.3)

# Summarizing all the step we just did into a pipeline, that way we do not have to
# repeat (code) each step again for different sets of data. We should pass a list
# of things we want to do (tuple with the name of the thing we want to do). We will
# treat the pipeline as a normal estimatior
pipeline = Pipeline([

    ('bow',CountVectorizer(analyzer=text_process)),
    ('tfidf',TfidfTransformer()),
    ('classifier',MultinomialNB())
#   ('classifier',RandomForestClassifier())  # instead of MultinomialNB()
])

# Fitting our pipeline (our entire model)
    #spam_detect_model = MultinomialNB().fit(messages_tfidf,messages['label'])
pipeline.fit(msg_train,label_train)

# %%
# Predicting messages
    #all_pred = spam_detect_model.predict(messages_tfidf)
    #all_pred
predictions = pipeline.predict(msg_test)

# %%
# Checking performance
print(classification_report(label_test,predictions))