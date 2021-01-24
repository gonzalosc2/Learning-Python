####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 21 - K Means Clustering
# datasets: (i) sklearn datasets: make blobs (to create artificial data). (ii) College admissions
####################################

### K MEANS ###
# Unsupervised learning algorithm that attempts to group similar clusters together in the data.
# That means to divide data into distinct groups such that observations within each group are 
# similar. 
# 
# Algorithm:
#   1. Choose a number of clusters: K
#   2. Randomly assign each point to a cluster.
#   3. Until clusters stop changing, repeat the following steps:
#       a. for each cluster, compute the cluster centroid by taking the mean vector of points in the cluster.
#       b. assing each data point to the cluster for which the centroid is the closest.
# 
# How to choose K? --> No easy answer.
#   1. Elbow method.
#       -> Compute the SSE (sum of squared distance between each member of the cluster and its centroid) for some values of K.
#       -> Plot K against the SSE, notice the error decreases as K gets larger. 
#          (Larger # clusters -> Smaller the clusters -> smaller distortion)
#       -> Then, chose the K at which the SSE decreases abruptly ("elbow effect").

# %% 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans 
from sklearn.metrics import confusion_matrix,classification_report

#%matplotlib inline
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/kmeans_data')

# %%
# Creating artificial data
data = make_blobs(n_samples = 200, n_features=2,centers = 4, cluster_std=1.8,random_state=101)

# Checking how data looks like
data  # tuple ([1] generated samples, [2] corresponding clusters)
data[0].shape

# %%
# Visualizing the blobs (clusters)
plt.scatter(data[0][:,0],data[0][:,1], c = data[1])

# %%
# Applying K Means algorithm
kmeans = KMeans(n_clusters=4)
kmeans.fit(data[0])
 
# %%
# Checking cluster centroids
kmeans.cluster_centers_

# %%
# Checking predicted labels (clusters)
kmeans.labels_

# %%
fig, (ax1,ax2) = plt.subplots(1,2,sharey=True,figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1],c=kmeans.labels_)

ax2.set_title('Original')
ax2.scatter(data[0][:,0],data[0][:,1],c=data[1])
plt.show()

####################################################################################
# PROJECT EXERCISE 
# %%
# Loading and visualizing data
df = pd.read_csv('College_Data',index_col=0)
df.head()

# %%
# Checking information and more description of the data.
df.info()
df.describe()

# %%
## EXPLORATORY DATA ANALYSIS
sns.scatterplot(y='Grad.Rate',x='Room.Board',data=df,hue='Private')
plt.show()
# Comment: Non-private-college students have a lower graduation rate compared to those
#          studentes attending to private colleges.

# %%
sns.scatterplot(y='F.Undergrad',x='Outstate',data=df,hue='Private')
plt.show()
# Comment: Private colleges concentrate a lower number of full-time students compared to non-private colleges.
#          Additionally, it seems like outstate tuition is bounded around 12,500 (with some outlier colleges),
#          compared to the wide variety of outstate tuition shown by private schools.

# %%
sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
g = g.map(plt.hist,'Outstate',bins=20,alpha=0.7)
# Comment: Once again, out-of-state tuition is lower in non-private colleges.

# %%
sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
# Comment: the graduation rate in private colleges is more concetrated towards higher,
#          values compared to non-private colleges. Note there is private school acting
#          as an outlier.

# %%
df[(df['Grad.Rate']>100) & (df['Private']=='Yes')]
# Comment: the name of the previously mentioned school is Cazenovia College.

# %%
# Correcting the outlier
df['Grad.Rate']['Cazenovia College'] = 100

# %%
# Checking if the correction worked
sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',size=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
# Comment: yes! it worked.

# %%
## K MEANS CLUSTERING
kmeans = KMeans(n_clusters=2)
kmeans.fit(df.drop('Private',axis=1))

# Cluster centroids
kmeans.cluster_centers_

# %%
## EVALUATION (FICTICIOUS EXERCISE)
def converter(cluster):
    if cluster=='Yes':
        return 1
    else:
        return 0

df['Cluster'] = df['Private'].apply(converter)

# %%
print(confusion_matrix(df['Cluster'],kmeans.labels_))
print(classification_report(df['Cluster'],kmeans.labels_))