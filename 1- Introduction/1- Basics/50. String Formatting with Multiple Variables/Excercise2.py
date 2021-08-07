# String Formatting and Uppercase (E)

# Implement a function that gets a person's name as a parameter and returns a greeting like "Hi <name>".
# The person's name first letter should always be uppercase.

def myfunc(name):
    return "Hi %s" % name.title()