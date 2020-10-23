####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 20 - Advanced Objects and Data Structures
# other: N/A
####################################

############
# NUMBERS
## Hexadecimal: transforms a number into Hexadecimal
hex(12)
hex(310710931)

## Binary: transforms a number into Binary
bin(32032)
bin(1034)
bin(128)
bin(4)
bin(2)
bin(3)

## Power: function pow  -- mainly related to efficiency cases
2**4
pow(2,4)
pow(2,4,3)  # calculates the (2**4) % 3 (the mod)

## Absolute value
abs(-3)
abs(2)

## Round: by default rounds numbers to zero decimal points
round(3.9)
round(3.141592,2)

############
# STRINGS
s = 'hello world'
s.capitalize()   # capitalizes only the first word
s.upper()
s.lower()
s.count('o')  # counts the number of occurrences the value happens
s.find('o')  # returns the index where the value first happens

## formating methods
#s.center()  # allows to place a string centred between a provided string of
             # certain length
s.center(20,'z')
s.center(18,'z')

#tabulation
print('hello\thi')
'hello\thi'.expandtabs()

#checking format
s = 'hello'
s.isalnum()  # tells whether it is alphanumeric or not
s.isalpha()  # tells whether it is alphabetic or not
s.islower()  # checks whether it is all in lower case
s.isupper()
s.isspace()  # checks whether all characters are white spaces
s.istitle()  # checks whether it is a title case string and there's at
             # least one character in this (each word is capitalized)
s.endswith('o') # checks whether it ends with a certain character
s[-1] == 'o'

#regex
s.split('e') # creates a list of object separated at every occurrence of the
             # character specified. The default character is a space (\n)
s.partition('e') # splits the word at the first instance of this character and
                 # includes it. The output is a tuple. If the character is not
                 # found, then the output is (string,'','')

############
# SETS
s = set()
s.add(1)
s.add(2)
s
s.add(2)
s
s.clear()
s
s1
s.discard(2)  # eliminates a value from the set. If not in it, nothing happens
s
s = {1,2,3}
sc = s.copy()  # hard copy
sc.add(4)

## difference: returns the value that's different between two sets.
##             Should be calculated as follows BiggerSet - SmallerSet
sc.difference(s)

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)  # compares two lists and returns the none duplicated
                          # values from the original list

## intersection: returns common elements from two lists
s1 = {1,2,3}
s2 = {1,2,5}
s1.intersection(s2)
s1
s1.intersection_update(s2)  # changes the value of the original string with
                            # common elements from two lists (origina & comparison)
s1

## disjoint: evaluates whether two sets are intersected (FALSE) or not (TRUE)
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
s1.isdisjoint(s2)
s1.isdisjoint(s3)

## sub- and supersets: returns a boolean as disjoint
s1.issubset(s2)
s2.issuperset(s1)

## symmetric difference: returns the elements that are exactly in one of the sets.
##                       it is the opposite of the intersection
s2.symmetric_difference(s1)
s1.symmetric_difference(s3)
s1.symmetric_difference_update(s3)
s1

## union: returns the elements in both sets
s1 = {1,2}
s1.union(s2)
s1.update(s2)
s1

############
# DICTIONARIES
d = {'k1':1,'k2':2}

# creating a dictionary with dict comprenhension
{x:x**2 for x in range(10)}
