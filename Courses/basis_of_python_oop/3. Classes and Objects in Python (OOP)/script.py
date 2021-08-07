# class: car
# methods (actions): refuel() getFuel() setSpeed() getSpeed() drive()
# attributes (variables): fuel maxspeed

# Class name first letter as CAPITAL
class Student:
    #attributes with default values
    def __init__(self):
        self.name = "Nicolas"
        self.age = 31
        self.marks = 95
    #methods
    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)

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