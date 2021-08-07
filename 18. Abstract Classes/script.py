class Shape():
    def area(self):
        pass
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

shape_obj = Shape()
square_obj = Square(side=10)

# Here we can create both objects, although Shape does not have a Constructor

# What if we don't want to allow the user to create object of my Parent class?

