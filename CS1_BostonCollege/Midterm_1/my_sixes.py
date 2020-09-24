# author: Gonzalo Salazar
# assigment: Midterm 1
# type: python function
# description: function called my_sixes
#   INPUTS: a numeric value
#   OUTPUTS: sum of the numbers from 1 to num divisible by 6.
#            The numbers cannot be divisible by 5 and 6 together, as well.

def my_sixes(num):
    result = 0
    i = 0

    while i <= num:
        i += 1
        if i % 6 == 0 and i % 5 == 0:
            pass
        elif i % 6 == 0:
            result += i
        else:
            pass

    return result

my_sixes(16)
