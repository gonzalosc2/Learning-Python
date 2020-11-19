# author: Gonzalo Salazar
# assigment: Midterm #3

# description
'''
Write a function named lineIndex that takes a file name, fName, as a parameter
and returns a dictionary, d, that indexes the words in fName by line number,
with the first line in fName being numbered 0.

Each word in fName should be a key in the returned dictionary d, and the
corresponding value should be a list of the line numbers on which the word
occurs. A line number should occur no more than one time in a given list of
line numbers.

The file fName contains only upper and lower case letters and white space.
Capital and lower case letters are different. That is, 'You' is not the same
word as 'you'.
'''

# script
import os

os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/CS1_BostonCollege/Midterm_3')

def lineIndex(fName):

    with open(fName, mode = 'r') as f:

        my_list = []
        for line in f:
            my_list.append(line.strip().split())

        d = {}
        i = 0
        for sublist in my_list:
            for value in sublist:
                if value not in d:
                    d[value] = [i]
                elif d[value][-1] == i:
                    pass
                else:
                    d[value].append(i)
            i += 1

        return d

# checking
print(lineIndex('makeItRain.txt'))
