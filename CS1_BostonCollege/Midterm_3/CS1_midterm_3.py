
####################################
def trackChars(aString):
    d = {}
    for char in aString:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d

ben = 'hello world'
print(len(trackChars(ben)))

####################################
def container(s1, s2):
    rtnVal = ''
    for i in range(len(s2)):
        sub = s2[:i]
        if sub not in s1:
            rtnVal += sub
    return rtnVal

type(container('hoof','hoot'))

####################################
magic = {1:'one', 0:[2,3,4,5]}
magic[0][1]

####################################
def testString(aString):
    aDict = {}
    for letter in aString:
        num = aString.count(letter)
        if num not in aDict:
            aDict[num] = letter
        else:
            return num
    return -1

print(testString('eager'))

####################################
def what_do_I_do(n):
    n=str(n)
    num = 0
    for each in n:
        num = num + each

print(what_do_I_do(76889))

####################################
print(set('cold day'))

####################################
x,y = (3,4)
x=x+y
print(x,y)

####################################
import os

os.getcwd()
os.chdir('/Users/gsalazar/Desktop')

def lookInto(inFile, outFile, searchString):
    inF = open(inFile, 'r')
    outF= open(outFile, 'w')
    for line in inF:
        instances = line.count(searchString)
        outF.write(str(instances))
    inF.close()
    outF.close()

lookInto('lewis.txt','out.txt','the')
