####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 10 - Python for Data Visualization, Pandas Built-in DV
# other: N/A
####################################

import pandas as pd
import seaborn as sns
import numpy as np
import os

os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/Pandas_examples')

df1 = pd.read_csv('df1',index_col = 0)
df1.head()
df2 = pd.read_csv('df2')
df2.head()

## Plotting
df1['A'].hist(bins=30)
df1['A'].plot(kind = 'hist',bins = 30)
df1['A'].plot.hist(bins = 30)

df2.plot.area(alpha = 0.4)
df2.plot.bar(alpha = .5,stacked = True)

#df1.plot.line(x=df1.index,y='B')  # it returns me an error
df1['A'].plot.line(alpha=.5,figsize = (12,3), lw = 1)

df1.plot.scatter(x='A',y='B')
df1.plot.scatter(x='A',y='B',c='C',cmap = 'coolwarm')
df1.plot.scatter(x='A',y='B',s=df1['C']*20)

df2.plot.box()

df = pd.DataFrame(np.random.randn(1000,2),columns=['A','B'])
df.plot.hexbin(x='A',y='B',gridsize = 30)

df2['a'].plot.kde()
df2['a'].plot.density()  # the same as the previos command
df2.plot.density()
