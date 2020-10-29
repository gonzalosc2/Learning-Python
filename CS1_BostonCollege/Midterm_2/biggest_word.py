# author: Gonzalo Salazar
# assigment: Midterm #2
# name: biggest word

# description
'''
Create a function called biggest_word that receives a string as a parameter,
the function must return the biggest word (in terms of number of characters).
But if the parameter has more than 2 words with the same size, it has to return
the first instance (first appearance).

Example:

If I call the function with the parameter: today is a beautiful day

The function must return beautiful

If I call the function with the parameter: the day today is rainy

The function must return today. The words today and rainy, both have 5 characters
but today appeared first, so this is the word that have to be returned.
'''

# script
def biggest_word(string_value):

     size = []
     list = string_value.strip().split()
     for word in list:
         size.append(len(word))

     maximum = max(size)
     where = size.index(maximum)

     return str(list[where])

# checking
string_value = 'today is a beautiful day'
string_value2 = 'the day today is rainy'
print(biggest_word(string_value))
print(biggest_word(string_value2))
