# File Processing Inside Function (E):

# Define a function that gets a single string character and a filepath as parameters and returns the number of occurences of that character in the file

def myFunc(mychar, mypath):
    with open(file=mypath) as myfile:
        content = myfile.read()
    return content.count(mychar)