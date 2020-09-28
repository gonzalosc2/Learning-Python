####################################
# author: Gonzalo Salazar
# purpose: lecture notes
# course: Computer Science 1 at Boston College
# other: N/A
####################################

# Modules or libraries
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



t
