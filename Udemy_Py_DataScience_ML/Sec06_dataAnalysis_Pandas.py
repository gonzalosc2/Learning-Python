####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 06 - Python for Data Analysis, Pandas
# other: N/A
####################################

# PANDAS
# To know: Pandas will try to turn all numeric data into float in order to retain
# as much information as possible
import pandas as pd
import numpy as np

## Series (data type)
# It is like a NumPy array that contains axis labels so it can be indexed by a
# label.
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}
pd.Series(data = my_data)  # w/o labels
pd.Series(data = my_data, index = labels)
pd.Series(arr,labels)  # NumPy arrays or lists work equally as a Series
pd.Series(data = labels)  # string data

# if we have a dictionary, the following line is unnecesary
pd.Series(data = my_data, index = d)
pd.Series(data = d)  # this is a simplified version

# very flexible, e.g., built-in functions within a Series
pd.Series(data = [sum,print,len])  # not used in reality

# indexing - it will depend on the data type is my index
ser1 = pd.Series([1,2,3,4],['USA','Germany','Chile','Japan'])
ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])

ser1['USA']
ser1[0] == ser1['USA']

# operations are by label - if there is no match, then a NaN is return
ser1 + ser2

## DataFrames (made of Series objects)
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(data = randn(5,4),index = ['A','B','C','C','E'], \
                  columns = ['W','X','Y','Z'])
df

# each column is Series
df['W']
df.W  # SQL nomenclature is also allowed!! [it can be messy, since it can get
      # confounded with a DataFrame method!]
type(df['W'])
# df['column']['row'] - numeric indexing works just for rows
df['W']['A']
df['W'][0]
type(df['W']['A'])
df[['W','Z']] # an extract from a DataFrame which is a DataFrame by itself
type(df[['W','Z']])

# creating a new column - it can be defined as it already exists
df['new'] = df['W'] + df['Y']
df

# deleting columns or rows - it does not happen in place!!
df.drop('new',axis = 1)  # deletes the specified columns
df.drop(['B','C'])  # deletes the specified rows
#df.drop[['B','C'], axis = 0]  # same as previous command, but by default
df  # not in place!!!
# to make it happen in place, I have to options
df = df.drop('new',axis = 1)  # re-define df
#df.drop('new',axis = 1, inplace = True) # activate the inplace option
df

# shape or DataFrame dimensions
df.shape  # 2-tuple: (columns, rows)

# selecting rows
# using loc - note it requires to use brackets instead of parentheses.
df.loc['A']  # series
df.loc[['A','B']]  # DataFrame
# using numerical position with iloc
df.iloc[0]
df.iloc[[0,1]]

# selecting subsets
df.loc['B','Y']  # row first, column second
df['Y']['B']  # column first, row second
df.loc['B','Y'] == df['Y']['B']

df.loc[['A','B'],['W','X']]
df[['W','X']][:2]
df.loc[['A','B'],['W','X']] == df[['W','X']][:2]

# conditional selection
booldf = df > 0
df[booldf]  # NaN when the value is false
df['W']>0  # a series
df[df['W']>0]  # filtering by rows that fulfill the specified condition

# working with a filtered dataset
### one way
new_df = df[df['Z']<0]
new_df['X']
### another way
df[df['Z']<0][['X','Y']]
### and / or does not normally work in this environment, since we have plenty
### of values within a column. Both are built to be use for comparing just
### a single True/False value, not multiple (truth value of a Series is
### ambiguous). Instead what we need to use is the & symbol for 'and' and | for
###  'or'. These, now, are going to allow us to make multiple comparisons at
### the same time
df[(df['W']>0) & (df['X']>1)]
df[(df['W']>0) | (df['X']>1)]

# reseting / setting the index - not occurring in place!
df.reset_index()  # it resets index values to numbers and creates a new column
                  # with their former values
#  df.reset_index(inplace = True)  # in place!
newind = 'CA NY WY OR CO'.split()  # fast way to create a new list
df['States'] = newind
df.set_index('States')  # setting an existing column as index
df
