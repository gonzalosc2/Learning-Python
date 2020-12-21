####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 14 - Introduction to Machine Learning
# other: N/A
####################################

# MACHINE LEARNING - SUPERVISED LEARNING
# Uses algorithms that are trained using labeled examples. It's usually an input
# where the desired ouput is known. That means within our dataset we're going to 
# have some historical features with historical labels. 
# Commonly used in applications where historical data predicts likely future events.

## The process:
# 1. Data acquisition.
# 2. Data cleaning: often using Pandas.
# 3.1. Test data: usually 30% of the data.
# 3.2 Model training & building: we use this specific training set on our model in order
#                                to fit a model to this training data.
# 4. Model testing (back and forth with step 3): we use test data to know how well our model
#                                                actually performed. In that way, we compare
#                                                the model's prediction to the actual correct
#                                                label that the test data had.
# 5. Model deployment.

# Issue: is it fair to use our single split of the data to evaluate our models performance? No.
# Since we were given the chance to update the model parameters again and again with that same
# data.
# How to fix it? -> Separate the data -actually- in 3 sets!
# 1. Training data: training model parameters.
# 2. Validation data: used to determine what model what model hyperparameters to adjust.
# 3. Test data: used to get <some> final performance metric (truly unseen data).

# Model Evaluation for CLASSIFICATION PROBLEMS (suitable for categorical values)
# In the real world not all incorrect or correct matches hold equal value when comparing model
# prediction with correct labels, instead we use a set of classification metrics, all related 
# by a confusion matrix. From it, we can get the following CLASSIFICATION ERROR METRICS.
#   Accuracy: measures the number of correct predictions made by the model divided by the total
#             number of predictions. Useful when target classes are well balanced.
#   Recall: ability of a model to find all the relevant cases within a dataset. Measures the number
#           of true positives divided by both the number of true positives and false negatives.
#   Precision: ability of a classification model to identify only the relevant data points (or the 
#              proportion of the data points our model says was relevant that actually were relevant).
#              Measures the number of true positives divided by both the number of true positives 
#              and false positives. Note the trade-off betweeen recall and precision.
#   F1-Score: combinated measure between recall and precision (harmonic mean)
#             F_1 = 2*(precision*recall)/(precision+recall)
#             It punishes extreme values (e.g. a classifier with recall 0 and precision 1 gives us
#             a mean of .5. Instead, their F1-score is 0).

# Confusion Matrix:
#                                  |            predicted condition
#             |  total population  | prediction postive         | prediction negative
# true        | condition positive | true positive              | false negative (T-II error)
# condition   | condition negative | false positive (T-I error) | true negative
#
# E.g., disease diagnosis
# True positive: someone actually having a disease and our model correctly predicting that she has it
# True negative: someone actually NOT having a disease and our model correctly predicting that she
#                does not have it
# False positive: someone actually NOT having a disease and our model INcorrectly predicting that she has it
# False negative: someone actually having a disease and our model INcorrectly predicting that she does
#                 not have it

# Model Evaluation for REGRESSION PROBLEMS (suitable for continuous values)
#   Mean absolute error (MAE): 1/n Sum_i^n | y_i \hat y_i |
#                              it does not punish large errors.
#   Mean squared error (MSE): 1/n Sum_i^n (2) y_i \hat y_i )^2
#                             it punishes large error predictions, but changes
#                             squares the unit of measurement.
#   Root mean square error (RMSE): sqrt[] 1/n Sum_i^n (2) y_i \hat y_i )^2) ]
# Their interpretaion will always depend on the context. A RMSE of $10 is splendid for predicting the 
# price of a house, but horrible for predicting the price of a candy bar. Try to compare it with the 
# average value of the label in our data.

# Python: each algorithm exposed via an estimator
#from sklearn.family import Model
#from sklearn.family import LinearRegression
#from sklearn.cross_validation import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

## only on SUPERVISED ESTIMATORS
# model.fit(X_train,y_train)  
# model.predict(X_test)
# model.predict_proba()       # for classification problems, some estimator also provide this method,
#                               which return the probability that a new observation has each categorical
#                               label. In this case, the label with the highest probability is returned by
#                               model.predict().
# model.score()               # for classification or regression problems, most estimators implement a 
#                               score method. Scores are between 0 and 1, with a larger score indicating a
#                               better fit.

## only on UNSUPERVISED ESTIMATORS
# model.fit(X_train)          # predict labels in clustering algorithms.
# model.transform()           # given an unsupervised model, transform new data into the new basis. This
#                               also accepts one argument X_new, and return the new representation of the
#                               data based on the unsupervised model.
# model.fit_transform()       # some estimator implement this method, which more efficiently performs a fit 
#                               and a transform on the same input data.
