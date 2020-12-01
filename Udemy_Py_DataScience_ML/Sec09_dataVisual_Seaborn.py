####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 09 - Python for Data Visualization, Seaborn
# other: N/A
####################################

# Seaborn
# conda install seaborn

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# to see plots created inside a Jupyter Notebook, then type
#%matplotlib inline
# this library has some built-in data sets which can be used to work with
tips = sns.load_dataset('tips')
tips.head()

### Distribution Plots
## Univariate Plots - Histogram
    # the kernel density estimator is plotted by default
sns.distplot(tips['total_bill'], kde = False, bins = 30)

## Bivariate Plots
sns.jointplot(x = 'total_bill', y = 'tip', data = tips)  # scatter plot

    # the option kind allows us to select which kind of graph do we want inseide the
    # the main plot
sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'hex')
sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'reg') # linear regression
    # a 'kde' kind essentially just shows us the density of where the points
    # match up the most
sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind = 'kde')

    # a pairplot plots pairwise relationships across an entire data frame, at
    # least for the numerical columns
sns.pairplot(tips)
    # the hue option allows us to distinguish between categorical values in a pairplot
sns.pairplot(tips, hue = 'sex', palette = 'coolwarm')  # color palette can be used

## Rug plots: it draws a dash mark for every single point along the distribution line.
#            The higher the concentration of dashes, the taller the histogram bar.
sns.rugplot(tips['total_bill'])

#   In order to get a KDE we need to plot a distribution for each dash. Commonly,
#   a normal distribution is used (in that case, it should be centered on each dash).
#   Once done, all these distributions should be summed up.

### Categorical Plots
## Bar plot: it allows us to aggregate the categorical data based off of some
#            function.
sns.barplot(x = 'sex', y = 'total_bill', data = tips)  # mean by default
sns.barplot(x = 'sex', y = 'total_bill', data = tips, estimator = np.std)  # std

## Count plot: a bar plot that explicitly counts the number of occurrences
sns.countplot(x = 'sex', data = tips)

## Box plot: shows the distribution of quantitative data in a way that hopefully
#            facilitates comparisons between the variables
sns.boxplot(x = 'day', y = 'total_bill', data = tips)
    # here mean, and quartiles are plotted. The whiskers (the T lines) show the rest
    # of the distribution. The points that are outside of these whiskers
    # considered outliers.

sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'smoker')
    #using hue allows us to split the plot by another categorical variable again

## Violin Plot: it shows the distribution of the data across some sort of category,
#              allowing to plot all the components that correspond to actual data
#              points and it's essentially showing the kde of the underlying
#              distribution. In contrast to the box plot, it is a little harder
#              to interpret.
sns.violinplot(x = 'day', y = 'total_bill', data = tips)
sns.violinplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex',split = True)

# Strip Plot: it draws a scatter plot where one variable is categorical
sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True)
sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True,
              hue = 'sex', dodge = True)  # split was renamed as dodge

## Swarm Plot: similar to a stripplot except the points are adjusted so that they
#             do not overlap.
sns.violinplot(x = 'day', y = 'total_bill', data = tips)
sns.swarmplot(x = 'day', y = 'total_bill', data = tips, color = 'black')

## Factor Plot: a more general plot, similar to previous one, but now we have to
# specify its kind. Also know as sns.catplot( )
sns.factorplot(x = 'day', y = 'total_bill', data = tips, kind = 'bar')
sns.factorplot(x = 'day', y = 'total_bill', data = tips, kind = 'violin')

##########################################
flights = sns.load_dataset('flights')
flights.head()

### Matrix Plots
# It requires data already be in a matrix form, so that the index name and the
# column nme match up so that the cell value actually inicates something that
# is relevant to both of those names. This can be achieved through correlations
# or using Pivot Tables.
tc = tips.corr()

## Heat map: it colors pairwise relations between variables.
sns.heatmap(tc, annot = True, cmap = 'coolwarm')

fp = flights.pivot_table(index = 'month',columns = 'year', values = 'passengers')
sns.heatmap(fp, cmap = 'coolwarm')
sns.heatmap(fp, cmap = 'magma', linecolor = 'white', lw = .2)

## Cluster map: it uses hierachical clustering to produce a clustered version of
#               a heat map.
sns.clustermap(fp, cmap = 'coolwarm', standard_scale = 1)
    # In this case, years and months are put together according to their similarity

##########################################
iris = sns.load_dataset('iris')
iris.head()
iris['species'].unique()

### Grids: give us more control to define what we really want to be plotted.
g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

## Facet Grid:
g = sns.FacetGrid(data = tips, col = 'time', row = 'smoker')
#g.map(sns.distplot,'total_bill')
g.map(sns.scatterplot,'total_bill','tip')

## Regression Plots
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex',
           markers = ['o','v'], scatter_kws = {'s':100})  # s: size

sns.lmplot(x = 'total_bill', y = 'tip', data = tips, col = 'day', hue = 'sex',
           aspect = 0.6, size = 8)

### Style and colors
#sns.set_style('white')
sns.set_style('ticks')
#sns.set_style('darkgrid')
#sns.set_style('whitegrid')
sns.countplot(x='sex',data=tips)
sns.despine(left = True, bottom = True)

## Size
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)

## Context
sns.set_context(context = 'paper', font_scale = 1)
sns.countplot(x='sex',data=tips)

## Color
sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex',
           palette = 'winter')
    # Color maps can be found here: https://matplotlib.org/3.3.3/tutorials/colors/colormaps.html
