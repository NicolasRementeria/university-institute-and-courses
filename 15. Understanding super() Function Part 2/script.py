# In this case we will utilize Super instead of calling Parent every time

# Note that over Child class we replaced in the constructor calling Parent, with super()

# Also, now that Child is utilizing Super, it's no need to call "self" into the functions

class Parent:
    def __init__(self, name):
        print("Parent __init__", name)

class Child(Parent):
    def __init__(self):
        print("Child __init__")
        super().__init__("Nico")

child_obj = Child()

# Output:
# Child __init__
# Parent __init__ Nico

# MRO:
# Method Resolution Order
# Its used to print the sequence of resolution of the class

print(Child.__mro__)

# Output:
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class 'object'>)

# Child methods will be called first
# Then Parent Class



