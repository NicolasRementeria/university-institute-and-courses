# write First 90 (E):

# Create a first.txt file that contains the first 90 characters of bear.txt

with open("bear.txt") as bearFile:
    bearContent = bearFile.read()

with open("first.txt", mode="w") as firstFile:
    firstFile.write(bearContent[0:90])