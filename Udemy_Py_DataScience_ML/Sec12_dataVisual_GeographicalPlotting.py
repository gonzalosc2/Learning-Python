####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 12 - Python for Data Visualization, Geographical Plotting
# other: N/A
####################################

import os

os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/Geo_data')

# two libraries can be used: plotly (interactive framework) or from Matplotlib
# we can use 'basemap'. There might be more libraries, but these are commonly used.

#pip install chart-studio

# CLOROPLETH MAPS
import chart_studio.plotly as py  #instead of, import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd

# Connecting JavaScript (interactive library) to a Python script
init_notebook_mode(connected=True)

## NATIONAL PLOTS
# Example 1

# Building a data dictionary
data = dict(type = 'choropleth',
            locations = ['AZ','CA','NY'],
            locationmode = 'USA-states',
            colorscale = 'Greens',
            text = ['text1','text2','text3'],
            z = [1.0,2.0,3.0],
            colorbar = {'title':'Colorbar Title'})

# Layout nested dictionary
layout = dict(geo = {'scope':'usa'})

# Setting up the object that finally gets passed into iplot()
choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)
#plot(choromap)  # will open html file

# Example 1
df = pd.read_csv('2011_US_AGRI_Exports')
df.head()

data = dict(type = 'choropleth',
            colorscale = 'ylorbr',
            locations = df['code'],
            locationmode = 'USA-states',
            z = df['total exports'],
            text = df['text'],
            # marker generates the separation by states
            marker = dict(line = dict(color = 'rgb(255,255,255)', width = 2)),
            colorbar = {'title':'Millions USD'})

layout = dict(title = '2011 US Agriculture Exports by State',
              geo = dict(scope = 'usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)'))

# Setting up the object that finally gets passed into iplot()
choromap2 = go.Figure(data = [data], layout = layout)
iplot(choromap2)

## INNATIONAL PLOTS
# Example 1
df = pd.read_csv('2014_World_GDP')
df.head()

data = dict(type = 'choropleth',
            locations = df['CODE'],
            colorscale = 'Greens',
            z = df['GDP (BILLIONS)'],
            text = df['COUNTRY'],
            colorbar = {'title':'Billions USD'})

layout = dict(title = '2014 World GDP',
              geo = dict(showframe = False,
                         projection = {'type':'natural earth'}))

choromap3 = go.Figure(data = [data], layout = layout)
iplot(choromap3)
