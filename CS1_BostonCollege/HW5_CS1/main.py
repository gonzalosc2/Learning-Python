# author: Gonzalo Salazar
# assigment: Homework #5
# name:
# description:
#
#
#

#recall: to set working directory
#cd ..
#cd Learning-Python/CS1_BostonCollege/HW5_CS1

### FUNCTIONS DEFINITION ###
def is_file(filename):
    "Checks if a file exists or not"
    "   INPUT: name of a file"
    "   OUTPUT: boolean"

    try:
        with open(filename, 'r') as f:
            return True
    except IOError:
        return False

def empl_data_processing(filename):
    "############"
    "   INPUT: name of a file"
    "   OUTPUT: list of lists with employment data by year"

    with open(filename, 'r') as f:
        f = list(f)[1:]
        data = []
        for item in f:
            yr_data = item.strip().split(',')
            each_year_info = [yr_data[0]]

            for value in yr_data[1:]:
                each_year_info.append(int(value))

            data.append(each_year_info)

    return data

def presi_data_processing(filename):
    "############"
    "   INPUT: name of a file"
    "   OUTPUT: list of lists with employment data by year"
    filename = 'presidents.txt'

        with open(filename, 'r') as f:
            f = list(f)
            data = []

            for item in f:
                presi_data = item.strip().split(', ')

                # for jr
                while len(presi_data) > 3:
                    pres_data = [presi_data[0] + ', ' + presi_data[1]]
                    pres_data.extend(presi_data[2:])
                    presi_data = pres_data

                # for min and max period
                pres_data = [presi_data[0]]
                pres_data.extend([presi_data[2],presi_data[1][:4],str(int(presi_data[1][-4:])-1)])

                data.append(pres_data)

        return data

def collecting_data(answer):
    "Opens a txt file with data and processes it"
    "   INPUT: N/A"
    "   OUTPUT: list of lists with useful information"

    while True:
        filename = input('Please enter the name of the file containing the relevant data. \
                    \nThe file should be on a comma-separated basis. Please provide the name of \
                    the file with its extension as well, e.g., name_of_the_file.txt')
        if is_file(filename) == False:
            print('Sorry, but there is no file named ' + filename + '. Please provide the correct name.')
            continue
        else:
            break

    if answer.upper() in ('G','GOVERNMENT','P','PRIVATE'):
        return empl_data_processing(filename)

    else:
        return presi_data_processing(filename)

def data_source():
    " ########"
    "   INPUT: N/A"
    "   OUTPUT: "

    while True:
        try:
            answer = input('Are you going to load information related to (P)rivate or \
                       (G)overnment employment, or related to (Pr)esidents elected in \
                       the U.S.? Please answer P, G, or Pr.')
            if answer.upper() in ('G','GOV','GOVERNMENT'):
                return collecting_data(answer)
            elif answer.upper() in ('P','PRIV','PRIVATE'):
                return collecting_data(answer)
            elif answer.upper() in ('PR','PRESIDENT','PRESIDENTS')
            else:
                raise ValueError('Invalid value.')

        except ValueError:
            print('The value provided is invalid, please answer P, G, or Pr.')

# ### INITIALIZING THE CODE ###
# def main():
#     "Runs the whole code"
#     "   INPUT: N/A"
#     "   OUTPUT: a file with a bunch of DNA sequences"
#
#
# ### RUNNING THE CODE! ###
# main()
