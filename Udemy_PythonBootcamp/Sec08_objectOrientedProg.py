####################################
# author: Gonzalo Salazar
# course: 2020 Complete Python Bootcamps: From Zero to Hero in Python
# purpose: lecture notes
# description: Section 08 - Object Oriented Programing
# other: N/A
####################################

# OOP allows a programmer to create her own objects that have methods and attributes.
# Recall that after defining an object (i.e., string, list, dictionary, etc)
# I was able to call methods off them with the .method_name() syntax.
# In general, OOP allows us to create code that is repeatable and organized,
# specially for much larger scripts.

# OBJECT or CLASS: a user defined object. It is a blueprint that defines the
# nature of a future object. From classes we can construct an instance of the
# object. An instance is a specific object created from a particular class.

# class NameOfClass():
#   def __init__(self,param1,param2):
#       self.param1 = param1
#       self.param2 = param2
#
#   def some_method(self):
#       #perform some action
#       print(self.param1)

# "def" inside a class does not define a function, instead it defines a method.
# Using "self" again to let Python know tha this isn't just some functions it's
# a method that's connected to this class, and that's where we us the self word
# to connect these methods to the class

class Sample():
    # HERE WE HAVE TO SPECIFY THE ATTRIBUTES, IN THIS CASE WE DO NOT HAVE ANY
    pass

my_sample = Sample() # an instance of my class.

type(my_sample)

# Class: has attributes.
# Attributes: characteristic of an object.

####################################
class Dog():

    # INIT METHOD: called upon whenever we actually create an instace of the class.
    #              It always start off with the "self" keyword which basically
    #              connects this method to the instance of the class and it allows
    #              us to refer to itself and then we pass in any attributes that
    #              we want the user to define.
    def __init__(self, breed, name, spots):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        #self.my_attribute = breed # the same, it highlights the difference
                                   # between the input breed and the attribute
                                   # breed
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

help(Dog)
my_dog = Dog(breed='Huskie', name='Rambo', spots=False) # instance of a class

type(my_dog)
my_dog.name
my_dog.spots

####################################
# CLASS OBJECT ATTRIBUTES: attributes that are going to be the same for any instance
#                          of the class.

# METHODS: functions defined inside the body of the class they're used to perform
#          operations that sometimes utilize the actual attributes of the object
#          we created.

class Cat():

    # CLASS OBJECT ATTRIBUTE
    species = 'mammal'

    def __init__(self, breed, name):

        # ATTRIBUTES
        self.breed = breed
        self.name = name

    # OPERATIONS/ACTIONS ---> Methods
    def sound(self,number):  # adding "self" keyword connects this functon to the class
        print('MIAU! My name is {} and the number is {}'.format(self.name, number))
    def sound(self):
        print('MIAU! My name is {}'.format(self.name))

my_cat = Cat(breed='Persian', name='Amon')

my_cat.name
my_cat.sound(3)

####################################
class Circle():
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = self.pi * (radius ** 2)
        #self.area = Circle.pi * (radius ** 2) # also valid only if it's a CLASS OBJECT ATTRIBUTE

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle()
my_circle2 = Circle(4)
my_circle.get_circumference()
my_circle2.get_circumference()
my_circle2.area

####################################
# INHERITANCE: a way to form new classes using classes that have already been defined.
#              It allows us to reuse code and to reduce the complexity of a program.

# Base class
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

# Inherited class or derived class
class Dog(Animal):

    # NOT NECESSARILY NEEDED IT IF WE ARE INHERITING IT.
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    # overwritting previous methods is also possible when a class is inherited
    #def who_am_i(self):
    #   print('I am a dog!')

mydog = Dog()
mydog.eat() # Inherited in Dog class

####################################
# POLYMORPHISM: refers to the way in which different object classes can share
#               the same method name, and then those methods can be called from
#               the same place even though a variety of different objects
#               might be passed in.

class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'

niko = Dog('niko')
felix = Cat('felix')

print(niko.speak())
print(felix.speak())

# Example 1
for pet in [niko,felix]:
    print(type(pet))           # they're different type
    print(type(pet.speak()))   # both share the same method name

# Example 2
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

# Notice that in both cases we're able to pass in different objects and we obtain
# object specific results from the same mechanism that same method call.

####################################
# ABSTRACT CLASS: is one that neve expects to be instantiated. You never actually
#                 expect to create an instance of this class. Designed to serve
#                 as a BASE CLASS.

class Animal():

    def __init__(self,name):
        self.name = name

    def speak(self):
        # raise works as a warning in R, it shows an error.
        raise NotImplementedError('Subclass must be implemented. This is an abstract method')

#myanimal = Animal('fred')
#myanimal.speak()

class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'

class Cat(Animal):

    def speak(self):
        return self.name + ' says meow!'

print(fido.speak())
print(isis.speak())

####################################
# SPECIAL/MAGIC METHODS: enables us to actually use built in Python functions
#                        suc as length or print with my own user defined objects.

class BookNoSpec():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

class BookSpec():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        # provides the user with more info when "del" command is used
        print('A book object has been deleted.')

b = BookNoSpec('Python rocks', 'G', 200)
b2 = BookSpec('Python rocks', 'G', 200)

print(b) # it does not print what we want
len(b) # error
print(b2)
len(b2)
del b2
del b # deletes a variable
