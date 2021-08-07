# Task:
# 1- Take input from user (name, age, marks)
# 2- Create a class with __init__ method and also create an action method display() to print attributes
# 3- Try to use Arguments and Parameters with different objects

class User:
    def __init__(self, name="DefaultName", age=0, marks=0):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)

class UserUpdated:
    #marks support multiple values after the 3rd parameter included
    def __init__(self, name, age, *marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)

class UserUpdated2:
    #marks support multiple values after the 3rd parameter included
    def __init__(self, name, age, **marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)

myName = input("Name: ")
myAge = int(input("Age: "))
myMarks = int(input("Marks: "))

print("-----")
user1 = User(myName, myAge, myMarks)
user1.display()

print("-----")
user2 = User("Test 2")
user2.display()

print("-----")
user3 = User(age=99, marks=99)
user3.display()

print("-----")
user4 = UserUpdated("Test 4", 22, 95,22,25,35)
user4.display()

print("-----")
user5 = UserUpdated2("Test 5", 22, science = 0, english = 1, maths = 2)
user5.display()

print("-----")
user6 = UserUpdated2("Test 6", 99, science = 8, english = 4, maths = 3)
user6.display()