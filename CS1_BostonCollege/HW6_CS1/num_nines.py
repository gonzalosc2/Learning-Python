# author: Gonzalo Salazar
# assigment: Homework #6
# name: num_nines
# description: main .py file with a function that returns the number of times
#              9 appears as a digit in a number specified by the user.
#              I assumed the input value is an interger.

### FUNCTION DEFINITION ###
def num_nines(y):
    "Calculates the number of times 9 appears as a digit in the input value"
    "   INPUT: interger"
    "   OUTPUT: interger"

    y = str(y)

    # Base case
    if len(y) < 1:
        sum = 0

    # Recursive case
    else:
        if y[-1] == '9':
            sum = 1 + num_nines(y[:-1])
        else:
            sum = 0 + num_nines(y[:-1])

    return sum

### CHECKING THE FUNCTION! ###
print(num_nines(3))
print(num_nines(7))
print(num_nines(9))
print(num_nines(99999))
print(num_nines(345678))
print(num_nines(397896599))
