"""
Name   : Section 06 - Methods and Functions
Course : 2020 Complete Python Bootcamps: From Zero to Hero in Python
Purpose: Lecture notes
Author : gsalazar
"""

# METHODS
# Built-in objects in Python.
# e.g., append, pop are methods
# a way to discover them is pressing dot (.) and checking displayed options

mylist = [1,2,3,4]
help(mylist.insert)

# FUNCTIONS
# Helps to create clean repeatable code
def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello()
say_hello('Gonzalo')

# I cannot save the results from a def if I just use print at the end.
# It does not generate an output. For that purpose we have to use "return"

# *ARGS (ARGUMENTS or POSITIONAL ARGS) and *KWARGS
# Within a function we have to pass them as tupples
# *ARGS sets a function to take an arbitrary number of arguments
def myfunc(*args):
    return sum(args) * 0.05

def myfunc(*by_convention_spam_is_used):
    return sum(by_convention_spam_is_used) * 0.05

# So we do not need specify ARG by ARG, it will treat all input as a tuple
# Thus, the output is a TUPLE

# **KWARGS sets a function to take an arbitrary number of keyworded arguments
# making a dictionary of key-value pairs. Thus, the output is a DICTIONARY
def myfunc(**kwargs):

    # the DICTIONARY
    print(kwargs)

    # the FUNCTION
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple', veggie='lettuce')

# MIX: **KWARGS + *ARGS (inputs should go in this order!)
def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange',food="eggs",animal='dog')

# Skyline exercise
def myfunc(word='Default'):
    new_word = []
    pos = 0
    length = len(word)
    while pos < length:
        if (pos + 1) % 2 == 0:
            new_word.append(word[pos].upper())
        else:
            new_word.append(word[pos].lower())
        pos += 1
    return "".join(new_word)

myfunc('garogargrr')

# MAP function: passes in the function we want to map to every single element
# in an object (list). It is like "apply" in R
def square(num):
    return num**2

my_nums = [1,2,3,4,5,6]

# you have to iterate
for item in map(square, my_nums):
    print(item)

# or create a list
list(map(square, my_nums))

def splice(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Andy','Eve','Sally']

list(map(splice, names))

# FILTER function: returns an iterator yielding those items of the iterable
# for which when you pass in the item into the function it's true. It requires
# to filter by a function that returs either TRUE or FALSE

def check_even(num):
    return num % 2 == 0

num_list = [1,2,3,4,5,4,3,5,6]

list(filter(check_even,num_list))

# LAMBDA EXPRESSION (converting a statement into a lambda exp step by step)
    # Step 1:
def square(num):
    result = num ** 2
    return result

# Step 2:
def square(num):
    return num ** 2

# Step 3:
def square(num): return num ** 2

# Step 4:
square = lambda num: num ** 2

square(5)

# Lambda expressions are anonymous functions (do not require names)
# If we want to use a function ONE time, it is useful (and efficient)
# to just use a lambda expression (helps us to save lines of coding)
list(map(lambda num:num**2, num_list))

list(filter(lambda num:num%2 ==0,num_list))

list(map(lambda name:name[0],names))

list(map(lambda name:name[::-1],names))

#SCOPE
#LEGB Rule: the order that Python is going to look for variables in.
# Local: Names assigned in any way within a function (def or lambda), and not
# declared global in that function
# Enclosing function locals: Names in the local scope of any and all enclosing
# fucntions (def or lambda), from innner to outer.
# Global (module): Names assigned at the top-level of a modle file, or declared
# global in a def within the file.
# Built-in (Python): Names preassigned in the built-in names module: open,
# range, SyntaxError, etc...

# Local
# lambda num:num**2

# Enclosing
    # GLOBAL (no indentation)
name = 'THIS IS A GLOBAL STRING'

    # ENCLOSING function
def greet():

    name = 'Sammy'

    def hello():
    # LOCAL
        print('Hello ' + name)

    hello()

greet()

# Global
x = 50

def func2(x):
    print(f'X is {x}')

    #LOCAL REASSIGMENT ON A GLOBAL VARIABLE! (Local scope, not defined as
    # "global x")
    x = 200
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

func2(x)
print(x)

def func():
    global x
    print(f'X is {x}')

    #LOCAL REASSIGMENT ON A GLOBAL VARIABLE! (Global scope due to "global x")
    x = 200
    print(f'I JUST LOCALLY CHANGED GLOBAL X TO {x}')

func()

print(x)
