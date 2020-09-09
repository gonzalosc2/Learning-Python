# author: Gonzalo Salazar
# assigment: Homework #1
# description:

def valid_day():
    valid = False
    while not valid:
        try:
            day = int(input('What day you were born? [1-31]'))
            if day < 1 or day > 31:
                print('That is incorrect, please enter a valid number between 1 and 31')
            else:
                valid = True
        except ValueError:
            print('That is incorrect, please enter a valid number between 1 and 31')
    return day

def valid_month():
    valid = False
    while not valid:
        try:
            month = int(input('What month you were born? [1-12]'))
            if month < 1 or month > 12:
                print('That is incorrect, please enter a valid number between 1 and 12')
            else:
                valid = True
        except ValueError:
            print('That is incorrect, please enter a valid number between 1 and 12')
    return month

def valid_year():
    valid = False
    while not valid:
        try:
            year = int(input('What year you were born? [1900-2020]'))
            if year < 1900:
                print('You are actually dead, please enter a valid number between 1900 and 2020')
            elif year > 2020:
                print('You have not even born yet, please enter a valid number between 1900 and 2020')
            else:
                valid = True
        except ValueError:
            print('That is incorrect, please enter a valid number between 1900 and 2020')
    return year


# Asking the user about her date of birht
D = valid_day()
M = valid_month()
YYYY = valid_year()

print('What would you like to do?  \na) Show day of the week for date \nb) Show the hit songs of the week \nq) quit')
# Asking the user what does she want to do next
valid = False
while not valid:
    answer = input('Please answer: a, b or, q')
    if answer == 'a' or answer == 'b' or answer == 'q':
        valid = True
    else:
        print('The answer is incorrect. Please enter a valid answer (a, b or q)')

# Loading functions from another .py files
from a_dayweek import day_of_the_week
from b_hitlist import hitlist

if answer == 'a':
    print(day_of_the_week(DAY=D, MONTH=M, YEAR=YYYY))
elif answer == 'b':
    hitlist(DAY=D, MONTH=M, YEAR=YYYY)
else:
    exit()



pwd
