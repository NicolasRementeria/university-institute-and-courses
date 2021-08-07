class Student:
    def __init__(self):
        print("1st Init method!")
    def __init__(self):
        print("2nd Init method!")
    def display(self):
        print("Hi,")

s1 = Student()
s1.display()

# Output:
# 2nd Init method!
# Hi,

# Although all constructors are valid, only the last one will be in use

class Student2:
    def __init__(self):
        print("1st Init method!")
    def __init__(self, n):
        self.name = n
        print("2nd Init method!", self.name)
    def display(self):
        print("Hi,", self.name)

s1 = Student2("Nico")
s1.display()

# Output:
# 2nd Init method! Nico
# Hi, Nico

# Changing self for other keyword works as long you are consistent on its use
# Over vsCode can fail due to pyLint extension

#class Student2:
#    def __init__(anotherSelf):
#        print("1st Init method!")
#    def __init__(anotherSelf, n):
#        anotherSelf.name = n
#        print("2nd Init method!", anotherSelf.name)
#    def display(anotherSelf):
#        print("Hi,", anotherSelf.name)

s1 = Student2("Nico")
s1.display()