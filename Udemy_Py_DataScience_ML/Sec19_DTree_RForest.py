####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 19 - Decision Trees and Random Forests
# datasets: (i) fake dataset, (ii) Lending data from 2007-2010 (source: LendingClub.com)
####################################

### DECISION TREES ###
# The tree has:
#   Nodes: which splits for the value of a certain attribute
#   Edges: outcomes of a split to next node
#   Root: the nodes that performs the first split
#   Leaves: terminal nodes that predict the outcome
#
# The root will depend on the user, but using entropy and information gain measures
# we can choose the best split. The actual intuition is just trying to choose the 
# features that best split our data.
#
# CONS: they do not tend to have the best predictive accurary due to the high variance (different splits
#       in the training data can lead to very different trees).

### RANDOM FORESTS ###
# Check for 'bagging' - Chapter 8, Intro to Statistical Learning
# To improve performance, we can use many trees with a random sample of features chosen as the split. 
# That is we create an ensemble of decision trees using bootstrap samples of the the training set (w/replacement)
# A new random sample of M features is chosen for every single tree at every single split.
# For classification, M is tipically chosen to be the square root of P (full set of features).
# 
# Note that when there is one very strong feature in the data as well as we're using 'bagged' trees (bootstrap sampling), 
# most of the trees will use that feature as the top splot, resulting in an ensenmble of similar trees that are highly
# correlated. Hence, getting the mean. Averaging highly correlated quantities does not significantly reduce variance. 
# By randomly leaving out candidate features from each splot, Random Forests decorrelates the trees, such that the 
# averaging process can reduce the variance of the resulting model.
#
# This is an extremely powerful tool when it comes to ML algorithms. It is the first quick choice for recreating
# a very fast classification model as far as just trying to see what's kind of baseline accuracy or precision 
# or recall we can get from a model before we start kind of playing around for other models or tuning stuff.

# %% 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,confusion_matrix

#%matplotlib inline
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/dt_rf_data')

# %%
# Loading and visualizing data
df = pd.read_csv('kyphosis.csv')
df.head()

# Exploratory analysis
sns.pairplot(df, hue = 'Kyphosis')

# %%
# Splitting data by test and train data
X = df.drop('Kyphosis',axis = 1)
y = df['Kyphosis']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)

# %%
# DECISION TREE
# Initializing the model and training it
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)

# %%
# Predicting points classification
pred = dtree.predict(X_test)

# %%
# Checking performance
print('Classification Report')
print(classification_report(y_test,pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,pred))

# %%
# RANDOM FOREST
rf = RandomForestClassifier(n_estimators = 200)
rf.fit(X_train,y_train)

rf_pred = rf.predict(X_test)

# %%
# Checking performance
print('Classification Report')
print(classification_report(y_test,rf_pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,rf_pred))

# %%
# Notice
df['Kyphosis'].value_counts()
# Comment: notice that there are more present values than absent ones, which might be affecting the result

# %%
# TREE VISUALIZATION
# Requires both the 'pydot' and the 'graphviz' library. The latter is not actually a libary, instead is a 
# whole new software outside Python, which requires to be downloaded and installed it (www.graphviz.org)

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

# %%
# Loading and visualizing data
df = pd.read_csv('loan_data.csv')
df.head()

## EXPLORATORY DATA ANALYSIS
# %%
# Checking the distribution of FICO depending on credit.policy
sns.histplot(x='fico', data=df,hue='credit.policy')
# Comment: mostly all people who do not meet the credit underwriting criteria posses a lower FICO.

# %%
# Checking the distribution of FICO depending on not.fully.paid
sns.histplot(x='fico', data=df,hue='not.fully.paid')
# Comment: there's a lot of people who have not fully paid their debts

# %%
# Checking the amount of loans by purpose, distinguishing by not.fully.paid status
plt.figure(figsize=(10,6))
sns.countplot(x = 'purpose', data = df, hue='not.fully.paid')
plt.tight_layout()
plt.show()
# Comment: Mostly all the loans are due to debt consolidation. Regardless of the purpose,
#          all of them posses a high percent people who have not fully paid them.

# %%
# Checking the trend between FICO and interest rate
sns.jointplot(x='fico',y='int.rate',data=df,kind='reg',scatter_kws = {'s':10},color='green')
# Comment: the lower the interest rate, the higher the FICO score

# %%
# Checking if the previous relationship differs between not.fully.paid and credit.policy
sns.lmplot(x='fico',y='int.rate',data=df,hue='credit.policy',col='not.fully.paid')
# Comment: there is no difference by these factor. The relationship still holds.

# %%
## CLEANING DATA
cat_feats = ['purpose']
final_data = pd.get_dummies(df,columns=cat_feats,drop_first=True)
final_data.head()

# %%
## TRAIN, TEST, SPLIT
X = final_data.drop('not.fully.paid',axis = 1)
y = final_data['not.fully.paid']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)

# %%
## DECISION TREE
dtree = DecisionTreeClassifier()
dtree.fit(X_train,y_train)
pred = dtree.predict(X_test)

# Checking performance
print('Classification Report')
print(classification_report(y_test,pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,pred))

# %%
## RANDOM FOREST
rf = RandomForestClassifier(n_estimators = 200)
rf.fit(X_train,y_train)
rf_pred = rf.predict(X_test)

# Checking performance
print('Classification Report')
print(classification_report(y_test,rf_pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,rf_pred))