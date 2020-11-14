# author: Gonzalo Salazar
# assigment: Homework #6
# name: missing_digits
# description: main .py file with a function that returns the number of missing
#              digits between the first and last digit of the value provided by
#              the user. The input can be both disordered or ordered.

### FUNCTION DEFINITION ###
def missing_digits(x):
    "Calculates the number of missing digits between the first and last digit"
    "from the input value"
    "   INPUT: interger"
    "   OUTPUT: interger"

    x = sorted(str(x))

    # Base case
    if len(x) == 1:
        sum = 0

    # Recursive case
    else:
        if int(x[-1]) - int(x[-2]) > 1:
            # diff minus 1 to avoid including one of the extremes
            diff = int(x[-1]) - int(x[-2]) - 1
            sum = diff + missing_digits(int(''.join(x[:-1])))
        else:
            sum = 0 + missing_digits(int(''.join(x[:-1])))

    return sum

### CHECKING THE FUNCTION! ###
print(missing_digits(12289))
print(missing_digits(98221))
print(missing_digits(3459))
print(missing_digits(9543))
