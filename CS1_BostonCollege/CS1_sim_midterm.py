####################################
import random as rd

def comp_x_comp():
    turn = 1

    while True:
        numA = rd.randint(1,6)
        numB = rd.randint(1,6)
        print('turn: ' + str(turn) + ' compA play: ' + \
            str(numA) + ' compB play: ' +  str(numB))
        if numA > numB:
            return print('Comp A won \nIt took compA, ' + str(turn) + ' turn to win')
        elif numA == numB:
            return print('tied')
        else:
            turn += 1
            False

comp_x_comp()

####################################
def pass_course(*args):

    average = sum(args)/3

    if average >= 6:
        return "Passed course"
    else:
        return "Failed course"

pass_course(1.0, 9.9, 5.0)
pass_course(7.0, 9.9, 5.0)

####################################
def divisibles3(num):
    num_list=[]
    for i in range(1,num+1):
        if i % 3 == 0:
            num_list.append(i)
        else:
            pass

    return sum(num_list)

divisibles3(10)
divisibles3(15)
divisibles3(22)

####################################
n=1
while n < 25:
    if n % 5 == 0:
        print(n)
        break
    n = n+1

####################################
j=100
i = 0
while (j >=1):
    j = j//2
    print("yes")
    i = i+1
print(i)

def print_evens(n):

####################################
x=0

while 2*x <= n:
    print(x)
    x += 1
