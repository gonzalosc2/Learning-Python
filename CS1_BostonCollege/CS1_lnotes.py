####################################
# author: Gonzalo Salazar
# purpose: lecture notes
# course: Computer Science 1 at Boston College
# other: N/A
####################################

# MODULES OR LIBRARIES
import random

# Interger division
7//3

# Print many values
x = 1
y = 6
v = 4
print(x, y, v)

phr1 = 'love you'
phr2 = 'I'
print(phr1, phr2)
print(phr1, phr2, end = " ")

# Assigning two variables
c, b = 2, 3
c
b
c, b

# Random library
random.randint(1, 6)

# FUNCTIONS
# Parenthesis are mandatory
def function_name():
    print('Hey!')
    return print('Python will finish the function here, anything after will not be ran')
    print('NOOOO!')

# when None appears it means that we forgot to use return in a function

def even_odd(number):
    if number%2==0:
        return 'Even'
    else:
        return 'Odd'

# SLEEP
from time import sleep  # any library should be loaded at the beginning of the script

sleep(1)  # it suspends the execution of the script for the specified # of seconds (e.g., 1)

h = 2
m = 1
s = 30

print("%1d% 02d:%02d" % (h,m,s))
print("%1d:%02d:%02d" % (h,m,s))
print("%3d:%02d:%02d" % (h,m,s))
print("%02d:%02d:%02d" % (h,m,s))

# % recognizes that we want to change the format of the variable
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# WHILE
# when using "continue", it jumps to the next iteration of the while, no matter what follows after the "continue"
# it skips the next lines and star from the beginning of the next iteration

# LISTS
# Shallow copy: is a pointer or a reference, so if I change the value of the reference
# it will change where it is used

my_list = [2,3,4,5,6,7]
print(my_list)

l2 = my_list  #shallow copy
print(l2)

l2[0] == "anna"
print(my_list, l2)

# Deep copy: creates a new space in memory for a list already existing, so it will
# not have a shallow copy's problem

    # one way
my_list_copy = [] #creates a new space in memory
for item in my_list:
    my_list_copy.append(item)

print(my_list, my_list_copy)
my_list_copy[2] = "gonzalo"
print(my_list, my_list_copy)

    # another way
l3 = my_list.copy()
l3[1] = 'the best'
print(l3, my_list)

# STRINGS
# split(","), separates by the comma
# split(), separates by space
# string.strip(), gets rid of the specified character at the beginning or at the end.
#   It only work on strings, it does not work if it is applied to a list.
#   In that case a for should be used to go through each word.
# string.replace(old,new), returns a copy of the original string with all the
#   letters in lower case, it does not modify the original string
# find(x), delivers the value of the index that the substring occupies equal to
#   x within the string
# find(x,start), gives the value of the index that occupies the substring equal
#   to x within the string, looking from the start position onwards

# deep copy - due to slicing/sub list
my_list = [111,222,333,444,555]
my_list_copy = my_list[:]  #slicing  #only works for a list with single elements
                           #inside. For list of lists it will be a shallow copy.
                           #In that case, we should use deepcopy from copy module

my_list_copy.remove(111)

print('after remove')
print(my_list)
print(my_list_copy)

# shallow copy - due to slicing/sub list
my_list = [111,222,333,444,555]
my_list_copy = my_list  # passing by reference

my_list_copy.remove(111)

print('after remove')
print(my_list)
print(my_list_copy)

# slicing
my_list = [111,222,333,444,555]
#           0   1   2   3   4
#          -5  -4  -3  -2  -1

# example where to start we should count from the right and to end, we should
# start from the left
my_list[-2:4]
my_list[0:1]  # last item is never included

# GENERATORS
#range(j): generates a list with values from 0 to j-1
#range(i,j): generates a list with values from i to j-1
#range(i,j,k): generates a list with values from i to j-1, and k is the step

