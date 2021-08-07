from square import Square
from triangle import Triangle

s1 = Square()
s1.setValue(width=8, height=15)
s1.setColor(color="Blue")
print(s1.area())
print(s1.getColor())

t1 = Triangle()
t1.setValue(width=5, height=10)
t1.setColor("Green")
print(t1.area())
print(t1.getColor())
