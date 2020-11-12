# author: Gonzalo Salazar
# assigment: Homework #5
# name: employment analysis in the U.S.
# description: main .py file with a series of functions
#              This code generates a set of figures summarizing the employment
#              in the U.S. This is done taking into account political parties and
#              sector (government or private). Finally, some figures per president
#              are shown as well. The user only needs to provide the name of three
#              files associated with:
#                   (i) government employment data,
#                  (ii) private employment data, and
#                 (iii) presidential data.

#recall: to set working directory
#cd ..
#cd Learning-Python/CS1_BostonCollege/HW5_CS1

### LIBRARIES ###
import pandas

### FUNCTIONS DEFINITION ###
def is_file(filename):
    "Checks if a file exists or not"
    "   INPUT: string(name of a file)"
    "   OUTPUT: boolean"

    try:
        with open(filename, 'r') as f:
            return True
    except IOError:
        return False

def empl_data_processing(filename):
    "Transforms a txt file into a useful list"
    "   INPUT: string(name of a file)"
    "   OUTPUT: list of lists with employment data by year"

    with open(filename, 'r') as f:
        f = list(f)[1:]
        data = []
        for item in f:
            yr_data = item.strip().split(',')
            each_year_info = [int(yr_data[0])]

            for value in yr_data[1:]:
                each_year_info.append(int(value))

            data.append(each_year_info)

    return data

def presi_data_processing(filename):
    "Transforms a txt file into a useful list"
    "   INPUT: string (name of a file)"
    "   OUTPUT: list of lists with presidents data (period and party)"

    filename = 'presidents.txt'

    with open(filename, 'r') as f:
        f = list(f)
        data = []

        for item in f:
            presi_data = item.strip().split(', ')

            # Solves the issue with compound names of presidents, such as James Earl Carter, Jr
            while len(presi_data) > 3:
                pres_data = [presi_data[0] + ', ' + presi_data[1]]
                pres_data.extend(presi_data[2:])
                presi_data = pres_data

            # Separates the period by which each president was in charge in two diff values
            pres_data = [presi_data[0]]
            pres_data.extend([presi_data[2],int(presi_data[1][:4]),int(presi_data[1][-4:])-1])

            data.append(pres_data)

    return data

def collecting_data(answer):
    "Opens a txt file with data and processes it"
    "   INPUT: option stated by the user: (G)overnment, (P)rivate or (Pr)esident"
    "   OUTPUT: list of lists"

    while True:
        # Asks for the filename
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
    "Asks the user for the type of information she is planning to work with,"
    "to then call other functions in order to collect and transform the data"
    "   INPUT: N/A"
    "   OUTPUT: a data frame with specific data provided by the user or "
    "           an error if the option provided is not valid"

    while True:
        try:
            answer = input('Are you going to load information related to (P)rivate or \
                       (G)overnment employment, or related to (Pr)esidents elected in \
                       the U.S.? Please answer P, G, or Pr.')
            if answer.upper() in ('G','GOV','GOVERNMENT'):
                global gov
                gov = collecting_data(answer)
                break
            elif answer.upper() in ('P','PRIV','PRIVATE'):
                global priv
                priv = collecting_data(answer)
                break
            elif answer.upper() in ('PR','PRESIDENT','PRESIDENTS'):
                global pres
                pres = collecting_data(answer)
                break
            else:
                raise ValueError('Invalid value.')

        except ValueError:
            print('The value provided is invalid, please answer P, G, or Pr.')

def data_prompting():
    "Keeps asking for data files if these have not been loaded yet"
    "   INPUT: N/A"
    "   OUTPUT: N/A"

    while len(priv) == 0 or len(gov) == 0 or len(pres) == 0:
        data_source()

def data_merging(db):
    "Merges a list with presidential information"
    "   INPUT: list (database)"
    "   OUTPUT: updated list (modification of the original database)"

    for my_list in db:
        for president in pres:
            if my_list[0] in range(president[2],president[3]+1):
                my_list.extend(president[:2])

def bysort_empl(db):
    "Selects the column by which we want to sort, in this case by year"
    "   INPUT: list (database)"
    "   OUTPUT: value in specific column"

    return db[0]

def bysort_pres(db):
    "Selects the column by which we want to sort, in this case by the first year"
    "a president was in charge"
    "   INPUT: list (database)"
    "   OUTPUT: value in specific column"

    return db[-2]

def data_sorting(db):
    "Sorts a list depending on criteria"
    "   INPUT: list (database)"
    "   OUTPUT: sorted list"

    if db in (gov,priv):
        db.sort(key = bysort_empl)

    elif db in pres:
        db.sort(key = bysort_pres)

