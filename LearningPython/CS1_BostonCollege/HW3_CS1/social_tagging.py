# author: Gonzalo Salazar
# assigment: Homework #3
# name: Social Tagging
# description: main .py file with three functions
#   First function (labeled)
#       Input: a message
#       Output: a list of hashtags present on that message
#   Second function (tabulated):
#       Input: an local list of words obtained from the first function
#       Output: a list showing lists of unique words and the number of times
#               these appeared in the input list
#   Third function (main): calls first and second function as required by
#                          the user, otherwise the user has the option to
#                          exit the program

############################################################
### FUNCTION DEFINITION
############################################################

def labeled(saved_words):

    message = input('\nPlease type in the message you want to publish.' +
        'If you want to highlight a particular topic, please use hashtags (#): ')
    list_of_words = message.split()
    is_avoid = [',','.',';',':']

    for word in list_of_words:
    # Considers only words starting with hashtags (#)
        if word[0] == "#":
        # Checks if there is any symbol that should be avoided and gets rid of it
            if word[len(word)-1] in is_avoid:
                new_word = word[1:len(word)-1]
            else:
                new_word = word[1:len(word)]
            saved_words.append(new_word)
        else:
            pass

    return saved_words

def tabulated(hashtag_words):
    tab_list = []
# Considers just unique values to avoid duplicates
    for word in set(hashtag_words):
        count = 0
    # Counts how many of these unique values are in the entire list
        for list_word in hashtag_words:
            if word == list_word:
                count += 1
            else:
                pass
        tab_list.append([word,count])

    return tab_list

############################################################
### WHERE CODE INITIATES!
############################################################
def main():
    hashtag_words = []
    continue_values = ['continue','c']
    show_values = ['show','s']
    quit_values = ['quit','q']

    while True:
        answer = input('\nDo you want to start or continue writing a message in your social networks?' +
            '\n\nPlease type "Continue" (C) if you want to keep going,' +
            '\nPlease type "Show" (S) in case you want to check how many hasthags you have used so far,' +
            '\nothewise type "Quit" (Q): ')
        if answer.lower() in continue_values:
            hashtag_words = labeled(hashtag_words)
        elif answer.lower() in show_values:
            if hashtag_words == []:
                print('\nThere are no hashtags yet.')
            else:
                print('\n')
                print(tabulated(hashtag_words))
        elif answer.lower() in quit_values:
            return quit()

        else:
            print('\nThe value entered is not valid. Please try again.')

main()
