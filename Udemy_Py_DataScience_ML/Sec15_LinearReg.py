####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 15 - Linear Regression
# other: N/A
####################################

#%%
import os
from numpy.lib.function_base import corrcoef
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

del y, X, X_test, X_train, y_train, y_test, m1, m2, m3, error_measurement, lm, predic

####################################################################################
# PROJECT EXERCISE - Ecommerce Customers
# %%
# Reading in the Ecommerce Customers csv file as a DataFrame called customers
df_ecomm = pd.read_csv('Ecommerce Customers')

# Checking the head of customers, and checking out its info() and describe() methods
df_ecomm.head()
df_ecomm.info()
df_ecomm.describe()

# %%
## Exploratory Data Analysis
# Comparing the Time on Website and Yearly Amount Spent.
sns.jointplot(y = 'Time on Website', x = 'Yearly Amount Spent', data = df_ecomm)

# Comparing the Time on APP and Yearly Amount Spent.
sns.jointplot(y = 'Time on App', x = 'Yearly Amount Spent', data = df_ecomm)
# Comment: given the first correlation, which is null, it might be happening that people 
#          visiting the website find it interesting and then continue following through the
#          App (if they did not already started following it through the App since the very 
#          beginning). Perhaps people prefer to use the App because it is more convenient 
#          since they do not have to turn on a PC each time they want to buy something as 
#          well as they can use the App wherever they want to. Besides, since they have their
#          smartphones with them all the time, they can spend more time shopping and selecting
#          what they really want to buy, this also eases the way the buy something since they
#          only need to press a bottom to buy (assuming they can register their card on their
#          devices).
#          
#          The previous phenomenon might be explaining why the yearly amount spent is 
#          positively associated with spending more time on APP. The correlation between 
#          both is not pefect, though (around 0.5).

# %%
# Comparing Time on App and Length of Membership
sns.jointplot(y = 'Time on App', x = 'Length of Membership', data = df_ecomm, kind = 'hex')
# Comment: similarly people who spend more time on App is positively correlated with people who
#          hold older memberships. This phenomenon might be explained by the fact that older
#          members found the App easier to use compared to the Website given the experience they 
#          have had across the years. Perhaps those who remain using the website are people who
#          is reluctant to switch, or that do not understand how to use it very well. Here, 
#          a measure for technology's insertion and age, would be great to measure that.

# %%
# Exploring types of relationships across the entire data set
sns.pairplot(df_ecomm)
# Comment: those who have yearly spent more are those who have older memberships (the strogest
#          correlation). This might be a fidelity effect, in the sense that people who have 
#          spent more years buying in here, are the ones who prefer to buy all their clothing 
#          with us.

# %%
# Create a linear model plot (using seaborn's lmplot) of Yearly Amount Spent vs. Length of 
# Membership.
sns.lmplot(y = 'Yearly Amount Spent', x = 'Length of Membership', data = df_ecomm)
# Comment: this plot reassures what was my interpretation above.

# %%
## Training the model
y = df_ecomm['Yearly Amount Spent']
X = df_ecomm[df_ecomm.columns[3:7]]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state=101)

# Instantiating a linear regression model
#lm = LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
lm = LinearRegression()
lm.fit(X_train,y_train)

# %%
## Predicting with the model
predic = lm.predict(X_test)

# Checking performance
sns.scatterplot(predic,y_test)

# %%
# Evaluating the model by calculating the Mean Absolute Error, Mean Squared 
# Error, and the Root Mean Squared Error
m1 = metrics.mean_absolute_error(y_test,predic)
m2 = metrics.mean_squared_error(y_test,predic)
m3 = np.sqrt(metrics.mean_squared_error(y_test,predic))

error_measurement = pd.DataFrame([m1,m2,m3],['MAE','MSE','RMSE'],columns = ['Value'])
error_measurement

# %%
# Plotting a histogram of the residuals and make sure it looks normally distributed
sns.distplot(y_test-predic, bins = 50)

# %%
## Interpreting
coef = pd.DataFrame(lm.coef_,X.columns,columns = ['Coeff'])
coef 
# Comment: more focus should be put on membership time instead of increasing
#          efforts on the mobile app or in a website development. More people
#          should follow and remain following the business. Notice, a one-year
#          increase in membership time is associated with a 61.27 increase in 
#          yearly amount spent (compared to a 0.19 and 38.59 associated with
#          both time on Website and time on App, resp.). Though the company 
#          should also focus more on their mobile app.

# NOTICE: IN THIS PROJECT WE HAVEN'T USED HYPOTHESIS TESTING TO EVALUATE 
#         THE SIGNIFICANCE OF EACH COEFFICIENT!