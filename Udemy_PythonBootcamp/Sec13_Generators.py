####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 13 - Generators
# other: N/A
####################################

# GENERATORS are functions that automatically suspend and resume their execution
# and stata around the last point of value generation. This helps to save memory.
# A good example is the range() function, which only stores the value from the
# last iteration. If we actually want the whole sequence of numbers we should
# cast it to a list with list(range(i,j)).

# Example: NO generator is used (w/o yielding)
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

for x in create_cubes(10):
    print(x)

# Example: generator is used (w yielding)
def create_cubes(n):
    for x in range(n):
        yield x**3   # this defines a generator

for x in create_cubes(10):
    print(x)

# similarly, as with range() function
create_cubes(10)  # not a function itself, instead a generator
list(create_cubes(10))

# Example 2
def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

for number in gen_fibon(10):
    print(number)

# NEXT FUNCTION: show what the previous "step" was and then returning the next
#                value given the later formula
def simple_gen():
    for x in range(3):
        yield x*2

# calling for the next thing. It caches the error and stops calling next
for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g))  # 0
print(next(g))  # 2
print(next(g))  # 4
print(next(g))  # StopIteration error: all he values have been yielded

# ITER FUNCTION: allows to automatically iterate through a normal object that
# you may not expect
s = 'hello'

for letter in s:
    print(letter)

# it does not iterate automatically, it only does it because we use a for loop
next(s)

s_iter = iter(s)  # turns the string into a generator
print(next(s_iter))
print(next(s_iter))
