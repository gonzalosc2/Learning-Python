####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 14 - Advanced Python Modules
# other: N/A
####################################

# COLLECTIONS MODULE
# Implements specialized container data types that are essentially alternatives
# to Python's built-in container (dict. or tuple) that are just general purpose.

## Counter: specialized dictionary. elements are dict. keys and counts are the
#          values
from collections import Counter

mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
mylist2 = ['a','b','a',10,10,10]

Counter(mylist)
Counter(mylist2)

sentence = 'How many times does each word show up in this sentence with a word'
Counter(sentence.lower().split())

letters = 'aaaaaabbbbbcccccdddddddddd'
c = Counter(letters)

# there are functions within the class such as most_common
c.most_common(3)
c.most_common(1)

## Defaultdict: assigns a default value if there is an instance where a key
# error would have occurred
from collections import defaultdict

d = {'a':10}
d
d['a']

d['WRONG']  # not present in a default dict. (error!)

# Helps to keep the code running
d = defaultdict(lambda: 0)
d['correct'] = 100
d['correct']
d['WRONG key']

## Namedtuple: helps when we have long tuples and it is difficult to remember a
#              value at a specific index
mytuple = (10,20,30)
mytuple[0]

from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age = 5, breed = 'Husky', name = 'Sam')
type(sammy)

sammy
sammy.age
sammy.breed
sammy[0]

# OS MODULE
# Allows to do things like get the current working directory or list all the
# files in a directory. These commands work in any OS or any Python script
import os

os.getcwd()
#pwd  # only works on jupyter and terminal

os.listdir()
os.listdir('/Users/gsalazar/Documents/C_Codes/')

f = open('practice.txt','w+')
f.write('Hey, I am new here!')
f.close()

# SHELL MODULE
# Allows to move files in different directions or in different locations
# Make sure to have admin permissions in order to perform this module in certain
# folders
import shutil

shutil.move('/Users/gsalazar/Documents/C_Codes/Coding-Projects/practice.txt',
            '/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp')

os.listdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp')

# Removing files
## Permanently (dangerous)
#os.unlink(path) which deletes a file at the provide path
#os.rmdir(path) which deletes a folder (folder must be empty) at the provide path
#shutil.rmtree(path) which remove all files and folders contained in the path

## Temporarily (sending files to trash)
pip install send2trash

import send2trash

os.listdir()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp')
os.listdir()
send2trash.send2trash('practice.txt')

# Directory tree generator
# For each directory in a directory tree rooted at the top, it is going to
# yield a tuple (dirpath, dirnames, filenames)
file_path = '/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp'
for folder, sub_folders, files in os.walk(file_path):
    print(f'Currently looking at {folder}')
    print('\nThe sub folders are:')
    for sub_fold in sub_folders:
        print(f'\t Subfolder: {sub_fold}')

    print('\nThe files are: ')
    for f in files:
        print(f'\t File: {f}\n')

# DATETIME MODULE
# Allows to create objects with day and time, time zone and operations between
# date time objects, such as how many seconds have passed
import datetime

mytime = datetime.time(2,20)
mytime.minute
mytime.hour
print(mytime)

type(mytime)

today = datetime.date.today()
date = datetime.date(2020,10,10)
print(today)
print(date)

today.year
today.month
today.day

today.ctime()

from datetime import datetime

mydatetime = datetime(2021,10,3,14,20,1)
print(mydatetime)

# if we made a mistake and we want to change an element from the datetime object
mydatetime.replace(year = 2020)
print(mydatetime)

# calculating time between to dates
## using a date object (might have issues with leap years)
from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2
type(result)

## using a datetime object
datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)

result1 = datetime1 - datetime2
result1.seconds
result1.total_seconds()
result1.days

# MATH MODULE
# Holds a ton of useful math functions
import math

value = 4.35
math.floor(value)
math.ceil(value)
round(4.35)  # not part of the math module

# generally we want to choose to always round to either all evens or all odds.
# Notice that if we always chose to round down(up) when it came to a point five,
# split something right in the middle, then all our estimates overt time would
# be lower(larger) than they should be.
# If we choose a rule based off a numbr being even or odd, then we start to even
# itself out because we'll round down as many times (hopefully) as we round up
round(4.5)  # 4
round(5.5)  # 6

math.pi
math.e
math.inf
math.nan

math.log(math.e)
math.log(100,10)
math.sin(10)
math.degrees(math.pi/2)
math.radians(180)

# RANDOM MODULE
# Containes a lot of mathematical random functions as well as random functions
# for grabbing a random item from a python list
import random

random.randint(0,100)

# run the following three commands together several times
random.seed(11)
random.randint(0,100)
random.randint(0,100)

mylist = list(range(0,20))
random.choice(mylist)

# sample with replacement
random.choices(population = mylist, k = 10)

# sample without replacement
random.sample(mylist, k = 10)

random.shuffle(mylist)
mylist

