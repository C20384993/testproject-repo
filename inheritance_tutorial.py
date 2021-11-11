# Tutorial Week 8: Module import, Revision on class, Inheritance, Encapsulation in Python
# B. Schoen-Phelan
# 09-11-2021

# a python file and imports and how they work together
# create one python file called car.py in there we write,
# see car.py for what's in there
# then we can write the following:
from car import Car

# notice how we have one less argument compared to the
# definition of the class. self does not need to be
# passed. Python does this automatically.
my_car = Car("Honda", "Civic", 2000)
print(my_car.make)
my_car.drive() # again, self does not need to be passed. It's handled automatically by Python.

# now that we have a blueprint of the car class, we can
# create as many cars as we would like. Let's create a second car
my_second_car = Car("Mercedes", "B Class", 2021, "red")
print(my_second_car.colour)
my_second_car.drive()

my_car.stop() # in the output, notice how what's "self" in the definition is replaced by this object's identifier

# basic inheritance example

class A:
  def __init__(self):
    print("I'm class A")

class B(A):
  pass

a = A()
b = B()
#
# usage of isinstance
print(isinstance(21, int))
print(isinstance(a,A))
print(isinstance(b,A))
#
# # compare to type
print(type(21))
print(type(a))
print(type(b))
print(type(b)==A, type(b)==B)

# example from W3 schools

class Person:
  def __init__(self, f_name, l_name):
    self._first_name = f_name
    self._last_name = l_name

  def print_name(self):
    print(self._first_name, self._last_name)

# Use the Person class to create an object, and then execute the print_name method:

bsp = Person("Bianca", "Phelan")
bsp.print_name()

class Student(Person):
  pass
#
# you have access to the methods and attributes
# of the parent class without having to
# program any of the functionality
x = Student("John", "Doe")
x.print_name()
# notice how we do not need an instance of Person
# in order to use the Student. The definition of
# Person was enough to be able to use it.

# now extend Student class with more functionality
class Student(Person):
  # init in Student overrides init from Person
  def __init__(self, s_id, f_name, l_name):
    self._student_id = s_id


x = Student(12345, "John", "Doe")
x.print_name() # causes an error if not defined in init

# now corrected student:
class Student(Person):
  # init in Student overrides init from Person
  # super() grabs the class one higher in the hierarchy
  # the parent class and initialises the fname and lname
  def __init__(self, s_id, f_name, l_name):
    super().__init__(f_name, l_name)
    self.student_id = s_id


x = Student(12345, "John", "Doe")
x.print_name()
print(x.student_id)


# let's have a look at the three types of variables
# Python is not very strict on this, apart from the
# double underscore variable
class A:
  def __init__(self):
    self.a_var = "hi"
    self._a_protected_var = "world"
    self.__a_private_var = "everyone"

class B(A):
  def __init__(self):
    super().__init__()
    self.b_var = "hello"


b = B()
print(b.a_var)
print(b.b_var)
print(b._a_protected_var)
print(b.__a_private_var) # causes an error, doesn't know this variable


#  another example
class A:
  def __init__(self):
    self.public_profession = "Lecturer"
    self._protected_name = "Bianca"
    self.__private_surname = "Phelan"

  @property
  def private_var(self):
    return self.__private_surname

  @private_var.setter
  def private_var(self, value):
    if type(value) == str:
      self.__private_surname = value
    else:
      raise Exception("Error, cannot set this value.")


bianca = A()
print(bianca.__private_surname) # this causes an error
#
try:
  bianca.private_var = "Schoen" # switch this out for a 3 or other non string values
except Exception as e:
  print("Tried setting non string", e)
finally:
  print("Stays a string")

print(bianca.private_var)

class B(A):
  pass
#
susan = B()
print(susan.public_profession)
print(susan._protected_name)
# print(susan.__private_surname) #causes an error
print(susan.private_var) # also available, like before
susan.private_var = "McKeever"
print(susan.private_var)


