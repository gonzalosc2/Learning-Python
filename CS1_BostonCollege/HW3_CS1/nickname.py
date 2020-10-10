# author: Gonzalo Salazar
# assigment: Homework #3
# name: Nickname
# description: main .py file with three functions
#   First function (nickname):
#       Input: a list of words
#       Output: a nickname given a couple of rules (no connectors, no
#               prepositions, no punctuation, no numbers)
#   Second function (main): calls the first function if required by the user.
#       Input: N/A
#       Output: a nickname

############################################################
### TUPLES THAT A NICKNAME SHOULD AVOID
############################################################

# Source: https://en.wikipedia.org/wiki/Pronoun
pronouns = ('I', 'me', 'my', 'mine', 'myself','we','us','our','ours', \
            'ourselves','you','your','yours','yourself','yourselves', \
            'he','him','his','himself','she','her','hers','herself', \
            'it','its','itself','they','them','their','theirs','themself', \
            'themselves','this','these','that','those','former','latter', \
            'who','whom','whose','what','which','that','one',"one's",'oneself', \
            'something','anything','nothing','someone','anyone','somebody', \
            'anybody','nobody')
# Souce: https://www.wallstreetenglish.com/blog/speak-fluent-english-thanks-to-conversational-connectors-the-complete-list/
# and https://www.fluentu.com/blog/english/english-connectors/
connectors = ('and','plus','furthermore','moreover','also','in','addition', \
              'as','well','when','while','soon','then','after','afterwards', \
              'next','firstly','secondly','finally','but','however','though', \
              'although','nevertheless','despite','whereas','while','long', \
              'that','provided','unless','otherwise','because','due','to', \
              'so','order','therefore','a','result','consequently','thus', \
              'for','example','instance','such','like','an','actually','fact', \
              'matter','of','most','importantly','especially','notably', \
              'particular','significance','similarly','way','same','manner', \
              'additionally','likewise','even','hand','other','spite','contrary', \
              'on','all','first','second','place','the','conclusion','summarize', \
              'sum','up')
prepositions = ('above','across','after','against','along','among','around', \
                'at','away','from','before','behind','below','beneath','beside', \
                'between','by','down','during','for','from','in','front','of', \
                'inside','into','near','next','to','off','on','onto','out', \
                'outside','over','through','till','toward','towards','under', \
                'underneath','until','up')
punctuation = ('.',',',':',';')
numbers = ('0','1','2','3','4','5','6','7','8','9')

############################################################
### FUNCTION DEFINITION
############################################################

def nickname(answer):
    name = []

    while True:
        try:
            #answer = input('\nProvide a sentence: ')
            list_words = answer.split()

        # Validates the input of the user, numbers are not allowed
            for word in list_words:
                for letter in word:
                    if (letter[0] in numbers) or (letter[0] == '-'):
                        raise ValueError('The value entered is not valid.')

        # Creates a nickname following the rules
            for word in list_words:
                if (word in connectors) or (word in pronouns) or \
                    (word in prepositions) or (len(word) <= 3) or \
                    (word[0] in punctuation):
                    pass
                else:
                    name.append(word[0].upper())

            return print(''.join(name))

        except ValueError:
            print('The value entered is not valid.' +
                ' Please, type in a valid sentence (numbers are not allowed)')
            break

############################################################
### WHERE CODE INITIATES!
############################################################

def main():
    exit_true = ['q','quit']

    while True:
        answer = input('\nEnter a sentence or quit. If you want to exit' +
            ' type "quit" (Q): ')

        if answer.lower() in exit_true:
            return quit()
        else:
            nickname(answer)

main()
