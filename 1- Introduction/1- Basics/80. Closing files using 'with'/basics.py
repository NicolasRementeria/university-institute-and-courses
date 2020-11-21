# Closing files using "with" is not necessary, as close action is implicit

with open("text.txt") as myfile:
    content = myfile.read()

print(content)