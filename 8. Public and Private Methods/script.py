class Example:
    def __init__(self):
        self.x = 10
        self._y = 50
        self.__z = 100
    def publicMethod(self):
        print("Inside Public Method")
        print(self.x)
        print(self._y)
        print(self.__z)
    def __privateMethod(self):
        print("Inside Private Method")
        print(self.x)
        print(self._y)
        print(self.__z)

s = Example()

# Different levels of "privateness" over the Constructor:
# _single = weak "internal use" indicator

print(s.x)
# Output:
# 10
print(s._y)
# Output:
# 50
print(s.__z)
# Output:
# AttributeError: 'Example' object has no attribute '__z'

s.publicMethod()
# Output:
# 10
# 50
# 100
s.__privateMethod()
# AttributeError: 'Example' object has no attribute '__privateMethod'

class Example2:
    def __init__(self):
        self.x = 10
        self._y = 50
        self.__z = 100
    def publicMethod(self):
        print("Inside Public Method")
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__privateMethod()
    def __privateMethod(self):
        print("Inside Private Method")
        print(self.x)
        print(self._y)
        print(self.__z)

s = Example2()
s.publicMethod()

# Output:
# Inside Public Method
# 10
# 50
# 100
# Inside Private Method
# 10
# 50
# 100