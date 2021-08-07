# Indefinite Number of Strings Processed (E)

# Define a function that takes an indefinite number of strings as parameters  and returns a list containing all the strings in UPPERCASE and sorted alphabetically

def myFunc(*strings):
    myList = list(strings)
    myList = [item.upper() for item in myList]
    myList.sort()
    return myList

# Alternative:

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)
