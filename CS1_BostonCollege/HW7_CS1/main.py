# author: Gonzalo Salazar
# assigment: Homework #7
# name: earthquake analysis around the world
# description: This code generates a set of insights about earthquakes such as
#              their intensity, their number by region, the strongest one, among
#              others. The user only needs to provide the name of the file
#              containing earthquake data.

#recall: to set working directory
#cd ..
#cd Learning-Python/CS1_BostonCollege/HW7_CS1

### LIBRARIES ###
import matplotlib.pyplot as plt
import numpy as np

### FUNCTIONS DEFINITION ###
def is_file(filename):
    "Checks if a file exists or not"
    "   INPUT: string(name of a file)"
    "   OUTPUT: boolean"

    try:
        with open(filename, 'r'):
            return True
    except IOError:
        return False

def data_processing(filename):
    "Transforms a txt file into a useful dictionary"
    "   INPUT: string(name of a file)"
    "   OUTPUT: a dictionary with regions and its related earthquakes data"

    with open(filename, 'r') as f:
        lol = []
        for item in f:
            value = item.strip().split(' ')
            eq_info = [float(value[0])] + value[1:6]

            reg = []
            for item in value[6:]:
                reg.append(item)

            region = ' '.join(reg)
            event = [region] + eq_info
            lol.append(event)

        data = {}
        for lt in lol:
            if lt[0] not in data:
                data[lt[0]] = [lt[1:]]
            else:
                data[lt[0]].append(lt[1:])

    return data

def collecting_data():
    "Opens a txt file with data and processes it"
    "   INPUT: N/A"
    "   OUTPUT: dictionary"

    while True:
        # Asks for the filename
        filename = input('Please enter the name of the file containing the ' +
                         'relevant data. \n The file should be on a ' +
                         'comma-separated basis. Please provide the name of ' +
                         'the file with its extension as well, ' +
                         'e.g., name_of_the_file.txt: ')
        if is_file(filename) == False:
            print('\nSorry, but there is no file named ' + filename + \
                  '. Please provide the correct name.')
            continue
        else:
            break

    return data_processing(filename)

def bar_chart(my_dict):
    "Generates a bar chart displaying the number of earthquakes by their intensity"
    "   INPUT: dictionary"
    "   OUTPUT: figure (bar chart)"

    intensity = {'micro':0,'light':0,'lower':0,'average':0,'big':0, \
                 'strong':0,'disaster':0}
    for key in my_dict:
        for lt in my_dict[key]:
            if lt[0] <= 3:
                intensity['micro'] += 1
            elif lt[0] > 3 and lt[0] <= 3.9:
                intensity['light'] += 1
            elif lt[0] > 3.9 and lt[0] <= 4.9:
                intensity['lower'] += 1
            elif lt[0] > 4.9 and lt[0] <= 5.9:
                intensity['average'] += 1
            elif lt[0] > 5.9 and lt[0] <= 6.9:
                intensity['big'] += 1
            elif lt[0] > 6.9 and lt[0] <= 7.9:
                intensity['strong'] += 1
            elif lt[0] > 7.9 :
                intensity['disaster'] += 1

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(intensity.keys(),intensity.values(),color = '#25a165')
    ax.set_title('Earthquakes Intensity')
    ax.set_ylabel('Amount of Earthquakes')
    return plt.show()

def line_chart(my_dict,key):
    "Generates a line chart displaying earthquakes intesity in a particular region"
    "   INPUT: dictionary"
    "   OUTPUT: figure (line chart)"

    intensity = []
    for lt in my_dict[key]:
        intensity.extend([lt[0]])

    x = np.linspace(0,len(intensity),len(intensity))
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.plot(x,intensity,color = '#cf5753',lw = 2,label = 'Intensity')
    ax.set_title('Earthquakes Intensity in ' + key)
    ax.set_ylabel('Richter scale')
    ax.legend()
    return plt.show()

def pie_chart(my_dict):
    "Generates a pie chart displaying locations that had more than 4 telluric events"
    "   INPUT: dictionary"
    "   OUTPUT: figure (pie chart)"

    region_count = {}
    for key in my_dict:
        count = 0
        for lt in my_dict[key]:
            count += 1
        if count >4:
            region_count[key] = count

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.pie(region_count.values(), autopct='%1.1f%%',
           labels = region_count.keys())
    ax.set_title('Ocurrences')
    return plt.show()

def strongest_earth_qk(my_dict):
    "Returns de location and magnitude of the strongest earthquake"
    "   INPUT: dictionary"
    "   OUTPUT: string"

    sgt_region = ['',0]
    for key in my_dict:
        for lt in my_dict[key]:
            if lt[0] > sgt_region[1]:
                sgt_region = [key,lt[0]]

    text = '\nThe strongest earthquake was in ' + sgt_region[0] + '.\n' + \
            str(sgt_region[1]) + ' (on the Richter scale) was its magnitude.'

    return print(text)

### INITIALIZING THE CODE ###
def main():
    "Runs the whole code"
    "   INPUT: N/A"
    "   OUTPUT: a bunch of figures about earthquakes around the world"

    # Asking for data file. Filtering, rearranging and cleansing database
    earth_qk_data = collecting_data()

    # Displaying insights obtained from database
    bar_chart(earth_qk_data)

    line_chart(earth_qk_data, key = 'HAWAII REGION, HAWAII')

    pie_chart(earth_qk_data)

    strongest_earth_qk(earth_qk_data)

### RUNNING THE CODE! ###
main()
