# class: car
# methods (actions): refuel() getFuel() setSpeed() getSpeed() drive()
# attributes (variables): fuel maxspeed

# Class name first letter as CAPITAL
class Student:
    #attributes with default values
    # The __init__ function is called a constructor, or 
    # initializer, and is automatically called when you 
    # create a new instance of a class 
    # __init__ method is initialized automatically
    # A constructor is a special type of method (function)
    # Is used to  initialize the instance members of the class
    # __init__ is a constructor method
    def __init__(self):
        self.name = "Nicolas"
        self.age = 31
        self.marks = 95
        print("__init__ is called!")
    #methods
    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)

# self is a variable that refers to current class instance

# To create a Student, needs to create an Object of Student class

student1 = Student()

print(student1.name)
print(student1.age)
print(student1.marks)
# Nicolas
# 31
# 95

student1.talk()

# Name - Martin
# Age - 31
# Marks - 95

# Change the object's name attribute
student1.name = "Martin"
print(student1.name)
# Martin

student2 = Student()
print(student2.name)
# Nicolas

# print memory positions:
print(id(student1))
print(id(student2))