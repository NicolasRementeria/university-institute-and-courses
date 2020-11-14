from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side

shape_obj = Shape()
square_obj = Square(side=10)

# Output:
# TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# To fix this issue, the methods inside Shape class has to be also defined over Square class

# Follow it into script3.py