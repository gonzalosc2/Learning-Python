"""
Created on Tue Aug 27 17:01:29 2019

@author: gsalazar
"""

h = input('nº de hombres?')

m = input('nº de mujeres?')

p = 100.0*int(h)/(int(h)+int(m))

print("%hombres=", round(p, 1))

print("%mujeres=", round(100-p, 1))
