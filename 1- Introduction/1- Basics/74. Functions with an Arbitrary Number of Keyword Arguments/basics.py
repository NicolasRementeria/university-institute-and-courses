def mean(**kargs):
    return kargs

print(mean(a=1, b=10, c=100))

# Output:
# {'a': 1, 'b': 10, 'c': 100}

# Giving 2 asterisks, will return a dictionary with the name of the arguments as keys