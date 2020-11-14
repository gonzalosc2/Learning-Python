# author: Gonzalo Salazar
# assigment: Homework #6
# name: heroes
# description: main .py file a function that opens a file and returns a dictionary
#              with alignments and heroes belonging to those alignments.

#recall: to set working directory
#cd ..
#cd Learning-Python/CS1_BostonCollege/HW6_CS1

### FUNCTION DEFINITION ###
def heroes():
    "Opens a tabulated data file and returns a dictionary"
    "   INPUT: N/A"
    "   OUTPUT: dictionary (keys: alignments, values: list of lists with heroes)"

    with open('Marvel.csv', mode = 'r') as f:

        # Transforming info in a list of lists
        db = []
        for list in f:
            db.append(list.strip().split(','))

    # Saving the names of each alignment
    alignment = set()
    for heroe in db:
        alignment.add(heroe[2])

    heroes_by_alignment_dict = {}
    for align in alignment:
        align_heroes = []
        for heroe in db:
            if heroe[2] == align:
                align_heroes.append(heroe[:2]+heroe[3:])
        heroes_by_alignment_dict['{}'.format(align)] = align_heroes

    return heroes_by_alignment_dict

### CHECKING THE FUNCTION! ###
print(heroes())
