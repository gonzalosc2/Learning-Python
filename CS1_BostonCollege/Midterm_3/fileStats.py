# author: Gonzalo Salazar
# assigment: Midterm #3

# description
'''
Write a function named fileStats. The function fileStats takes two string
parameters: inFile, the name of an input file and outFile, the name of an output
file.

The function fileStats should read and analyze the contents of the input file
and write the statistics it compiles to the output file. The statistics you
should compute about the input file are:

the number of characters;
the number of words;
the number of lines;
the number of digits;
the number of punctuation marks
Each statistic should be written to a separate line of the output file.
(Hint: the string class contains constants named punctuation and digits.)
'''

# script
#import os
import string

#os.getcwd()
#os.chdir('/Users/gsalazar/Desktop')

#def fileStats(inFile,outFile):
def fileStats(inFile,outFile):

    # Opening file and calculating number of lines, characters and words
    with open(inFile, mode = 'r') as inF:

        text = []
        lines_count = 0
        char_count = 0
        for line in inF:
            char_count += len(line)
            text.extend(line.strip().split())
            lines_count += 1

        char_count += lines_count
        words_count = len(text)
        text = ' '.join(text)

    # Calculating number of punctuations and digits
    punc_count = 0
    dig_count = 0
    for char in text:
        if char in string.punctuation:
            punc_count += 1
        elif char in string.digits:
            dig_count += 1

    # Saving the info into a file
    with open(outFile, mode = 'w') as outF:
        outF.write('Characters: '  + str(char_count) + '\n')
        outF.write('Words: '       + str(words_count) + '\n')
        outF.write('Lines: '       + str(lines_count) + '\n')
        outF.write('Digits: '      + str(dig_count) + '\n')
        outF.write('Punctuation: ' + str(punc_count))

# checking
fileStats('example_fileStats.txt','output.txt')
