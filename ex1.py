"""
Created on Tue Aug 27 17:01:29 2019

@author: gsalazar
"""

print("nº de hombres?")

h=input()

print("nº de mujeres?")

m=input()

p=100.0*int(h)/(int(h)+int(m))

print("% hombres=",round(p,1))

print("% mujeres=",round(100-p,1))
     
