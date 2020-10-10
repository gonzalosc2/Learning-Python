#one.py

def func():
    print('FUNC() in one.py')

print('TOP LEVEL IN ONE.py')

if __name__ == '__main__':
    print('ONE.py is being run directly')
else:
    print('ONE.PY has been imported!')
