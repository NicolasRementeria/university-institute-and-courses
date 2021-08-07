# Zeros instead (E)

# Define a function that takes as parameter a list that contains both numbers and strings and returns the same list but with zeros instead of strings

def myFunc(lst):
    result = [0 if isinstance(item, str) else item for item in lst]
    return result