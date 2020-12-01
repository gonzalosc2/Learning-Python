####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 08 - Python for Data Visualization, Matplotlib
# other: N/A
####################################

# Matplotlib
# conda install matplotlib

import matplotlib.pyplot as plt
import numpy as np
import os
# to see plots created inside a Jupyter Notebook, then type
#%matplotlib inline

x = np.linspace(0,5,11)
y = x ** 2

## FUNCTIONAL METHOD
plt.plot(x,y)
#plt.plot(x,y,'r--')  # allows MATLAB specification
plt.ylabel('Y Label')
plt.xlabel('X Label')
plt.show()  # printing a plot

# subplots
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'g')
plt.show()

## OO METHOD
# It allows us to create figure objects and then just call methods off of this.
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])  # left, bottom, width, and height
axes.plot(x,y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')

# another example
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])  # left, bottom, width, and height
axes2 = fig.add_axes([0.2,0.5,0.4,0.3]) # specifies the % value to the left, ...
axes1.plot(x,y)
axes1.set_title('LARGER PLOT')
axes2.plot(y,x,'*', label = 'y on x')
axes2.plot(x,x, label = '45 degree line')  # including another line inside the same plot
axes2.legend(loc = 0)  # loc is between 0 and 10 (inclusive), 0 is the best
#axes2.legend(loc = (0.1,0.1))  # also works
axes2.set_title('SMALLER PLOT')

# subplots
fig, axes = plt.subplots(nrows = 1, ncols = 2)
axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.tight_layout()  # fixes overlapping layouts

## Figure Size and DPI
fig = plt.figure(figsize = (3,2), dpi = 100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

fig,axes = plt.subplots(nrows = 2, ncols = 1, figsize = (3,5))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()

## Saving Figures
os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML')
fig.savefig('my_pic.jpeg')
#fig.savefig('my_pic.jpeg',dpi = 200)

## Plot Appeareance
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,color = 'green',lw = 1)
axes.plot(y,x,color = '#FF8C00')  # RGB Hex Code is also allowed
axes.plot(y,y,linewidth = 5)  # number of times with respect to the value by default
axes.plot((x+5),y,color = 'blue', alpha = 0.5)  # controls the transparency of the line
#axes.plot((x+2),y-5,color = 'purple', linestyle = '--')
#axes.plot(y-5,(x+2), color = 'black',linestyle = ':')
#axes.plot(y-5,(x*2)+5, color = 'gray',linestyle = '-.')
#axes.plot(y,(x*2)+5, color = 'orange',lw = 6, ls = 'steps')
axes.plot(y-5,(x*2)+5,marker = 'o',markersize = 10, \
          markerfacecolor = 'yellow', markeredgewidth = 3, \
          markeredgecolor = 'green')  # '+', '*', '1', 's', ...

## Plot Range
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y,color = 'green',lw = 2,ls='--')
axes.set_xlim([0,1])
axes.set_ylim([0,1])

## Special Plot Types
# Scatter plots
plt.scatter(x,y)
plt.show()

# Histograms
from random import sample
data = sample(range(1,1000),100)
plt.hist(data)
plt.show()

# Boxplots
data = [np.random.normal(0,std,100) for std in range(1,4)]
plt.boxplot(data,vert = True,patch_artist = True)
plt.show()
