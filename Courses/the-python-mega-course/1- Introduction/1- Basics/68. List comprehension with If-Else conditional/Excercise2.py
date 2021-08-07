# Convert and Sum Up (E)

# Define a function that takes as parameter a list that contains decimal numbers as strings and returns the sum of those numbers.

def myFunc(lst):
    result = [float(item) for item in lst]
    return sum(result)