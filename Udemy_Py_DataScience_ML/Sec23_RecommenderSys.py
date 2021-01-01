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
columns_names = ['user_id','item_id','rating','timestamp']
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

# %%
# Creating a matrix of user_id vs. movies where values = rating
moviemat = df.pivot_table(index = 'user_id',columns='title',values='rating')
moviemat.head()
# Comment: there are plenty of missing values since not everyone has seen all movies

# %%
# Checking out the most rated movies again and choosing two movies and grabbing their
# user ratings
ratings.sort_values('num of ratings', ascending = False).head(10)
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
# Comment: Choosing Star Wars and Liar Liar

# %%
# Computing the pairwise correlation between rows or columns of two DataFrame objects
# (instead of just the index or columns of a DataFrame)
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()
# Comment: We get a bunch of titles of movies adn the correlation column, which tells us 
#          how correlated this movies user ratings were to the user rating of the Star 
#          Wars movie.

# %%
# Sorting values out
corr_starwars.sort_values('Correlation',ascending=False).head(10)
#Comment: Notice that some correlations do not make sense because most likely these
#         movies happened to have been seen only by one person who also happened to
#         rate Star Wars five stars. We can fix this by filtering movies that have
#         under a certain number of reviews.

# %%
# Checking the histogram of movies by number of ratings, we see that after a 100 
# reviews the histogram seems to 'normalize' or decline seriously.
corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head(10)

# %%
# Checking for Liar Liar
corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head(10)