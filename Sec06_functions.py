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

    
