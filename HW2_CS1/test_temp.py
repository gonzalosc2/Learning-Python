# author: Gonzalo Salazar
# assigment: Homework #2
# description: main .py file with two functions
#   First function:
#       Input: N/A
#       Output: prints a menu of alternatives
#   Second function:
#       Input: N/A
#       Output: depends on the option chosen by the user:
#          (i) it calculates Fahrenheit temperature from Centigrade temperature
#          (ii) it calculates Centigrade temperature from Fahrenheit temperature
#          (iii) it calculates the wind chill factor (based on the old formula)
#          (iv) it exits the application

# Importing temperature.py
import temperature

# Defining the menu of alternatives
def user_menu():
    print('What would you like to do?  \
        \na) Convert a Centigrade temperature to a Fahrenheit temperature \
        \nb) Convert a Fahrenheit temperature to a Centigrade temperature \
        \nc) Calculate a wind chill factor (the "old" one) \
        \nd) Exit the application' )

# Main function presenting the user menu, requesting input data, performing
# the selected operations and displaying the final resuls
def main():

    # Showing the menu of alternatives
    user_menu()

    # Validating the input data
    answer = ""  # placeholder variable

    while answer not in ['a','b','c','d']:
        answer = input('Please answer: a, b, c or, d:  ')

    # Converting a Centigrade temperature to a Fahrenheit temperature
    if answer == "a":
        temp_c = ""  # placeholder variable

        while type(temp_c) != float:
            try:
                temp_c = float(input('Please specify the temperature value in degrees Centrigrade:  '))
            except ValueError:
                print('That is an incorrect value, please use numerical values.')

        return print(round(temperature.centigrade_to_fahrenheit(temp_c)))

    # Converting a Fahrenheit temperature to a Centigrade temperature
    elif answer == "b":
        temp_f = ""  # placeholder variable

        while type(temp_f) != float:
            try:
                temp_f = float(input('Please specify the temperature value in degrees Fahrenheit:  '))
            except ValueError:
                print('That is an incorrect value, please use numerical values.')

        return print(round(temperature.fahrenheit_to_centigrade(temp_f)))

    # Calculating a wind chill factor (the "old" one)
    elif answer == "c":
        temp_f = ""  # placeholder variable
        wind = ""  # placeholder variable

        while type(temp_f) != float or type(wind) != float:
            try:
                temp_f = float(input('Please specify the temperature value in degrees Fahrenheit:  '))
                wind = float(input('Please specify the wind speed value in miles per hour:  '))
            except ValueError:
                print('That is an incorrect value; use numerical values only. \
                    \nPlease provide temperature and wind speed information again.')

        return print(round(temperature.wind_chill_factor(TEMPERATURE = temp_f,WIND = wind)))

    # Exiting  the application
    else:
        return exit()

# Calling the main function
main()

# Personal comments
#cd ..
#cd Python/HW2_CS1
