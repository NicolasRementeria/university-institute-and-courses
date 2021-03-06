from polygon import Polygon
from shape import Shape

class Square(Polygon, Shape):
    def area(self):
        return self.getHeight() * self.getWidth()