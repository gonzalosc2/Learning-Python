####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 03 - Python Object and Data Structure Basics
# other: N/A
####################################

# -----------------------
# NUMBERS

# Basic Operations: sum, difference, division, multiplication
3+4
4-3
3/4
4*3

# Special Operations: "mod" or Modulo. It is the remainder after division.
7/4
7/3
6/6

# Special Operations: power
2**3

# Different ways to write 100
50*2
120-20+20-2*10
(5**2)*4
round(400/4)

# -----------------------
# VARIABLE ASSIGNMENTS

a = 5
a = a ** 2
my_meals = 1.5
type(a)
type(my_meals)

my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate

print(my_taxes)

# -----------------------
# STRINGS

# Print: one line, two lines (w & w/o indentation), tabulation
print('hello world')
print('hello \n world')
print('hello \nworld')
print('hello \tworld')

# Length
len('hello')
len('hello wonderful world')

# Indexing starts at zero
char = 'hello'
char[0]
char[1]
char[2]
char[3]
char[4]

# Reverse indexing also works, when we want to start from the end
char[0] == char[-5]
char[1] == char[-4]
char[2] == char[-3]
char[3] == char[-2]
char[4] == char[-1]

# Slicing: [start:stop:step]; step by default is 1
char2 = 'I_like_to_code_in_Python'
char2[-6:-1:1]
char2[0:10:1]
char2[0:10:2]
char2[0:10:3]
char2[10:]
# when using [:stop] it is to stop, but not including the stop
char2[:6]
# when using [:-step] reverses the string
char2[::2]
char2[::4]
char2[::-1]
char2[::-2]
char2[::-4]

# -----------------------
# STRINGS: PROPERTIES AND METHODS

# Immutability: second line (l95) will show an error
name = 'Sam'
"name[0] = 'P'"

# Concatenation
last_letters = name[1:]
name1 = 'P' + last_letters
x = 'Hello World'
x = x + ' it is beautiful outside!'
letter = 'z'
letter * 10

# Be careful with these situations: (i) is a number, (ii) is a string
2 + 3
'2' + '3'

# Features: after definining a variable, use a dot and choose among the options
# For some features parenthesis should be typped in, otherwise it will display
# what is the command for. Using ".split" helps us to create a list with each
# word on a string (by default considering the blank/white space)
x.upper()
x.lower()
x.capitalize()
x.split()
x.split('o')

# Interpolation: .format add the specified text inside the curly braces
print('This is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
'           2   1   0            0       1         2'
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# Float formatting
result = 100/777
print('The result was {}'.format(result))
print('The result was {r}'.format(r=result))
# Float formatting follows "{value:width.precision f}": width is just the
# length we want for the output
print('The result was {r:1.3f}'.format(r=result))

# f-strings: formatted string literals. It is another way to do what is above
name = 'Jose'
age = 3
print(f'Hello, his name is {name}. His {age} years old')

# -----------------------
# LISTS: OBJECTS RETRIEVED BY LOCATIONS
# Ordered sequence can be indexed or sliced

my_list = ['one', 'two', 'three']
my_list2 = ['STRING', 100, 23.4]
my_list[0]
my_list[1:]
my_list[:2]
another_list = ['four', 'five']
new_list = my_list + another_list
print(new_list)

# Mutation is possible here
new_list[0] = 'ONE ALL CAP'
print(new_list)

# Add/removing items from a list. Default value for poping is "-1", the end
new_list.append('six')
print(new_list)
new_list.pop()
print(new_list)
new_list.pop(3)
print(new_list)

# Sort and reverse
awesome_list = ['a', 'e', 'x', 'b', 'g']
awesome_list_num = [1, 434, 535, 12, 43, 5, 664, 2, 43]
sorted(awesome_list)
print(awesome_list)
print(awesome_list_num)
awesome_list.sort()
awesome_list_num.sort()
print(awesome_list)
print(awesome_list_num)
awesome_list.reverse()
awesome_list_num.reverse()
print(awesome_list)
print(awesome_list_num)

# -----------------------
# DICTIONARIES: OBJECTS RETRIEVED BY KEY NAME
# Unordered and cannot be sorted

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict['key1']
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
prices_lookup['oranges']
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
d['k2']
d['k2'][2]
d['k3']['insideKey']

# Similarities wih R
g = {'key1': ['a', 'b', 'c']}
g['key1'][2].upper()
newest_list = g['key1']
letter = newest_list[2]
letter.upper()

g['key2'] = 200
print(g)
g['key2'] = 'NEW'
print(g)

g.values()
g.keys()
g.items()

# -----------------------
# TUPLES: SIMILAR TO LISTS, BUT THEY ARE IMMUTABLE

t = ('a', 'a', 'b')
my_list = [1, 2, 3]
type(t)
type(my_list)

t.count('a')
# .index() returns the positions the specified value appears first
t.index('a')

# -----------------------
# SETS: UNORDERED COLLECTION OF UNIQUE ELEMENTS

myset = set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset)

mylist = [1, 1, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 3]
set(mylist)

# -----------------------
# BOOLEANS: OPERATORS THAT ALLOW TO CONVEY T OR F STATEMENTS

True
type(True)
1 > 0
1 > 2
1 == 1

# Helpful when we have to define something before a loop, for example.
# Otherwise we might get an error
b = None
type(b)

# -----------------------
# FILES: CREATING A .TXT FILE

pwd
# cd '/Users/gsalazar/Documents/C_Codes/Python'

%%writefile myfile.txt
Hello this is a text file
this is the second line

open('myfile.txt')
myfile = open('myfile.txt')
open('whoops_wrong.txt')

# Reads what is on the .txt file. To read it again I should reset the starting
# point
myfile.read()
myfile.read()
myfile.seek(0)
myfile.read()

# Helpful if I want to translate the file into a list
myfile.seek(0)
myfile.readlines()

# We should close it once I am done working with it
myfile.close()

# We could not worry about closing a file if we "open" as follows.
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

# open() is already a built-in function. The following file has only permission
# to be read
with open('myfile.txt', mode='r') as myfile:
    print(myfile.read())

# The following file has only permission to be written (overwrite)
with open('myfile.txt', mode='w') as myfile:
    contents = myfile.read()

# mode='a': append onlu (add on to files, lines)
# mode='r+': reading and writing
# mode='w+': writing and reading (overwrites existing file or creates one)

with open('myfile.txt', mode='a') as myfile:
    myfile.write('\nTHREE ON THIRD')

with open('myfile.txt', mode='r') as myfile:
    print(myfile.read())

with open('sample.txt', mode='w') as myfile:
    myfile.write('I CREATED THIS FILE!')

with open('sample.txt', mode='r') as myfile:
    print(myfile.read())
