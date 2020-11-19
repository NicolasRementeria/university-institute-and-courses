name = input("Enter your Name: ")
surname = input("Enter your Surname: ")

message = "Hello, i'm %s %s" % (name, surname)

print(message)

# Output:

# Enter your Name: Nico
# Enter your Surname: Rementeria
# Hello, i'm Nico Rementeria

# The next line only works on Python 3.6 and further
message = f"Hello, i'm {name} {surname}"

print(message)

# Output:

# Hello, i'm Nico Rementeria