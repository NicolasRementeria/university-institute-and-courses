import mymath
from import_folder import mymath2

# import alternative of a library outside this folder
# import import_folder.mymath2

# mymath is a custom test library
# mymath.py has to be on the same directory as this one

# mymath2 is a folder inside this folder, and from where we are importing mymath2

result = mymath.add(5, 5)
print(result)

# Output:
# 10

result = mymath.multiply(5, 5)
print(result)

# Output:
# 25

result = mymath2.add(5, 5)
print(result)

# Output:
# 10

result = mymath2.multiply(5, 5)
print(result)

# Output:
# 25

#result = import_folder.mymath2.add(5, 5)
#print(result)

# Output:
# 10

#result = mymath2.multiply(5, 5)
#print(result)

# Output:
# 25