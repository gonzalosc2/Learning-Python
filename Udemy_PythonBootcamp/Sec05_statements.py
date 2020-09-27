####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 05 - Python Statements
# other: N/A
####################################

# Control Flow: We only want a certain code to execute when a particular
# condition has been met

# CONLONS and INDENTATIONS are crucial!

# -----------------------
# IF / ELIF / ELSE

# if some _condition:
#   execute some code
# elif some_other_condition:
#   do something different
# else:
#   do something else

# Notice it does not require to put and end to the statement (as in matlab)

if True:
    print("It's true!")

hungry = True

if hungry:
    print("feed me!")
else:
    print("I'm not hungry")

loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('I love money')
else:
    print('I do not know much')

# -----------------------
# FOR LOOPS
# It can be done over characters in a string, an itme in a list or over every
# key in a dictionary

# my_iterable = [1, 2, 3]
# for item_name in my_iterable:
#   print(item_name)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    # check for even numbers
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in list1:
    list_sum = list_sum + num
    print(list_sum)

print('\nOutside the for loop')
print(list_sum)

mystring = "Hello World"

for letter in mystring:
    print(letter)

# When we are not planning to use the items specifically, we will use an
# underscore (_) and this will allow us to iterate through all the characters
# on the string value
for _ in mystring:
    print('Hello!')

tup = (1, 2, 3)
mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
len(mylist)

for item in mylist:
    print(item)

# Tuple and packing (with no parenthesis works as well)
for (a, b) in mylist:
    print(a)
#    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

# Two ways of getting the values from a dictionary
for item in d:
    print(d[item])

for value in d.values():
    print(value)

# Two ways of getting the keys from a dictionary
for key in d:
    print(key)

for key, value in d.items():
    print(key)

# Getting the dictionary back
for item in d.items():
    print(item)

# -----------------------
# WHILE

# while some_boolean_condition:
#   do something
# else:
#   do something different

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
    # x += 1 (another way to write the previous line)

else:
    print('X is not less than five')

# break: breaks out of the current closest enclosing loop
# continue: goes to the top of the closest enclosing loop
# pass: does nothing at all

x = [1, 2, 3]
for item in x:
    # comment

for item in x:
    # comment
    pass

print('end of my script')

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
        # break
    print(letter)

# -----------------------
# USEFUL OPERATORS

mylist = [1, 2, 3]

# RANGE function: it is a generator
for num in range(10):
    print(num)

# range(start, stop[, step])
for num in range(4, 10, 2):
    print(num)

# The following line is supposed to work, but it does not
list(range(1, 11, 2))

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1  # index position

index_pos = 0
word = 'sherezade'

for letter in word:
    print(word[index_pos])
    index_pos += 1

# Tuples
for item in enumerate(word):
    print(item)

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# ZIP function: matches up items on different lists
# The resulting tuple will be of the size of the shortest list
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

list(zip(mylist1, mylist2, mylist3))

# IN operator: useful to quickly check if an elements in inside an object
'x' in [1, 2, 3]
'x' in ['x', 'y', 'z']

'mykey' in {'mykey': 244}
d = {'mykey': 244}
244 in d.keys()
244 in d.values()

# Built-in operators
mylist = [10, 20, 30, 40]
max(mylist)
min(mylist)

# RANDOM library
from random import shuffle  # in-place function
mylist = [10, 20, 30, 40, 3, 8, 13]
shuffle(mylist)
mylist

from random import randint  # random interger number
randint(0, 100)

# INPUT function: it records everything as a string
result = input('Enter a number here: ')
result
type(result)
float(result)
int(result)

# LIST COMPREHENSIONS
mystring = 'hello'

mylist = []

for letter in mystring:
    mylist.append(letter)

# Flatting the for loop
myList = [letter for letter in mystring]
mylist1 = [num for num in range(0,10)]
mylist2 = [num**2 for num in range(0,10)]
mylist3 = [num**2 for num in range(0,10) if num%2==0]

celcius = [0,10,20,34.5]
fahrenheit = [( (9/5)*temp+32) for temp in celcius]

## IF and ELSE in a list COMPREHENSIONS (better to separete it for readeability)
results = [x if x%2==0 else 'ODD' for x in range(0,11)]

## Nested loops
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)

mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
