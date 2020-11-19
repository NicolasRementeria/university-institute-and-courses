# Only Numbers (E)

# Define a function that takes as a parameter a list that contains both integers and strings and returns the list containing only the integers.

def myFunc(lst):
    result = [item for item in lst if isinstance(item, int)]
    return result