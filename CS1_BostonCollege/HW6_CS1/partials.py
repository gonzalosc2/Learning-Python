# author: Gonzalo Salazar
# assigment: Homework #6
# name: partials
# description: main .py file with a function that returns the maximum value
#              from all the possible combinations of a number up to a certain
#              threshold defined by the user. The number is also provided by
#              the user and assumed to be interger.

### LIBRARIES ###
from itertools import combinations

### FUNCTION DEFINITION ###
def partials(n,l):
    "Calculates the maximum value from all possible combinations of a number"
    "up to a certain threshold"
    "   INPUT: n = interger, l = interger (length)"
    "   OUTPUT: interger"

    n = list(str(n))

    # Base cases
    if l == 0:
        my_combs = 0

    # Recursive case
    else:

        # If subset is greater than the set, then consider the set instead
        if l > len(n):
            l = len(n)

        # Calculates all possible combinations of a certain length
        comb_tuples = list(combinations(n,l))
        comb_list = []

        # Creates a list from a tuple
        for tuple in comb_tuples:
            value_list = list(tuple)
            my_list = []

            for value in value_list:
                my_list.append(str(value))

            comb_list.append(int(''.join(my_list)))

        if max(comb_list) >= partials(int(''.join(n)),l-1):
            my_combs = max(comb_list)
        else:
            my_combs = partials(int(''.join(n)),l-1)

    return my_combs

### CHECKING THE FUNCTION! ###
print(partials(20125,3))
print(partials(20125,5))
print(partials(20125,6))
print(partials(12345,0))
print(partials(12345,1))
