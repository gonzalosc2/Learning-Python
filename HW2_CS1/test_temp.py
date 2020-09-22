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
    valid = False
    while not valid:
        answer = input('Please answer: a, b, c or, d')
        if answer == "a" or answer == "b" or answer == "c" or answer == "d":
            valid = True
        else:
            print('The answer is incorrect. Please enter a valid answer (a, b, c, or d)')

    # Converting a Centigrade temperature to a Fahrenheit temperature
    if answer == "a":
        valid = False
        while not valid:
            try:
                temp_c = float(input('Please specify the temperature value in degrees Centrigrade'))
                if type(temp_c) != float:
                    print('That is an incorrect value, please use numerical values')
                else:
                    valid = True
            except ValueError:
                print('That is an incorrect value, please use numerical values')
        return print(round(temperature.centigrade_to_fahrenheit(temp_c)))

    # Converting a Fahrenheit temperature to a Centigrade temperature
    elif answer == "b":
        valid = False
        while not valid:
            try:
                temp_f = float(input('Please specify the temperature value in degrees Fahrenheit'))
                if type(temp_f) != float:
                    print('That is an incorrect value, please use numerical values')
                else:
                    valid = True
            except ValueError:
                print('That is an incorrect value, please use numerical values')
        return print(round(temperature.fahrenheit_to_centigrade(temp_f)))

    # Calculating a wind chill factor (the "old" one)
    elif answer == "c":
        valid = False
        while not valid:
            try:
                wind = float(input('Please specify the wind speed value in miles per hour'))
                temp_f = float(input('Please specify the temperature value in degrees Fahrenheit'))
                if type(temp_f) != float or type(wind) != float:
                    print('That is an incorrect value, please use numerical values')
                else:
                    valid = True
            except ValueError:
                print('That is an incorrect value, please use numerical values')
        return print(round(temperature.wind_chill_factor(TEMPERATURE = temp_f,WIND = wind)))

    # Exiting  the application
    else:
        return exit()

# Calling the main function
main()

# Personal comments
#cd ..
#cd Python/HW2_CS1
