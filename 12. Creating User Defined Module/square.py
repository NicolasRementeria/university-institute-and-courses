from polygon import Polygon

class Square(Polygon):
    def area(self):
        return self.getHeight() * self.getWidth()