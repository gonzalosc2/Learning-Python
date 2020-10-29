# author: Gonzalo Salazar
# assigment: Midterm #2
# name: yellow_submarine

# description
'''Write a function called yellow_submarine (no parameters) that opens the file attached,
read the file and counts the number of times the word is yellow is repeated and the number
of times the word submarine is repeated (it has to count of all them no matter upperCase or lowerCase).

You have to print which word is repeated more times and also how many times each one of them is repeated
'''

# script
def yellow_submarine():

    f = open('yellow_submarine.txt')
    mylist = []
    for row in f:
        mylist.extend(row.lower().strip().split(' '))

        count_yellow = mylist.count('yellow')
        count_submarine = mylist.count('submarine')

    if count_yellow > count_submarine:
        result = 'Yellow is repeated more times than Submarine.'
    elif count_yellow < count_submarine:
        result = 'Submarine is repeated more times than Yellow.'
    else:
        result = 'There is a tie!'

    print(result + '\n' + \
         'Yellow is repeated: ' + str(count_yellow) + '\n' + \
         'Submarine is repeated: ' + str(count_submarine))

# checking
yellow_submarine()
