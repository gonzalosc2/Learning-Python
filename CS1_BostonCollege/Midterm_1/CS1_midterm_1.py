####################################
# author: Gonzalo Salazar
# course: Computer Science 1 at Boston College
# assigment: Midterm 1
# description: Sketch of notes used to answer the midterm
####################################

####################################
def test(x):
    i=1
    result=0
    while i<=x:
        if i%2 == 0:
            result += i
        i += 1

    return result

print(test(10))

####################################
y = 0
while y*2<20:
    if y%3 == 0:
        y = y+2
        continue
    y = y+1
print(y)

####################################
x=2
y=True
a=1

if a:
    x *= 3
    y += 1
    a = y
else:
    y=False
    x-=1
    a=y
print(x,y,a)

####################################
b = 0
while b<=10:
    x=0
    while x<=15:
        x=x+1
    b=b+1
print(b,x)
