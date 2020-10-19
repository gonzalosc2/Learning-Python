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
#             value at a specific index
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
#
