# Read and Append (E):

# Append the text of bear1.txt to bear2.txt.

with open("bear1.txt") as bear_1_file:
    bear_1_content = bear_1_file.read()

with open("bear2.txt", "a") as bear_2_file:
    bear_2_file.write(bear_1_content)