# author: Gonzalo Salazar
# assigment: Midterm #2

# script

import os
import csv
os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/CS1_BostonCollege/Midterm_2')

file = open('file.csv')

lol = []
for row in file:
    lol.append([row.strip()])

print(lol)

file.close()
