# When you create a file object, a file object is created in the RAM, and it's going to remain there until the execution of your program ends.

# A good practice is to close the file to save RAM, when you finished to process the file.

myfile = open("text.txt")
content = myfile.read()
myfile.close()

print(content)