def empl_per_month(party,source):
    "Calculates the employment per month of a particular party given its source"
    "   INPUT: string [party] and list [source: government or private)]"
    "   OUTPUT: float"

    total_exp_list = []
    for my_list in source:
        if my_list[14].upper() in party:
            total_exp_list.append(sum(my_list[1:13])/len(my_list[1:13]))

    return sum(total_exp_list)/len(total_exp_list)

def empl_first_last_diff(source):
    "Calculates the difference in employment between the first and last month"
    "of a president in charge"
    "   INPUT: list [source: government or private)]"
    "   OUTPUT: list (with information about each president and the diff in employment)"

    empl_by_pres = []
    for my_list in source:
        for pres_period in pres:
            # First month for each president
            if pres_period[2] == my_list[0]:
                president_info = [my_list[-2],my_list[1]]

            # Last month for each president
            elif pres_period[3] == my_list[0]:
                #lm_empl.append([my_list[-2],my_list[-3]])
                president_info.append(my_list[-3])

        if len(president_info) == 3:
            empl_by_pres.append(president_info)

    # Adds the absolute difference and percentage difference for each president
    for my_list_pres in empl_by_pres:
        diff = my_list_pres[2]-my_list_pres[1]
        perc = diff / my_list_pres[1]
        my_list_pres.extend(['{:,}'.format(diff), '{:6.2%}'.format(perc)])

    return empl_by_pres

def data_formating(db):
    "Adds commas to units in thousands"
    "   INPUT: list"
    "   OUTPUT: modified list (with commas)"

    for i in (1,2):
        for item in db:
            item[i]='{:,}'.format(item[i])

def data_wrangling():
    "Encompasses the data processing step"
    "   INPUT: N/A"
    "   OUTPUT: lists with information about employment per month by party and"
    "           difference between first and last month employment per president"

    for db in (priv,gov):
        # Merging employment data with presidential information
        data_merging(db)

        # Sorting by year each database
        data_sorting(db)

    # Average monthly employment for each political party by source
    # for source in (gov,priv):
    #     for party in ('DEMOCRAT','REPUBLICAN'):
    #         source_empl_per_month_by_party.append(empl_per_month(party,source))

    # For government summary
    for party in ('DEMOCRAT','REPUBLICAN'):
        gov_empl_per_month_by_party.append('{:,}'.format(int(empl_per_month(party,gov))))

    # For private summary
    for party in ('DEMOCRAT','REPUBLICAN'):
        priv_empl_per_month_by_party.append('{:,}'.format(int(empl_per_month(party,priv))))

    # Change in employment from the first and last month for each president
    # For government summary
    gov_empl_per_president.extend(empl_first_last_diff(gov))
    data_formating(gov_empl_per_president)

    # For private summary
    priv_empl_per_president.extend(empl_first_last_diff(priv))
    data_formating(priv_empl_per_president)

def data_display():
    "Displays data related to employment in the U.S. by different classifications"
    "   INPUT: N/A"
    "   OUTPUT: prints of different data frames"

    side_party = ['Democrat','Republican']
    header_usd = ['(in millions)']
    side_num = list(range(1,len(gov_empl_per_president)+1))
    headers_pres = ['President','First Month','Last Month','Diff','% Diff']

    print('-----------------------------------------------')
    print('Governent employment average per month')
    print(pandas.DataFrame(gov_empl_per_month_by_party,side_party,header_usd))
    print('\n')

    print('-----------------------------------------------')
    print('Private employment average per month')
    print(pandas.DataFrame(priv_empl_per_month_by_party,side_party,header_usd))
    print('\n')

    print('-----------------------------------------------')
    print('Government employment by president (in millions)')
    print(pandas.DataFrame(gov_empl_per_president,side_num,headers_pres))
    print('\n')

    print('-----------------------------------------------')
    print('Private employment by president (in millions)')
    print(pandas.DataFrame(priv_empl_per_president,side_num,headers_pres))
    print('\n')

### INITIALIZING THE CODE ###
def main():
    "Runs the whole code"
    "   INPUT: N/A"
    "   OUTPUT: a bunch of figures about employment in the U.S."

    ### GLOBAL LISTS ###
    global gov
    global priv
    global pres
    gov = []
    priv = []
    pres = []

    global gov_empl_per_month_by_party
    global priv_empl_per_month_by_party
    global gov_empl_per_president
    global priv_empl_per_president
    gov_empl_per_month_by_party = []
    priv_empl_per_month_by_party = []
    gov_empl_per_president = []
    priv_empl_per_president = []

    # Asking for data files
    data_prompting()

    # Filtering, rearranging and cleansing databases
    data_wrangling()

    # Displaying insights obtained from databases
    data_display()

### RUNNING THE CODE! ###
main()
