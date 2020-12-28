####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 15 - Linear Regression
# other: N/A
####################################

#%%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#%matplotlib inline
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/lr_data')

#%%
df = pd.read_csv('USA_Housing.csv')

# %%
# Brief descriptive statistics from the data
df.head()
df.info()
df.describe()

# %%
# Describing the data we'll work with
sns.pairplot(df)
sns.displot(df['Price'],kde = True)
sns.heatmap(df.corr(),cmap = 'Greens')
plt.show()

# %%
# Establishing the data we'll work with as well as defining training and testing samples
X = df[df.columns[:5]]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.4, random_state=101)

## TRAINING/ESTIMATION
# %%
# Instantiating a linear regression model and training it
lm = LinearRegression()  
lm.fit(X_train,y_train)

# %%
# Estimated coefficients 
cdf = pd.DataFrame(lm.coef_,X.columns, columns = ['Coeff'])
cdf

# Interpretation (example)
# holding everything else constant, a one unit increase in average area income
# is associated with a 21.52 dolars increase in the unit price

#%%
## PREDICTION
predic = lm.predict(X_test)  # predicted housing prices

# Checking how well is performing the model
plt.scatter(y_test,predic)

# Plotting residuals
sns.displot(y_test-predic, kde = True)  
# Notice residuals are normally distributed -> model selected was a correct choice for the data.

# %%
# Measuring performance
m1 = metrics.mean_absolute_error(y_test,predic)
m2 = metrics.mean_squared_error(y_test,predic)
m3 = np.sqrt(metrics.mean_squared_error(y_test,predic))
error_measurement = pd.DataFrame([m1,m2,m3],['MAE','MSE','RMSE'],columns = ['Value'])
error_measurement

####################################################################################
# PROJECT EXERCISE - Ecommerce Customers

