# Reading and Processing Text (E):

# Read the 'bear.txt' file and print out the first 90 chracters of its content

with open(file="bear.txt") as myfile:
    content = myfile.read()

print(content[0:90])