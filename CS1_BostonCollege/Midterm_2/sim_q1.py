# author: Gonzalo Salazar
# assigment: Midterm #2
# name: best

# description
''''Write a function (best) that receives a list of lists as parameter.
This list of lists contains names and grades of students as in the example below.
Your function must print the name of the student with the best grade and its best grade.
You can assume that there are no repeated grades.

Example:

students=[["maria", 9.0], ["ben", 9.5], ["Caroline",9.6],["Tim", 9.1]]

best(students)   ->  The best student is:  Caroline with grade  9.6'''

# script
def best(lol):

     grade = []
     for list in lol:
         grade.append(list[1])

     maximum = max(grade)
     where = grade.index(maximum)

     return 'The best student is: ' + str(lol[where][0]) + ' with grade ' + str(lol[where][1])

# checking
students=[["maria", 9.0], ["ben", 9.5], ["Caroline",9.6],["Tim", 9.1]]
best(students)
