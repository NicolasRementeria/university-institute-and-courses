class Books:
    def __init__(self, pages):
        self.pages = pages
    # Here is the "+" overload
    # in this case, as the + operation only requires 2 parameters; b1 and b2, it's being abstracted as "self" and "other"
    def __add__(self, other):
        return self.pages + other.pages

b1 = Books(pages=100)
b2 = Books(pages=150)

print(b1 + b2) # b1.__add__(b2)

# Output:
# 250
