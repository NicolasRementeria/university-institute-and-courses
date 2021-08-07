# Adding now a second parent

class Parent:
    def __init__(self, name):
        print("Parent __init__", name)

class Parent2:
    def __init__(self, name):
        print("Parent2 __init__", name)

class Child(Parent, Parent2):
    def __init__(self):
        print("Child __init__")
        super().__init__("Nico")

child_obj = Child()

print(Child.__mro__)

# Output:
# Child __init__
# Parent2 __init__ Nico
# (<class '__main__.Child'>, <class '__main__.Parent'>, <class '__main__.Parent2'>, <class 'object'>)    


# If we change the sequence of the inheritance over the Child class, like:
# class Child(Parent, Parent2):
#   ...
# And we check the __mro__, the result would be:
# Child __init__
# Parent __init__ Nico
# (<class '__main__.Child'>, <class '__main__.Parent2'>, <class '__main__.Parent'>, <class 'object'>)  


# super() built-in hsa two major use cases:
# 1- Allows us to avoid using base class explicitly
# 2- Working with multiple inheritance
