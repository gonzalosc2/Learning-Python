# author: Gonzalo Salazar
# assigment: Homework #4
# name: DNA sequences generator
# description: main .py file with a series of functions
#              Under certain restrictions such as a GC content in 40-60%,
#              unique sequence, no restricted enzymes, no restriction sites,
#              and hamming distance >= 3, this code generates a file with a
#              bunch of DNA sequences. The size of the sequence as well as the
#              number of sequences can be changed by the user

#recall: to set working directory
#cd ..
#cd Learning-Python/CS1_BostonCollege/HW4_CS1

### MODULES ###
import random as rd

### GLOBAL VARIABLES ###
nucleotides = ('A','T','C','G')
rest_sites = ('ACCGGT','GGCGCGCC','GGATCC','CCTGCAGG')

### FUNCTIONS DEFINITION ###
def gen_DNA(size):
    "Generates DNA"
    "   INPUT: the length of the sequence (interger)"
    "   OUTPUT: a DNA sequence"

    return ''.join(rd.choices(nucleotides, k=size))

def not_unique(DNA_barcodes):
    "Checks whether the DNA barcode is unique or not"
    "   INPUT: a list of barcodes"
    "   OUTPUT: a boolean"

    if DNA_barcodes[-1] in DNA_barcodes[:-1]:
        return True
    else:
        return False

def not_GC_content(DNA_barcodes):
    "Checks whether the guanine-cytosine content of a DNA barcode is between"
    "40% and 60% (both extremes included) or not"
    "   INPUT: a list of barcodes"
    "   OUTPUT: a boolean"

    num,denom = 0,0
    i = 0

    #Calculates the guanine-cytosine content of a DNA barcode
    while i < len(DNA_barcodes[-1]):
        if DNA_barcodes[-1][i] == "C" or DNA_barcodes[-1][i] == "G":
            num += 1
            denom += 1
        else:
            denom += 1

        i += 1

    GCcontent = num / denom
    if GCcontent < .4 or GCcontent > .6:
        return True
    else:
        return False

def is_rest_enzyme(DNA_barcodes):
    "Checks whether there are three identical nucleotides in a row or not"
    "   INPUT: a list of barcodes"
    "   OUTPUT: a boolean"

    i = 0
    while i+2 < len(DNA_barcodes[-1]):
        if DNA_barcodes[-1][i+2] == DNA_barcodes[-1][i+1] and \
            DNA_barcodes[-1][i+1] == DNA_barcodes[-1][i]:
            return True
        else:
            pass

        i += 1

    return False

def is_rest_site(DNA_barcodes):
    "Checks whether there is a restricion site or not"
    "   INPUT: a list of barcodes"
    "   OUTPUT: a boolean"

    for site in rest_sites:
        if site in DNA_barcodes[-1]:
            return True
        else:
            pass

    return False

def is_hamming_dist_less_3(DNA_barcodes):
    "Checks whether the Hamming distance is less than three or not"
    "   INPUT: a list of barcodes"
    "   OUTPUT: a boolean"

#    distance = []
    for barcode in DNA_barcodes[:-1]:
        i,dist = 0,0

        while i < len(barcode):
            if barcode[i] != DNA_barcodes[-1][i]:
                dist += 1
            else:
                pass

            i += 1

    #    distance.append(dist)
    #return distance

        if dist < 3:
             return True
        else:
             return False

def multi_DNA(size, sequences):
    "Generates multiple sequences of unique DNA according to the four criteria:"
    "1. GC content between 40% and 60%"
    "2. No three identical nucleotides in a row"
    "3. No restriction site is included"
    "4. Hamming distance greater than or equal to 3"
    "   INPUT: the length of the sequence (interger) and the number of required"
    "          sequences (interger)"
    "   OUTPUT: a list of DNA sequences"

    i=1
    j=0  # self checking
    DNA_barcodes = []

    while i <= sequences:
        DNA_barcodes.append(gen_DNA(size))

        if not_GC_content(DNA_barcodes) or is_rest_enzyme(DNA_barcodes) \
            or is_rest_site(DNA_barcodes) or not_unique(DNA_barcodes) \
            or is_hamming_dist_less_3(DNA_barcodes):
            DNA_barcodes[:]=DNA_barcodes[:-1]
            j += 1
            #print(j)  # self checking
            continue
        else:
            i += 1

    return DNA_barcodes

def input_validation():
    "Checks that the size and number of sequences values are intergers."
    "   INPUT: N/A"
    "   OUTPUT: the length of the sequence (interger) and the number of required"
    "           sequences (interger)"

    while True:
        try:
            size = int(input('What should be the length of each DNA barcode?'))
            break

        except ValueError:
            print('Size introduced is not valid. Please enter interger values.')

    while True:
        try:
            sequences = int(input('How many DNA sequences do you need?'))
            break

        except ValueError:
            print('Number of sequences introduced is not valid. Please enter interger values.')

    return size,sequences

def barcode_print(DNA_barcodes,size,sequences):
    "Generates the exact format that will be saved on a text file"
    "   INPUT: a list of DNA sequences, its length (interger) and their"
    "          specific size (integer)"
    "   OUTPUT: a file with name 'barcodes (#length seqs of size #size)'"

    name = 'barcodes (' + str(sequences) + 'seqs of size' + str(size) + ').txt'

    with open(name, mode = 'w') as DNA_file:
        for sequence in range(0, len(DNA_barcodes)):
            DNA_file.write('barcode ' + str(sequence+1) + ': ' + DNA_barcodes[sequence] + '\n')

### INITIALIZING THE CODE ###
def main():
    "Runs the whole code"
    "   INPUT: N/A"
    "   OUTPUT: a file with a bunch of DNA sequences"

    # Asks for size of DNA barcode and number of barcodes required
    size, sequences = input_validation()

    # Creates a list of unique DNA barcodes which satysfy four criteria
    DNA_barcodes = multi_DNA(size, sequences)

    # Transform the list into the required text format
    barcode_print(DNA_barcodes,size,sequences)

### RUNNING THE CODE! ###
main()
