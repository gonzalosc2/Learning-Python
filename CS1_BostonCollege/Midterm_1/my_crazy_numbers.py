# author: Gonzalo Salazar
# assigment: Midterm 1
# type: python function called my_crazy_numbers
# description:
#   INPUTS: 3 parameters, which are numbers
#   OUTPUTS: prints all numbers smaller that the first parameter, but not
#            divisible by the second parameter or the third parameter or by the
#            multiplication of both second and third parameter

def my_crazy_numbers(n1,n2,n3):
    i = 0
    num = n1
    while i <= n1:
        i += 1
        if num % n2 != 0 and num % n3 !=0 and num % (n2*n3) != 0:
            print(num)
            pass
        else:
            pass
            
        num -= 1

my_crazy_numbers(13,2,3)
