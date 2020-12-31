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

# NOTICE: if we are classifying everything into a single class, this means our model needs to have
#         it parameters adjusted (it may also help to normalize the data).
#         
#         We do so by using a GridSearch. Finding the right parameters (like what C or gamma 
#         values to use) is a tricky task! But luckily, we can be a little lazy and just try a
#         bunch of combinations and see what works best! 
# 
#         The idea of creating a 'grid' of parameters and just trying out all the possible 
#         combinations is called a Gridsearch, this method is common enough that Scikit-learn 
#         has this functionality built in with GridSearchCV! 
# 
#         The CV stands for cross-validation which is the GridSearchCV takes a dictionary that
#         describes the parameters that should be tried and a model to train. The grid of 
#         parameters is defined as a dictionary, where the keys are the parameters and the 
#         values are the settings to be tested.   

# In SVM, C controls the cost of misclassification on the training data. A large C value gives us 
# low bias (we penalize more the cost of misclassification) and high variance, and vice versa.
# The gamma parameter has to do with the free parameter of the Gaussian radial basis function
# (which is the default kernel used in SVC). A small gamma means a Gaussian for large variance, where
# a large gamma value is going to lead to a high bias and low variance in the model (hence the 
# support vector does not have a widespread influence).

# %%
# GRID SEARCH (can take a very long time. Depends on the number of parameters to test and # obs)
param_grid = {'C':[0.1,1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
grid = GridSearchCV(SVC(),param_grid,verbose = 3)  # the higher the number, the more description
                                                   # in the ooutput
grid.fit(X_train,y_train)

# %%
# Getting the parameters after CV
grid.best_params_
grid.best_estimator_

# %%
# Predicting points classification
grid_pred = grid.predict(X_test)

# Checking performance
print('Classification Report')
print(classification_report(y_test,grid_pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,grid_pred))

# %%
del y, X, X_test, X_train, y_train, y_test, grid, pred, grid_pred, param_grid, svm

# %%
####################################################################################
# PROJECT EXERCISE - Iris

from sklearn.datasets import load_iris
iris = load_iris()
target = pd.DataFrame(iris['target'],columns=['species'])
data = pd.DataFrame(iris['data'],columns=iris['feature_names'])
iris = pd.concat([target,data],axis=1)
iris.head()

# Iris plants dataset

#     :Number of Instances: 150 (50 in each of three classes)
#     :Number of Attributes: 4 numeric, predictive attributes and the class
#     :Attribute Information:
#         - sepal length in cm
#         - sepal width in cm
#         - petal length in cm
#         - petal width in cm
#         - class:
#                 - Iris-Setosa
#                 - Iris-Versicolour
#                 - Iris-Virginica

# %%
# Exploratory Data Analysis
# Creatin a pairplot of the data set.
sns.pairplot(iris, corner=True, hue='species')
# Comment: Note setosa seems to be the most separable species compared to versicolour and virginica.
#          It does not share all the same characteristics as the other two.

# %%
# Creating a kde plot of sepal_length versus sepal width for setosa species of flower
sns.set_style('darkgrid')
sns.kdeplot(y='sepal length (cm)',x='sepal width (cm)',data = iris[iris['species']==1],fill=True,cmap='Greens')

# %%
# Splitting data by test and train data
X = iris.drop('species',axis=1)
y = iris['species']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)

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

# %%
# GRID SEARCH 
param_grid = {'C':[0.1,1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
grid = GridSearchCV(SVC(),param_grid,verbose = 3) 
grid.fit(X_train,y_train)

# %%
# Getting the parameters after CV
grid.best_params_
grid.best_estimator_

# %%
# Predicting points classification
grid_pred = grid.predict(X_test)

# Checking performance
print('Classification Report')
print(classification_report(y_test,grid_pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,grid_pred))