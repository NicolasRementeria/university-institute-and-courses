class Books:
    def __init__(self, pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages + other.pages
    def __mul__(self, other):
        return self.pages * other.pages
    def __gt__(self, other):
        return self.pages > other.pages

b1 = Books(pages=100)
b2 = Books(pages=150)

print(b1 + b2) 
print(b1 * b2) 

# Output:
# 250
# 15000

print(b1 > b2) # 100 > 150
# Output:
# False