# author: Gonzalo Salazar
# assigment: Homework #2
# description: contains three functions
#   First function:
#       Input: temperature value in degrees Centigrade
#       Output: temperature value in degrees Fahrenheit
#   Second function:
#       Input: temperature value in degrees Fahrenheit
#       Output: temperature value in degrees Centigrade
#   Third function:
#       Input: temperature value in degrees Fahrenheit and wind speed in mph
#       Output: wind chill factor for those parameters

#Converts a Centigrade temperature to a Fahrenheit temperature
def centigrade_to_fahrenheit(T_c):
    T_f = 9/5 * T_c + 32
    return T_f

#Converts a Fahrenheit temperature to a Centigrade temperature\
def fahrenheit_to_centigrade(T_f):
    T_c = 5/9 * (T_f - 32)
    return T_c

#Calculates a wind chill factor (the "old" one)
def wind_chill_factor(TEMPERATURE,WIND):
    wc = 0.0817 * (3.71 * WIND**0.5 + 5.81 - 0.25 * WIND) * (TEMPERATURE - 91.4) + 91.4
    return wc
