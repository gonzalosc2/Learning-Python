# ###################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 22 - Principal Component Analysis
# datasets: breast cancer diagnoses from sklearn
# ###################################

## PCA (aka general factor analysis) ###
# An unsupervised statistical technique used to examine the interrelations among a set of
# variables in order to identify the underlying structure of those variables. Where regression
# determines a line of best fit to a data set, factor analysis determines several orthogonal 
# lines of best fit to the data set.
# The components are a linear transformation that chooses a variable system for the data set
# such that the greatest variance of the data set comes to lie on the first axis, the second
# greatest variance on the second axis, and so on ... This process allows us to reduce the number
# of variables used in an analysis.
# 
# Note that components are uncorrelated, since in the sample space they are orthogonal to each other!
# 
# PROS: 
#   When we have a large number of variables in a data set, we can compress the amount of explained
#   variation to just a few components
# 
# CONS:
#   Interpreting the components

# %% 
#import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
#%matplotlib inline

# %%
# Loading and visualizing data
cancer = load_breast_cancer()
cancer.keys()
print(cancer['DESCR'])

df = pd.DataFrame(cancer['data'],columns = cancer['feature_names'])
df.head()

# %% 
# Scaling everything to have a single unit variance
scaler = StandardScaler()
scaler.fit(df)
scaled_data = scaler.transform(df)

# %% 
# Performing the PCA
pca = PCA(n_components = 2)  # number of component we want to keep are two
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)  # transforms the data to its first principle component

# Checking dimensions before and after transformation
print('Data dimensions')
print('Scaled data: ',str(scaled_data.shape))
print('Transformed data: ', str(x_pca.shape))

# %%
# Checking how the data looks like in 2D
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'],cmap='plasma')
plt.xlabel('First Principle Component')
plt.ylabel('Second Principle Component')
plt.show()

# %% 
# Showing how each variable was combined to get a component, where each row represents a component
# and each column represents the weigth of each column
pca.components_

df_comp = pd.DataFrame(pca.components_, columns=cancer['feature_names'])
sns.set_style('darkgrid')
plt.figure(figsize=(12,6))
sns.heatmap(df_comp,cmap='Greens')

# We can now use the x_pca to fit a classification algorithm. So we can do something like a logistic
# regression on x_pca instead of doing a logistic regression on the entire data frame of features.
# Since data seems to be very well separated, SVMs may actually be a good choice for this.