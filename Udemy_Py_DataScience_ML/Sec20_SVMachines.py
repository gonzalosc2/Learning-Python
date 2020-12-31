####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 20 - Support Vector Machines
# datasets: 
####################################

### SVM ###
# These are supervised learning models with associated learning algorithms that analyze data and recognize patterns, 
# used for classification and regression analysis
# 
# Given a set of training examples, each marked for belonging to one of two categories, and SVM training algorithm
# build a model that assigns new examples into one category or the other, making it a non-probabilistic binary
# classifier.
# 
# A SVM model is a representation of the examples as points in space, mapped so that the examples of the separate
# categories are divided by a clear gap (separating hyperplane) that is as wide as possible (a marging around the 
# hyperplane).
# 
# New examples are then mapped into that same space and predicted to belong to a category based on which side of 
# the gap they fall on. In case of having problems to separate data, for example we have a circle inside another
# circle, we can use the Kernel trick to look at this in a higher dimension.

# %% 
#import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report,confusion_matrix

#%matplotlib inline
#os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/dt_rf_data')

# %%
# Loading and visualizing data
cancer = load_breast_cancer()
cancer.keys()
print(cancer['DESCR'])

target = cancer['target']

df_feat = pd.DataFrame(cancer['data'],columns = cancer['feature_names'])
df_feat.head()

# %%
# Splitting data by test and train data
X = df_feat
y = target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state=101)

# %%
# SVM
# Instantiating the model and training it
svm = SVC()
svm.fit(X_train,y_train)

# %%
# Predicting points classification
pred = svm.predict(X_test)

# %%
# Checking performance
print('Classification Report')
print(classification_report(y_test,pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,pred))

# NOTICE: if we are classifying everything into a single class, this means our
#         model needs to have it parameters adjusted (it may also help to 
#         normalize the data).
#         
#         We do so by using a GridSearch. Finding the right parameters (like
#         what C or gamma values to use) is a tricky task! But luckily, we 
#         can be a little lazy and just try a bunch of combinations and see what 
#         works best! This idea of creating a 'grid' of parameters and just trying 
#         out all the possible combinations is called a Gridsearch, this method
#         is common enough that Scikit-learn has this functionality built in with
#         GridSearchCV! The CV stands for cross-validation which is the 
#         GridSearchCV takes a dictionary that describes the parameters that
#         should be tried and a model to train. The grid of parameters is defined 
#         as a dictionary, where the keys are the parameters and the values are 
#         the settings to be tested.   

# %%
del y, X, X_test, X_train, y_train, y_test, dtree, pred, df, rf, rf_pred

####################################################################################
# PROJECT EXERCISE - Loan Data

# GOAL: trying to classify and predict whether or not the borrower paid back their loan in full.
# 

# Here are what the columns represent:

    # credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
    # purpose: The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational",
    #          "major_purchase", "small_business", and "all_other").
    # int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers 
    #           judged by LendingClub.com to be more risky are assigned higher interest rates.
    # installment: The monthly installments owed by the borrower if the loan is funded.
    # log.annual.inc: The natural log of the self-reported annual income of the borrower.
    # dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).
    # fico: The FICO credit score of the borrower.
    # days.with.cr.line: The number of days the borrower has had a credit line.
    # revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
    # revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to 
    #             total credit available).
    # inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.
    # delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
    # pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).
