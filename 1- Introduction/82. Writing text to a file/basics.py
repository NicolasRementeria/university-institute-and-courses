# Using the parameter "w" over the Open function, will apply the Write mode. This can also create files, or overwrite it.

# Next command will create in the current folder an empty "banana.txt" file
# If a file with the same name exists, will overwrite it

with open("banana.txt", "w") as myfile:
    pass

# print(content)

with open("banana.txt", "w") as myfile:
    myfile.write("TEST\nTEST")
    myfile.write("TEST2\nTEST2")

# "banana.txt" Output:
# TEST
# TESTTEST2
# TEST2