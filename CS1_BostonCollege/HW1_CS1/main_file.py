# author: Gonzalo Salazar
# assigment: Homework #1
# description: Main .py file

# Loading functions from another .py files
import dob
from a_dayweek import day_of_the_week
from b_hitlist import hitlist

# Asking the user about her date of birht
D = dob.valid_day()
M = dob.valid_month()
YYYY = dob.valid_year()

print('What would you like to do?  \na) Show day of the week for date \nb) Show the hit songs of the week \nq) quit')
# Asking the user what does she want to do next
valid = False
while not valid:
    answer = input('Please answer: a, b or, q')
    if answer == 'a' or answer == 'b' or answer == 'q':
        valid = True
    else:
        print('The answer is incorrect. Please enter a valid answer (a, b or q)')

if answer == 'a':
    print(day_of_the_week(DAY=D, MONTH=M, YEAR=YYYY))
elif answer == 'b':
    hitlist(DAY=D, MONTH=M, YEAR=YYYY)
else:
    exit()
