# ###################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 25 - Neural Networks and Deep Learning
# datasets: 
# ###################################

## ANN ###
    # Simplified Biological Neuron Model, we think of them as accepting some sort of input
    # signal which can come from a variety of sources (Dendrites). These are processed in the
    # Nucleus and then transformed into a single output called Axon. This output can be the 
    # input of another Nucleus, and so on.
    # A neural network can be represented matematically through a perceptron (Rosenblatt, F., 1958).
    #
    # A perceptron (or neuron) model has inputs (x1,x2,...), an activation function f(X) and an output y.
    # It is also able to adjust some parameters in order to make it "learn" by adding adjustable
    # weights to each input (w1,w2,...). 
    # Note in case an input has a value of zero, the usage of a weight won't affect the contribution 
    # that this input has on the final output. For that reason, a bias term (b) is added to the inputs.
    # In that sense, the final input entered into an activation function is something like (x1*w1+b,
    # x2*w2+b,...) and \hat y = f(x1*w1+b,x2*w2+b,...). "b" can be thought of as an offset value which
    # makes x*w have to reach a certain threshold before having an effect. We will call x*w+b, z.
    #
    # Basic ANN (multi-layer perceptron model): it uses the output of a set of perceptrons (or perhaps just
    # one) to feed (as input) other perceptrons (or perhaps just one), so on so forth, creating a sort of tree.
    # The first layer is know as input layer, this could be things like tabular data that has features on 
    # info that we are trying to predict a label off of. The last layer is know as the output layer. Any
    # layers in between the input and output layers are the hidden layers, which are difficult to interpret,
    # due to their high interconnectivity and distance away from known input or output values (a sort of 
    # black box). A NN with two or more hidden layers is called a DEEP NN.
    #
    # This framework can be used to approximate any convex continuous function (Lu, Z & Hanin, B.).
    #
    # Activation functions help us contextualizing the output. For instance, we want to get the probability
    # of an event as a result of the NN, then we need a function that transforms the input into something
    # that moves between 0 and 1. Examples:
        # 1.  Step function: f(z) = if z > T then 1, else 0, where T is a threshold set by the user. All 
        #                    changes are not reflected in the output. We also cannot treat the output as 
        #                    a probability.
        # 2.  Sigmoid function (logistic): f(z) = 1/[1+e^(-z)]. We can treat the output as a probability.
        # 3.  Hyperbolic tangent: tanh(z) = sinh(z)/cosh(z), where cosh(z)= [e^x+e^(-z)]/2 and 
        #                         sinh(z) = [e^x-e^(-z)]/2. Its output is between -1 and 1
        # 4.  Rectified Linear Unit (ReLU): f(z) = max{0,z}. It's good when we are dealing with vanishing 
        #                                   gradient. It's the activation function by default for TF, due
        #                                   to its overall good performance.
        # Plenty more, check en.wikipedia.org/wiki/Activation_function.
    #
    # Multi-class activation functions are made for multi-class results or situations. This can happen in 
    # two cases.
        # Non-Exclusive classes: a data point can have multiple classes/categories assigned to it.
            # e.g., a photo can have multiple tags (i.e. beach, family, etc.)

        # Mutually Exclusive classes: on;y one class per data point.
            # e.g. a phot can be categorized as being in graysace or full color. It cannot be both at
            # the same time.
    # The easiest way to organize multiple classes is to simply have 1 output node per class. For this we
    # perform one-hot encoding (or create dummy variables) with each category. It lasts to choose the correct
    # classification activation function.
        # Non-exclusive -> Sigmoid function, since the output will tell the probability of having that class 
        #                  assigned to it. We can also work with a threshold in a way that every class/category
        #                  that trespasses it, then will be assigned to the particular data point.
        # Mutually exclusive -> Softmax function, f(Z)_i = e^(z_i)/(\sum^K_{j=1} e^{z_j}) for i = 1,...,K, where
        #                       K is the number of categories. This function calculates the probabilities
        #                       distribution of the event over K different events, i.e., it calculates the 
        #                       probabilities of each target class over all possible target class. Then, the
        #                       class is chosen by the neuron that has the highest probability.
    #
    # Cost function: 
    # The output \hat y is the model's estimation of what it predicts the label to be (output layer). But, 
    # after the network creates its prediction, (i) how do we evaluate it? and after the evaluation 
    # (ii) how can we update the network's weights and biases?
    # Answering (i), we compare the prediction with the actual values (from the test sample) using the cost
    # function (i.e., loss function). This must be an average so it can output a single value.
    # Recall z = w*x+b, now f() will be sigma() and \hat y, will be a. So sigma(Z)=a. Examples of cost functions:
        # Quadratic cost function: C = 1/(2n) * \sum_x ||y(x) - a^L(x)||^2, where L signals the output layer, so 
        #                          a^L is the output from the last layer. Squaring keeps everything positive and
        #                          punishes large errors.
        # Cross Entropy loss function: Used for classification problems. This assumes that our model predicts a 
        #                              probability distribution p(y=i) for each class i=1,2,...,C.
        #                              For binary classification, C = -(y*log(p) + (1-y)*log(1-p)).
        #                              For M number of classes > 2, C = \sum_{c=1}^M y_{o,c}*log(p_{o,c}).
    # The cost function depends on (W,B,S^r,E^r), W are the weights, B are the biases, S^r is the input of a single
    # training sample and E^r is the desired output of tha training sample. Note that a(x) has encoded information
    # about W, B.
    # Answering (ii), we minimize the cost function w.r.t. its weights (and biases). Take into account that this is 
    # a n-dimensional problem (due to n weights) so taking derivative and setting it equal to zero will not actually 
    # work. Instead we will use gradient descent (a stochastic process). For that:
        # 1.   We take a seed or initial point.
        # 2.   We calculate the slope at that point (since we are dealing with N-dimensional vectors (called tensors), we
        #      end up calculating the gradient, instead of a simple derivative).
        # 3.   We move in the downward direction of the slope.
        # 4.   We repeat the process till we converge to zero (zero gradient), indicating a minimum.
    #   In the process we could have chosen the step size to find each next point, smaller steps sizes take longer to find 
    #   the minimum; larger steps sizes are faster, but we risk overshooting the minimum (missing it). The step sizes is also
    #   called the learning rate. What we can use is an adaptive gradient descent in order to, e.g., start with larger steps, 
    #   then go smaller as we realize the slope gets closer to zero. An optimized version was coded in 2015 and is called ADAM,
    #   which stands for 'A Method for Stochastic Optimization'.
    #
    # Backpropagation.
    # We want to know how the cost function results changes with respect to the weights in the network, so we can update the 
    # weights to minimize the cost function. Recall the input of the last layer is z^L = w^L*a^{L-1}+b^L (notice this is an
    # example where the last nueron depends only on a previous neuron), and a^{L-1} is the output of that previous neuron.
    # How sensitive is the cost function to the weights and biases in the last layer? 
    #   \partial C_0/ \partial w^L = (\partial z^L / \partial w^L) * (\partial a^L / \partial z^L) * (\partial C_0 / \partial a^L)
    #   \partial C_0/ \partial b^L = (\partial z^L / \partial b^L) * (\partial a^L / \partial z^L) * (\partial C_0 / \partial a^L)
    #
    # The idea here is that we can use the gradient to go back through the network and adjust our weights and biases to minimize 
    # the output of the error vector on the last output layer. 
    #
    # IN SUMMARY
    # STEP 1: using x set the activation function a for the input layer. The resulting feeds into the next layer (and so on).
    # STEP 2: for each layer, we are computing a z^l = w^l*a^{l-1}+b^l and an a^l = sigma(Z^l).
    # STEP 3: we compute our error vector:
            # \delta^L= ∇_a C  ⊙ \sigma'(Z^L), where ⊙ is the Hadamard product (element-wise product); binary operation that takes
            #                                  two matrices of the same dimensions and produces another matrix of the same dimesion
            #                                  as the operands, where each element i, j is the products of elements i, j of the 
            #                                  original two matrices. Note ∇_a C = (a^L-y), which expresses the rate of change of C
            #                                  w.r.t. the output activations.
    # STEP 4: we back propagate the error vector, which is calculating the error back through every other single layer. In that way
            # we can adjust by Ws and Bs. Then, for each layer: L-1, L-2,... we compute ∂^l=(w^{l+1})^T ∂^{l+1} ⊙ \sigma'(Z^l), where
            # (w^{l+1})^T is the transpose of the weight matrix of l+1 layer.
            # The transposition of the weight matrix can be thought of as moving the error backward through the network, giving us
            # some sort of measure of the error at the output of the lth layer. So when we take the Hadamard product, this moves the 
            # error backward through the activation function in the layer l, giving us the error ∂^l in the weighted input to layer l.
            #
            # Note, the gradient of the cost function is given by:
                # for each layer: L-1, L-2,... we compute:
                    # \partial C/ \partial w^l_{jk} = a^{l-1}_k ∂^l_j
                    # \partial C/ \partial b^l_{j}  = ∂^l_j










        




# %% 
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import string
from nltk.corpus import stopwords
from sklearn import pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
#from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

#%matplotlib inline

os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_Py_DataScience_ML/nlp_data')
# %%
# Downloading a data set from the nltk librabry
#nltk.download_shell()  # write 'stopwords'

# %%
# Loading the dataset and checking its format
