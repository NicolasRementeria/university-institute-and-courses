# Only Positive Numbers (E)

# Define a function that takes as parameter list of numbers and returns the list containing only the numbers greater than 0

def myFunc(lst):
    result = [item for item in lst if item > 0]
    return result