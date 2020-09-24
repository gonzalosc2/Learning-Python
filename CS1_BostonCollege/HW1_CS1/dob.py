# author: Gonzalo Salazar
# assigment: Homework #1
# description: Captures day, month and year or birth

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
