####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 09 - Modules and Packages
# other: N/A
####################################

# Download and install packages host in PyPi (be careful with firewalls)
# These are command lines
#pip install requests

#pip install colorama
# Colorama package changes the color of the command line

from colorama import init
init()

from colorama import Fore
print(Fore.RED + 'some red text')
print(Fore.GREEN + 'switch to green')

# GOOGLE: python package for ...
#pip install openpyxl
#import openpyxl

####################################
# MODULES: are just .py scripts that you call in another .py scripts.

#cd ..
#cd Python/Udemy_PythonBootcamp
from my_module import my_func

my_func()

####################################
# PACKAGES: are a collection of modules.
# IT IS IMPORTANT TO CREATE A FILE WITH NAME __init__.py WITHIN EACH DIRECTORY
# WE WANT TO BE A PACKAGE OR A SUBPACKAGE
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()
mysubscript.sub_report()

####################################
#__name__: is a built in variable that gets assigned a string depending on how
# you're running the actual script

#if __name__ == "__main__":
#   print(The script is running directly, it has NOT being imported)

# for an example, run "one.py" and "two.py" from the terminal.
