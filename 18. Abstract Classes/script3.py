
from abc import ABC, abstractmethod

class Shape2(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square2(Shape2):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def perimeter(self):
        return 4 * self.__side

square_obj2 = Square2(side=10)
print(square_obj2.area())

# Output:
# 100

# Now Shape objects cannot be created 
# And area/permieter methods from Shape has to be also over Square