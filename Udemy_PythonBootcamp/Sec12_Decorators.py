####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 12 - Decorators
# other: N/A
####################################

# DECORATORS allow us to add extra functionality to an already existing functions
# without having to create a new function. These provide an "on/off" switch
# than can be turn on just on situations when we really need this additional
# functionality.
#
# They use the @ symbol and should be place above the original function.
#
# These are commonly used in web framework such as Django and Flask.

### Baseline: idea behind decoretors:
## Functions defined within a function

# Example 1:
def hello(name = 'Gonzalo'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello'

    def welcome():
        return '\t This is the welcome() func inside hello'

    #print(greet())
    #print(welcome())
    print('I am going to return a function!')

    # we will return a function that it is within another function
    if name == 'Gonzalo':
        return greet
    else:
        return welcome

new_func = hello()

new_func()
print(new_func())

# Example 2:
def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool

some_func = cool()

some_func()

## Passing in a function as an argument
def hello():
    return 'Hi Gonzalo!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

hello()
other(hello)

### Decorators in practice:
def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function!')

    return wrap_func

# One way:
def func_needs_decorator():
    print('I want to be decorated!')

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

# Second way (most common):
@new_decorator  # on/off switch
def func_needs_decorator():
    print('I want to be decorated!')

func_needs_decorator()
