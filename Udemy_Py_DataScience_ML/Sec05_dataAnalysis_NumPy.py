####################################
# author: Gonzalo Salazar
# course: Python for Data Science and Machine Learning Bootcamp
# purpose: lecture notes
# description: Section 05 - Python for Data Analysis, NumPy
# other: N/A
####################################

# NUMPY
import numpy as np

print(np.zeros((5,5)))  # notice that the standar way to create a matrix is using a tuple
print(np.random.rand(5))  # but in these cases it is unnecessary
print(np.random.rand(5,5))
print(np.random.randn(2))
print(np.random.randn(2,2))
print(np.random.randint(1,100))  # exclusive at the high end
my_array = np.random.randint(1,100,10)
print(my_array)

## reshape - shoots an error if dimensions are higher than the actual number of values
print(my_array.shape)
ma1 = my_array.reshape(2,5)
ma2 = my_array.reshape(5,2)
ma3 = my_array.reshape(10,1)
print('(2,5): ', ma1, '(5,2): ', ma2, '(10,1): ', ma3)

my_array.max()
my_array.min()
my_array.argmax()  # index value at which max is located (instead of using index())
my_array.argmin()

my_array.dtype  # data type inside an array (instead of type())

## broadcasting
arr = np.arange(0,10)
print(arr)
arr[1:5] = 100
print(arr)

## shallow copy problem - Python does it to save memory on large arrays
slice_of_arr = arr[0:6]
print(slice_of_arr)
slice_of_arr[:] = 10
print(slice_of_arr)
print(arr)

## deep copy
arr = np.arange(0,10)
arr_copy = arr[0:6].copy()
arr_copy[:] = 84
print(arr_copy)
print(arr)

## boolean arrays and conditional selection
arr = np.arange(1,11)
my_bool_arr = arr > 5
print(arr[my_bool_arr])

## matrices
arr_2d = np.arange(50).reshape(5,10)
arr_2d[1:3,3:5]

## operations - element by element
arr = np.arange(0,11)
arr+arr
arr-arr
arr+2
arr**2
arr / arr # for operations that are not possible Python will return a warning
          # (instead of an error), and a nan on the value that was not possible
          # to calculate
1 / arr  # or inf, in case the operation returns an infinite value

## universal array functions
np.sqrt(arr)
np.exp(arr)
np.sin(arr)
np.log(arr)
