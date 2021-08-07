# Average Function (E)

# Define a function that takes an indefinite number of numbers as arguments and return their average.

def mean(*args):
    return sum(args) / len(args)