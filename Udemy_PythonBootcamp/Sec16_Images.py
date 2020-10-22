####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 16 - Images
# other: N/A
####################################

#pip install pillow
# PILLOW LIBRARY
# It is a fork of the PIL (Python Imaging Library) with easy to use function calls

import os
from PIL import Image

os.getcwd()
os.chdir('/Users/gsalazar/Documents/C_Codes/Learning-Python/Udemy_PythonBootcamp/images')

# Opening images
mac = Image.open('example.jpg')
type(mac)
#mac.show()   # if running as a script, we should use this command
mac    # if we are running this on a Jupyter notebook
mac.size
mac.filename
mac.format
mac.format_description

# Cropping images
# the following command requires a 4-tuple. The first two values correspond to
# x and y. The other two are w(idth) and h(eight).
# By default, the x,y are the coordinates from where we start cropping, and then
# w,h the ones where we are going to end up cropping
mac.crop((0,0,100,100))

pencils = Image.open('pencils.jpg')
pencils.size

#top pencils
x = 0
y = 0
w = 1950/3
h = 1300/10

#bottom pencils
x2 = 0
y2 = 1100
w2 = 1950
h2 = 1300

pencils.crop((x,y,w,h))
pencils.crop((x2,y2,w2,h2))

mac.size
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257

computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))   # the following command requires a 2-tuple.
mac.resize((3000,500))  # the following command requires a 2-tuple.
mac.rotate(90)

# Color transparency
# RGBA - Red, Green, Blue, Alpha (it controls transparency)
red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

red.putalpha(0)
red  # it does not work for png. Instead use .show()
red.putalpha(255)
red
red.putalpha(100)
red
blue.putalpha(100)
#blue.show()

blue.paste(im=red,box=(0,0),mask=red)
#blue.show()
blue.save("purple.png")
