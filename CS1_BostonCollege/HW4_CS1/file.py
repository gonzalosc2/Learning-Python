# author: Gonzalo Salazar
# assigment: Homework #4
# name:
# description: main .py file with three functions

### MODULES ###
import random as rd

### GLOBAL VARIABLES ###
nucleotides = ('A','T','C','G')
rest_sites = ('ACCGGT','GGCGCGCC','GGATCC','CCTGCAGG')

### FUNCTIONS DEFINITION ###

def gen_DNA(size):
    "Generates DNA"

    return ''.join(rd.choices(nucleotides, k=size))

def not_unique(DNA_barcodes):
    "Checks whether the DNA barcode is unique or not"

    if DNA_barcodes[-1] in DNA_barcodes[:-1]:
        return True
    else:
        return False

def not_GC_content(DNA_barcodes):
    "Checks whether the guanine-cytosine content of a DNA barcode is between"
    "40% and 60% (both extremes included) or not"

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

    for site in rest_sites:
        if site in DNA_barcodes[-1]:
            return True
        else:
            pass

    return False

def is_hamming_dist_less_3(DNA_barcodes):
    "Checks whether the Hamming distance is less than three or not"

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

    while True:
        try:
            size = int(input('What should be the length of each DNA barcode?'))
            break

        except ValueError:
            print('Size introduced is not valid. Please enter interger values.')

    while True:
        try:
            sequences = int(input('How many sequences do you need?'))
            break

        except ValueError:
            print('Number of sequences introduced is not valid. Please enter interger values.')

    return size,sequences

### INITIALIZING THE CODE! ###
def main():
    "Runs the whole code"

    # Asking for size of DNA barcode and number of barcodes required
    size, sequences = input_validation()

    # Creating a list of unique DNA barcodes which satysfy four criteria
    return multi_DNA(size, sequences)

main()
