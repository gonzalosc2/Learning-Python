####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 18 - K Nearest Neighbors
# datasets: fake datasets
####################################

### K NEAREST NEIGHBORS ###
# A CLASSIFICATION algorithm which is divded in two:
#   Training: where we store all the data
#   Prediction:
#       1. Calculate the distance from x (the new point) to all points in our data
#       2. Sort the points in our data by increasing distance from x
#       3. Predict the majority label of the 'k' closest points (where k is a number)
# 
# Notice: the chosen k will affect what class a new point is assigned to.
#
# Smaller k values pick a lot of noise. Larger k values smooth out and creates more bias in the model,
# at the cost of mislabeling some points.
#
# NOTICE: the scale of the variable actually matters a lot and any variable that are on
#         a large scale will have a much larger effect on the distance between observations
#         and because of this when we use KNN we have to try to standarize evertything to the
#         same scale
#
# PROS:
    # Very simple
    # Training is trivial: sorting data
    # Works with any number of classes
    # Easy to add more data
    # Few parameters: K and distance metric
#
# CONS:
    # High prediction cost, which is worse for large data sets (because we have to sort the entire data set)
    # Not good with high dimensional data. It throws off our ability to measure distances in various dimensions
    # Categorical features do not work well with KNN

# %% 
import os
#from numpy.lib.function_base import corrcoef
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix

#%matplotlib inline
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/knn_data')


# %%
# Loading and visualizing data
df = pd.read_csv('Classified Data', index_col=0)
df.head()

# %%
# Standarizing data (note, I we did not consider the variable we want to predict)
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS', axis= 1))  # fits the scale to the data we have
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis = 1))  # transforms the data into a standarized dataset
df_feat = pd.DataFrame(scaled_features,columns = df.columns[:-1])

# %%
# Splitting data by test and train data
X = df_feat
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state=101)

# %%
# Initializing the model and training it
knn = KNeighborsClassifier(n_neighbors = 1)  # using k = 1
knn.fit(X_train,y_train)

# %%
# Predicting points classification
pred = knn.predict(X_test)

# %%
# Checking performance
print('Classification Report')
print(classification_report(y_test,pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,pred))

# %%
# Determining which k is the optimal to maximize performance (Elbow method)
error_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

# %%
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color = 'green',ls = 'dashed',marker='o',markerfacecolor='orange',markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show
# Comment: it seems like 17 is a good value. The error rate is already low son continue increasing k,
#          would only add bias to our prediction

# %%
# Intitializing the "optimal" model with k = 17, training and predicting with it
knn = KNeighborsClassifier(n_neighbors=17)  
knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('Classification Report')
print(classification_report(y_test,pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,pred))

del y, X, X_test, X_train, y_train, y_test, knn, pred, df, df_feat, scaler

####################################################################################
# PROJECT EXERCISE 
# %%
# Loading and visualizing data
df = pd.read_csv('KNN_Project_Data')
df.head()

# %%
# Checking the data to see if there is any pattern
sns.pairplot(df,hue = 'TARGET CLASS', corner = True)
# Comment: it's difficult to make a comment since the data is unlabel

# %%
# Standarizing the variables
scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_feat = scaler.transform(df.drop('TARGET CLASS',axis=1))
df_feat = pd.DataFrame(scaled_feat,columns = df.columns[:-1])
df_feat.head()

# %%
# Splitting data
X = df_feat
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3)

# %%
# Determining which k is the optimal to maximize performance (Elbow method)
error_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors = i)
    knn.fit(X_train,y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

k_opt = error_rate.index(min(error_rate))+1

# Plotting the optimal k
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color = 'green',ls = 'dashed',marker='o',markerfacecolor='orange',markersize=10)
plt.title('Error Rate vs K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show

# %%
# Intitializing the "optimal" model with k_opt, training and predicting with it
knn = KNeighborsClassifier(n_neighbors=k_opt)  
knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('Classification Report')
print(classification_report(y_test,pred))
print('\nConfusion Matrix')
print(confusion_matrix(y_test,pred))