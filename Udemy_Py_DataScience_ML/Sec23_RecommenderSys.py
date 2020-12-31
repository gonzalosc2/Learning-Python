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
import sklearn
#%matplotlib inline

os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/rsys_data')
# %%
# Loading and visualizing data


df = pd.DataFrame(cancer['data'],columns = cancer['feature_names'])
df.head()
