# Copy n-times (E):

# The existing content of data.txt looks like:
# 1.3, 1.5
# 2.3, 2.7

# Use Python to modify the content of data.txt so that its content looks like:

# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7

with open("data.txt", "a+") as data_file:
    data_file.seek(0)
    data_content = data_file.read()
    data_file.write(data_content)
    data_file.write(data_content)