####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 19 - Decision Trees and Random Forests
# datasets: fake datasets
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
# PROJECT EXERCISE 
# %%
# Loading and visualizing data
df = pd.read_csv('KNN_Project_Data')
df.head()

# %%
# Checking the data to see if there is any pattern
sns.pairplot(df,hue = 'TARGET CLASS', corner = True)
# Comment: it's difficult to make a comment since the data is unlabel
