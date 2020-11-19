# author: Gonzalo Salazar
# assigment: Midterm #3
# description
'''
Write a function that takes as a parameter a list of list words, which you may
assume to all be in lower case (e.g., [[“today is a rainy day”],
[“today is a beautiful day”],...]) and returns a dictionary in which each key
is a word of the list, and the corresponding value is a the frequency of the
word. For instance, with the word list above, the dictionary returned by the
function is:

{'today': 2, 'is': 2, 'a': 2, 'rainy': 1, 'day': 2, 'beautiful': 1}
'''

# script
def count_words(lol):

    words = []
    for list in lol:
        words.extend(list[0].split())

    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

    return d

# checking
example_list = [['today is a rainy day'], ['today is a beautiful day']]
print(count_words(example_list))
