class Books:
    def __init__(self, pages):
        self.pages = pages

b1 = Books(pages=100)
b2 = Books(pages=150)

print(b1 + b2)

# Output:
# TypeError: unsupported operand type(s) for +: 'Books' and 'Books'

# Fails due to that the operator is not able to understand the objects to "sum"

# That's why its needed Operator Overloading

# The "+" symbol, internally is understood as "__add__"

# b1 + b2 == b1.__add__(b2)