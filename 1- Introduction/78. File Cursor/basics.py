myfile = open("text.txt")
print(myfile.read())
print(myfile.read())

# Output:
# asd
# asdads
# adsasdadas
# asddasadsasddsa
# 

# Notice that the cursor reads from top to bottom and from left to right.
# With the first read() you'll reach the end of the file, and the cursor would be at top right 
# The next read(), as it's at the end of the file, returns none.

# To overcome this, it's a good practice to save the content of the file on a variable

myfile = open("text.txt")
content = myfile.read()

print(content)
print(content)
print(content)

# Output:
# >>> print(content)
# asd
# asdads
# adsasdadas
# asddasadsasddsa
# >>> print(content)
# asd
# asdads
# adsasdadas
# asddasadsasddsa
# >>> print(content)
# asd
# asdads
# adsasdadas
# asddasadsasddsa