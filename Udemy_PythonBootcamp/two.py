#two.py

#cd ..
#cd Python/Udemy_PythonBootcamp

import one

print('TOP LEVEL IN TWO.py')

one.func()

if __name__ == '__main__':
    #RUN THE SCRIPT!
    print('TWO.py is being run directly!')
else:
    print('Two.py has been imported')
