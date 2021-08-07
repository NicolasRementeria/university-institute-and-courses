# Create different classes and understand inheritance

# As Polygon will never be created by itself, it's no use to create a init Constructor

class Polygon:
    __width = None
    __height = None
    def setValue(self, width, height):
        self.__width = width
        self.__height = height
    def getWidth(self):
        return self.__width
    def getHeight(self):
        return self.__height

class Square(Polygon):
    def area(self):
        return self.getHeight() * self.getWidth()

s1 = Square()
s1.setValue(width=10, height=20)
print(s1.area())

# Output:
# 200

class Triangle(Polygon):
    def area(self):
        return (self.getHeight() * self.getWidth()) * 1/2

t1 = Triangle()
t1.setValue(width=10, height=20)
print(t1.area())

# Output:
# 100.0