# There is a problem with range(j): it has to generate a list with j values, for
# example if we are using it with a for, since Python has to know where are we as
# well as how many elements rest to cycle through. If the list is huge, this
# will be costly in terms of memory. Instead there is a solution provided by
# the xrange() function, which allows us to create the elements at the time they
# are used and thus saves memory.

# NUMPY (basically MATLAB in Python)
from numpy import *

## ARRAYS
# meant to manipulate vectors of data (numbers)
my_list = [323.42,643.43,656.4,47.546]
my_array = array(my_list)
print(my_list)
print(my_array)
print(3 * my_array + my_array ** 2)
my_array[3]

y = list(range(1,10))
y2 = arange(1,10)
print(y2)
a = zeros(4)
b = ones(10)
print(a, b)
linspace(1,10,10)

## SUBARRAYS (array slicing)
# We also have the issue of shallow copies here. To solve that we use copy()
a = matrix([[1,2,3],[4,5,6],[7,8,9]])
d = copy(a[2:,2:]) # deep copy
print("d: ", d)

c = copy(a[2:,2:])
c[-1] = 999
print("c: ", c)
print("a: ", a)

## MATRICES
a = zeros((4,3))
print("a: ", a)
my_matrix =  matrix([[1,2,3],[4,5,6],[7,8,9]])
print(my_matrix*2)
print(my_matrix+2)
size(my_matrix)  # number of values inside the matrix m times n
my_matrix.shape  # size of the matrix (m x n)
my_matrix.shape[0] # number of rows
my_matrix.shape[1] # number of columns
identity = eye(4)
print(identity)
my_diag = diag([1,2,3,4,5])
print(my_diag)
my_bool_mat = matrix([[True,True,False],[False, True, True]])
print(my_bool_mat)

## SYSTEM OF EQUATIONS
# e.g., solving the following system is easy (Ax=b)
# x -2y = -2
# 3x-2y =  2

print('x = ')
A = matrix([[1,-2],[3,-2]])
b = matrix([[-2],[2]])
x = linalg.solve(A,b)
print(x)

#transposing a matrix
print("x : ", x)
print("x transposed: ",x.T)

# MATPLOTLIB (2D graph library)
import matplotlib.pyplot as plt
import numpy as np

## Step 1 - Creating a figure
plt.figure()

## Step 2 - Loading data and creating the plot
x = np.array([4,6,3,10,7])
plt.plot(x)

## Step 2 - Showing the graph (make sure I run all the steps at the same time)
plt.show()

# another figure
y = np.array(np.arange(len(x)))
plt.figure()
plt.plot(x,y)
plt.title('My Graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

# another figure (smooth cosine)
x = np.linspace(0,10,1000)
y = np.cos(x)
plt.figure()
plt.plot(x,y)
plt.title('My Cosine')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

# plt.clf() clear the windo
# plt.subplots()  graphs inside a graph
# plt.axis()
# plt.ylim() sets limits to y-axis

## bar graphs
plt.figure()
x = [1,2,3,4,5]
y = [4,5,10,15,5]
plt.bar(x,y)
plt.title('My bars')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

## histograms
plt.figure()
x = [1,2,3,4,5,5,4,5,4,3,1,4]
plt.hist(x)
plt.title('My histogram')
plt.xlabel('x-axis')
plt.ylabel('frequencies')
plt.show()

## two lines in the same graph
plt.figure()
x = np.arange(-2*np.pi,2*np.pi,0.1)
plt.plot(x,np.sin(x),label = 'graph1')
plt.plot(x,np.cos(x),label = 'graph2')

plt.legend()
plt.show()

## subfigures
nrows = 2
ncols = 1
plt.subplot(nrows,ncols,1)  # 1 is the index
plt.plot((np.array([4,6,3,10,7])))
plt.subplot(nrows,ncols,2)  # 2 is the index
plt.plot((np.random.uniform(10,15,20)))
plt.show()

## pie chart
a = np.random.uniform(1,10,7)
L = ['b1','b2','b3','b4','b5','b6','b7']
plt.pie(a, labels = L)
plt.title('A pie chart example')
plt.show()

# ADVANCED PYTHON
