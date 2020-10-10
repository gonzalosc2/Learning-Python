####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 10 - Errors and Exceptions
# other: N/A
####################################

# ERRORS HANDLING
# try: block of code to be attempted (may lead to an error).
# except: block of code to be executed in case there is an error in try block.
# finally: final block of code to be executed, regardless of an error.

def add(num1,num2):
    return num1 + num2

number1 = 10
#number2 =  input('Please enter a number: ')
number2 =  int(input('Please enter a number: '))

try:
    result = add(number1,number2)
#Only one of these block will run
except:
    print('It looks like you are not adding correctly!')
else:
    print('Add went well')
    print(result)

####################################
# Including an error
try:
    f = open('testfile','r')
    f.write('write a a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS Error')
#except:
#    print('All other exceptions!')
finally:  # this block will always run
    print('I always run')

# Without an error
try:
    f = open('testfile','w')
    f.write('write a a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OS Error')

finally:
    print('I always run')

####################################
# While with error handling
def ask_for_int():

    while True:
        try:
            result = int(input('Enter a number: '))
        except:
            print('Ups, no number was entered')
            continue
        else:
            print('Correctly entered!')
            break
        finally:  # barely used
            print('Last message.')

ask_for_int()

####################################
# TESTING: as we make changes or update our code, we could run test files
#          to make sure previous code still runs as expected.

# TOOLS:
#   pylint: this is a library that looks at the code and reports back possible issues.
#   unittest: this is a built-in library that will allow to test our own programs
#             and check that we are getting desired results.

###
# pylint
#pip install pylint
# In the terminal type
# pylint name_of_the_file.py -r y

###
# unittest (for further details check test_cap.py file. That one should be run
# in the terminal: python name_of_test_file.py)
#import unittest
#import three

# CODE: (Notice the package unittest should be inherited in the created class)
#class TestCap(unittest.TestCase):

#    def test_one_word(self):
#        text = 'python'
#        result = three.cap_text(text)
#        self.assertEqual(result,'Python')

#    def test_multiple_words(self):
#        text = 'monty python'
#        result = three.cap_text(text)
#        self.assertEqual(result,'Monty Python')