random.uniform(a=0,b=100)
random.gauss(mu=0,sigma=1)

# PYTHON DEBUGGER
# Allows to set a trace, which is essentially going to pause operations,  mid
# script and then allow us to play with variables to understand what is going on

x = [1,2,3]
y = 2
z = 3

result = y + z
result1 = x + z

import pdb

x = [1,2,3]
y = 2
z = 3

resul_one = y + z

pdb.set_trace()  # type "quit" or "q" in order to exit the debugger
result_two = x + z

# REGULAR EXPRESSIONS
# Allows us to create specialized pattern strings and then search for matches
# within text
import re

# Phone Number: (555)-555-5555
r"(\d\d\d)-\d\d\d-\d\d\d\d"
r"(\d{3)-\d{3}-\d{4}"  # does the same as above, but it uses quantifiers
# r informs Python that this string should not be treated as a normal string.
# Instead, it tells Python that there's actually identifiers within this string
# Each identifier is a just a placeholder (a wild card) waiting for a matches
# based on a particular data type.
# identifiers:
#   \d: looks for digits
#   \w: looks for alphanumerics
#   \s: looks for white space
#   \D: looks for non digits
#   \W: looks for non-alphanumerics
#   \S: looks for non-whitespace

# quantifiers:
#     +: occurss one or more times
#   {x}: occurs exactly x times
#   {x,y}: occurs x to y times
#   {x,}: occurs x or more times
#     *: occurs zero or more times
#     ?: occurs once or none

text = "The agent's phone number is 408-555-1234. Call soon!"
'phone' in text

# nothing is found
pattern = 'NOT IN TEXT'
re.search(pattern,text)

# when something is found
pattern = 'phone'
re.search(pattern,text)
match = re.search(pattern,text)
match.span()
match.end()

# when there are more than one match
text = 'my phone once, my phone twice'
match = re.search('phone',text)
match.span()  # it only takes care of the first match
matches = re.findall('phone',text)  # it returns a list with matches

# to get actual match operator (each one), we should use finditer()
for match in re.finditer('phone',text):
    print(match)  # basically search()
    print(match.span())
    print(match.group())  # basically findall()

phone = re.search(r'\d{3}-\d{3}-\d{4}',text)  # important to add r before ' '
phone
phone.group()

# compile() allows us to group/compile together different regular expression
# pattern codes, which can then be broken down
# (e.g., if we want to get the area code)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)  # import
results.group()   # groups together all patterns in the compile function
results.group(1)            # note index starts at 1
results.group(2)  # groups together all patterns in the second group
results.group(3)

# searching for more than one element
re.search(r'cat|dog', 'The cat is here')   # | serves as OR operator
re.findall(r'at', 'The cat is hat sat there')   # without wildcard
re.findall(r'.at', 'The cat is hat sat there')   # . serves as a wildcard. we can
                                                 # use as much as we want
re.findall(r'^\d','1 is ...')   # ^ serves to find an identifier at the beginning
                                # of the whole text (note in the middle)
re.findall(r'\d$','The number is 2')   # ^ serves to find an identifier at the
                                       # end of the whole text

# excluding patterns (useful to get rid of punctuation)
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'
re.findall(pattern,phrase)

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall(r'[^!.? ]+',test_phrase)  # the space removes the spaces
' '.join(clean).lower()

# including patters
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'   # w/o brace notation also works, but difficult to read
                           # as well as allows us to group things together
re.findall(pattern,text

# combining or with other pieces of text
text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
textthree = 'Hello, have you seen this caterpillar?'

re.search(r'cat(fish|nap|claw)',text)
re.search(r'cat(fish|nap|claw)',texttwo)
re.search(r'cat(fish|nap|claw)',textthree)

# TIMING THE CODE
# Allows to distinguish which lines of code are more efficient than others
import time  # simple, but not designed for that purpose, won't catch slight diffs

def func_two(n):
    return list(map(str,range(n)))

## Current time before
start_time = time.time()

## Run code
result = func_two(1000000)

## Current tiem after running code
end_time = time.time()

## elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)

import timeit  # designed for this purpose

stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str,range(n)))
'''

timeit.timeit(stmt,setup,number = 100000)

# if we do not want to setup an environment, then use %%timeit, since it uses
# previously defined functions
%%timeit   #only works in a Jupyter notebook (or here: Atom!)
func_two(100)

# ZIPPING/UNZIPPING FILES
import os
#os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp')
f = open('fileone.txt','w+')
f.write('one file')
f.close()
f = open('filetwo.txt','w+')
f.write('one file')
f.close()

import zipfile
# does not work for compressing entire folders at once

# create the zip file first!
comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type = zipfile.ZIP_DEFLATED)
comp_file.close()

# extracting files from a zip file
#zip_obj = zipfile.extract('NAME.ext')  # it only extracts on
zip_obj.extractall('extracted_content')

import shutil
dir_to_zip = '/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)

shutil.unpack_archive('example.zip','final_unzip','zip')
