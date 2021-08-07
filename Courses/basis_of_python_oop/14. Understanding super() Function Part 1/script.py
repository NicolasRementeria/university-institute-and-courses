# super() function
# It's used to call our Parent class
# Also during multiple inheritance, multiple Parents

# In this case we will have inheritance without super()

class Parent:
    def __init__(self):
        print("Parent __init__")

class Child(Parent):
    def __init__(self):
        print("Child __init__")

child_obj = Child()

# Output: 
# Child __init__

# Will call to only Child, as the memory position is located into Child class

class Parent2:
    def __init__(self, name):
        print("Parent __init__", name)

class Child2(Parent2):
    def __init__(self):
        print("Child __init__")
        Parent2.__init__(self, "Nico")

child_obj2 = Child2()

# Output:
# Child __init__
# Parent __init__ Nico