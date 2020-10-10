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
my_list_copy = my_list[:]  #slicing

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

# FILES
