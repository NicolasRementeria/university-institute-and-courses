from polygon import Polygon

class Triangle(Polygon):
    def area(self):
        return (self.getHeight() * self.getWidth()) * 1/2