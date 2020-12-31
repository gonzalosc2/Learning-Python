# ###################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 23 - Recommender Systems
# datasets: Movie lens dataset
# ###################################

## Recommender Systems ###
# Take a look at the 'Recommender Systems' by Jannach and Zanker
# The two most common type of RS are:
# (i) Content-Based: focus on the attributes of the items and give you recommendations
#                    based on the similarity between them.
# (ii) Collaborative Filtering (CF): produces recommendations based on the knowledge
#                                    of users' attitude to items, i.e., it uses the 
#                                    'wisdom of the crowd' to recommend items 
#                                    (e.g. Amazon).
# CF is more commonly used because it usually gives better results and is relatively
# easy to understand (from an overall implementation perspective). This algorithm
# has the ability to do feature learning on its own, which means that it can start to
# learn for itself what features to use.
# 
# CF can also be sub-divided by:
# (a) Memory-based CF
# (b) Model-based CF

# %% 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import sklearn

#%matplotlib inline

os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/rsys_data')
# %%
# Loading movie data
columns_names = ['used_id','item_id','rating','timestamp']
df = pd.read_csv('u.data',sep='\t',names=columns_names)
df.head()

# %%
# Loading movie title data
movie_titles = pd.read_csv('Movie_Id_Titles')
movie_titles.head()

# %%
# Merging both data sets
df = pd.merge(df,movie_titles,on='item_id')
df.head()

# %%
# Checking the mean rating by movie (top 5)
df.groupby('title')['rating'].mean().sort_values(ascending=False).head()

# %%
# Checking the number of reviews by movie (top 5)
df.groupby('title')['rating'].count().sort_values(ascending=False).head()

# %%
# Creating a dataframe out of the previous calculations
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

# %%
# Checking the distribution of number of reviews
ratings['num of ratings'].hist(bins=70)
# Comment: Most of the movies were not reviewed.

# %%
# Checking the distribution of average rating
ratings['rating'].hist(bins=70)
# Comment: Mean around 3. A bunch of bad movies with the lowest rating. 

# %%
# Checking the relationship between both
sns.jointplot(x='rating', y='num of ratings',data=ratings,alpha=.5)
# Comment: the higher the number of reviews, the higher the rating of a movie