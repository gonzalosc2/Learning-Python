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

# multi-level indexing
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
hier_index.levels  # note each index level outside has an inside index
hier_index.levshape  # from outside to inside

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df

### indexing
df.loc['G1']  # data frame, outside index
df.loc['G1'].loc[1]  # series, inside index

### index names
df.index.names  # no names has been assigned
df.index.names = ['Groups','Num']

df.loc['G2'].loc[2]['B']

# cross - sections (xs function): useful when we want to extract info from a
# particular level that is common to each outside index
df.xs('G1')  # easy
df.xs(1,level = 'Num')  # non-trivial

## Missing Data
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)

# dropping missing values
df.dropna()  # it drops any ROW with missing values
df.dropna(axis = 1)  # it drops any COLUMN with missing values
df.dropna(thresh = 2)  # it keeps rows with at least 2 non-na values
df.dropna(thresh = 1)  # it keeps rows with at least 1 non-na values

# filling missing values
df.fillna(value = 'FILL VALUE')
df['A'].fillna(value = df['A'].mean())  # for instance with the mean of the column

## Group By - same sort of stuff from SQL; group together rows based off of
# a column and perform an aggregate function on them
data = {'Company': ['GOOG','GOOG','MSFT','MSFT','FB','FB'], \
        'Person': ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'], \
        'Sales': [200,120,340,124,243,350]}
df = pd.DataFrame(data)

# step 1 - group by a specific column
byComp = df.groupby('Company')

# step 2 - aggregate values using a specific operation (function)
byComp.mean()  # Pandas ignores non-numeric columns, such as Person
byComp.sum()
byComp.sum().loc['FB']
byComp.std()

# all together
df.groupby('Company').sum().loc['FB']
df.groupby('Company').count()

# useful information
df.groupby('Company').describe().transpose()

## Merging, Joining and Concatenating
df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],\
                    'B':['B0','B1','B2','B3'],\
                    'C':['C0','C1','C2','C3'],\
                    'D':['D0','D1','D2','D3']},\
                    index = [0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],\
                    'B':['B4','B5','B6','B7'],\
                    'C':['C4','C5','C6','C7'],\
                    'D':['D4','D5','D6','D7']},\
                    index = [4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],\
                    'B':['B8','B9','B10','B11'],\
                    'C':['C8','C9','C10','C11'],\
                    'D':['D8','D9','D10','D11']},\
                    index = [8,9,10,11])

# contatenating - dimensions should match along the axis we are concatenating on
#                 by default the axis = 0 (along rows)
pd.concat([df1,df2,df3])
pd.concat([df1,df2,df3],axis = 1)  # concatenating aling columns

# merging - similar to SQL
left = pd.DataFrame({'key':['K0','K1','K2','K3'],\
                     'A':['A0','A1','A2','A3'],\
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],\
                     'C':['C0','C1','C2','C3'],\
                     'D':['D0','D1','D2','D3']})

# with the 'how' option we specify the type of merge method we want to use
# (identical to SQL)
pd.merge(left,right,how = 'inner',on = 'key')  # inner is selected by default

left = pd.DataFrame({'key1':['K0','K0','K1','K2'],\
                     'key2':['K0','K1','K0','K1'],\
                     'A':['A0','A1','A2','A3'],\
                     'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key1':['K0','K1','K1','K2'],\
                      'key2':['K0','K0','K0','K0'],\
                      'C':['C0','C1','C2','C3'],\
                      'D':['D0','D1','D2','D3']})

## how = inner: it includes the intersection of cases
pd.merge(left,right,on = ['key1','key2'])
## how = outer: it includes all cases (union)
pd.merge(left,right,how = 'outer',on = ['key1','key2'])
## how = right: it includes all cases from the "right" set, no matter whether
## an intersection with the "left" set exists or not
pd.merge(left,right,how = 'right',on = ['key1','key2'])

# Joining - combines columns of two potentially differently-indexed DataFrames
# into a singre resulting DataFrame
left = pd.DataFrame({'A':['A0','A1','A2'],\
                     'B':['B0','B1','B2']},\
                     index = ['K0','K1','K2'])
right = pd.DataFrame({'C':['C0','C1','C2'],\
                      'D':['D0','D1','D2']},\
                      index = ['K0','K2','K3'])
left.join(right)
left.join(right,how = 'outer')  # same as concatenating by column (axis = 0)

## Operations
df = pd.DataFrame({'col1':[1,2,3,4], \
                   'col2':[444,555,666,444], \
                   'col3':['abc','def','ghi','xyz']})

df.head()  # displays the first n = 5 (by default) number of rows
df.info()  # shows haow many entries are and their data type
df['col2'].unique()  # shows all unique values in a specific array
len(df['col2'].unique())  # displays the number of unique elements
df['col2'].nunique()  # does the same as the previous command
df['col2'].value_counts()  # returns the number of times the values appear

# apply method - broadcast a function to each value in the column it a way
# to implement my own functions apart from those built-in in Python
def times2(x):
    return x*2
df['col1'].apply(times2)

df['col3'].apply(len)  # returns the length of each string value in a column
df['col2'].apply(lambda x: x*2)  # no need to define a function previously

# removing columns
#df.drop('col1',axis = 1,inplace = True)

# names (attributes)
df.columns
df.index

# sorting / ordering
df.sort_values(by = 'col2')

# null values
df.isnull()

# pivot table (similar to Excel) - mainly used to have a multi level DataFrame
data = {'A':['foo','foo','foo','bar','bar','bar'],\
        'B':['one','one','two','two','one','one'],\
        'C':['x','y','x','y','x','y'],\
        'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)

df.pivot_table(values = 'D', index = ['A','B'], columns = 'C')

## Data Input and Output
# required libraries to work with four main data sources: CSV, Excel, HTML, SQL
    #conda install sqlalchemy
    #conda install lxml
    #conda install html5lib
    #conda install BeautifulSoup4

import os

os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/Pandas_examples')

## CSV
df = pd.read_csv('example')  # reading
df.to_csv('My_output',index = False)  # saving - in case we do not use index =
                                      # False, then we will obtain a new column
                                      # in our new file which will appear once
                                      # we wanted to read the new file
pd.read_csv('My_output')

## Excel
# using pd.read_excel( ) my cause Python to crash, since it does not read formulas
# or macros.
pd.read_excel('Excel_Sample.xlsx',sheet_name = 'Sheet1', index_col = 0)
df.to_excel('Excel_Sample2.xlsx',sheet_name = 'NewSheet')

## HTML
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
data  # is a list!
data[0].head()  # we have to cicle in the list to find our DataFrame

## SQL
from sqlalchemy import create_engine  # allows us to create a SQL engine in memory
engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table',con = engine)

sqldf = pd.read_sql('my_table', con = engine)
sqldf
