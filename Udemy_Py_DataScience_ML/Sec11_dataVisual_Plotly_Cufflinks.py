####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 11 - Python for Data Visualization, Plotly and Cufflinks
# other: N/A
####################################

# Due to an update, I should be considering the following:
#
# 1. Possible Import Error 1: You need to install a new package. In your command
#line type and run:
#   pip install chart-studio
#
# Then in jupyter make sure you import it by running the code:
#    import chart_studio.plotly as py
#
# 2.Possible Colorscale Error 2: In the "Real Data US Map Choropleth", when
# you are creating the data dictionary, make sure the colorscale line
# is = 'ylorbr', not 'YIOrbr'... so like this:
#    colorscale='ylorbr'
#
# 3.Possible projection Error 3: In the "World Map Choropleth", when you are
# creating the layout, ensure that your projection line
# is = {'type':'mercator'} not Mercator with a capital...so like this:
#   projection={'type':'mercator'}

#conda install plotly
#pip install cufflinks  # connects ployly with Pandas

# Plotly and Cufflinks
import pandas as pd
import numpy as np
#from plotly import __version__
#print(__version__)
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot

# Connecting JavaScript (interactive library) to a Python script
init_notebook_mode(connected=True)
# Making offline use of cufflinks
cf.go_offline()
# DATA
df = pd.DataFrame(np.random.randn(100,4),columns = 'A B C D'.split())
df.head()

df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
df2

## Interactive plots!!
df.iplot()

df.iplot(kind = 'scatter',x='A',y='B',mode = 'markers')  # size option also available
df2.iplot(kind = 'bar',x='Category',y='Values')

# aggregation or groupby method
df.sum().iplot(kind = 'bar',mode = 'markers')

df.iplot(kind = 'box')
df['A'].iplot(kind = 'hist',bins = 40)
df.iplot(kind = 'hist',bins = 40)  # overlapping histograms for comparison
df.iplot(kind='bubble',x='A',y='B',size='C')
df.scatter_matrix()  # similar to a pairplot

# 3D surface plot
df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})
df3.iplot(kind = 'surface',colorscale='rdylbu')

# financial data visualization
df[['A','B']].iplot(kind = 'spread')
