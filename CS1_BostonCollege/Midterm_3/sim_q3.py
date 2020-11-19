# author: Gonzalo Salazar
# assigment: Midterm #3
# description
'''
PART A

Read the file and create a dictionary where the name of the restaurant is the key.
Clients name, rating and value that this client spent in the restaurant is the list
that you will store as values. If a restaurant was rated by more than one client,
this restaurant will have more than one list of values inside (list of lists)

Example:

{'Sushi Love': [['Bradley Atkinson ', '15', '22.75']],
'Another Broken Egg Cafe': [['Gini Carlson ', '11', '8.64']],
'Parizade': [['Ming Lao Zhang ', '12', '24.18']],
'Nana Tacos': [['Emily Sue Lynn Moon ', '18', '7.76']],
'The Little Dipper': [['Bala Yavatkar ', '12', '41.93']],
'Pompieri Pizza': [['Gini Carlson ', '14', '18.65']],
'Qshack': [['Bala Yavatkar ', '11', '12.76']]}

PART B

Someone wants to know the average rating of the restaurants, print a list of
restaurants and the average rate of them. You may assume that you have the
dictionary of the Question 2 A if needed. If you are able to do it your answer
should be (not necessarily in this order):

Sushi Love 15.0
Another Broken Egg Cafe 11.0 Parizade 12.0
Nana Tacos 18.0
The Little Dipper 12.0 Pompieri Pizza 14.0
Qshack 11.0

'''

# script
import os

os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/CS1_BostonCollege/Midterm_3')

### PART A
with open('sample.txt', mode = 'r') as f:

    db = []
    for line in f:
        db.append(line.strip().split(':'))

    db2 = []
    for list in db:
        my_list = []
        for value in list:
            my_list.extend(value.split('$'))

        db2.append(my_list)

    db = []
    for list in db2:
        db.append([list[0][:-3],int(list[0][-2:]),list[1],float(list[2])])

    restaurant = set()
    for list in db:
        restaurant.add(list[2])

    rest_dict = {}
    for rest in restaurant:
        people_rest = []
        for person in db:
            if person[2] == rest:
                people_rest.append(person[:2]+[person[-1]])
        rest_dict[rest] = people_rest

print(rest_dict)

### PART B
for key in rest_dict:
    sum = 0
    people = 0
    for person in rest_dict[key]:
        sum += person[1]
        people += 1
    print(key, ' rating is:  ', str(sum/people))
