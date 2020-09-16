"""
Created on Tue Aug 27 17:01:29 2019

@author: gsalazar
"""

print('What is the distance between point A and B (meters)?')

d = input()

print('How long does it take to reach point B, starting from point A (seconds)?')

t = input()

s = (float(d)/1000)/(float(t)/3600)

print('The required speed to travel from A to B in ' + str(t)+' seconds is ' + str(round(s,1)) + ' km/hr')
