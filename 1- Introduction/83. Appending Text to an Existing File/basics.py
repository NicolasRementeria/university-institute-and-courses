# help(open)

# Output:
# Modes:
# r = read
# w = create and write (overwrite the file with the new content if already exists)
# x = create and write (if the file already exists, wont overwrite it)
# a = append to the end of the file regardless of the current seek position

with open("text.txt", "x") as myfile:
    myfile.write("asd")

# Output: 
# FileExistsError: [Errno 17] File exists: 'text.txt'    

with open("text.txt", "x") as myfile:
    myfile.write("asd")

with open("text.txt", "a") as myfile:
    myfile.write("\nTHIS IS A TEST FILE")
    content = myfile.read()

# Output:
# Traceback (most recent call last):
#  File "<stdin>", line 3, in <module>
# io.UnsupportedOperation: not readable

with open("text.txt", "a+") as myfile:
    myfile.write("\nTHIS IS A TEST FILE")
    content = myfile.read()

print(content)

# Output:
# <NULL>

# The cursor is at the end of the file, so read() will only get the cursor at the end of the file, which has no strings there

# To fix this, you can move the cursor to the start of the file with "seek(0)"

with open("text.txt", "a+") as myfile:
    myfile.write("\nTHIS IS A TEST FILE")
    myfile.seek(0)
    content = myfile.read()

print(content)

# Output:
# asd
# asdads
# adsasdadas
# asddasadsasddsa
# THIS IS A TEST FILE