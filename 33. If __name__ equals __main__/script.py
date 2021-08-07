#  if __name__ == '__main__'

import mymath
import mymath2

print("--mymath1--")
print(mymath.add(50, 50))

# As mymath also prints something, the result of this script is:

# Output:
# 30
# 100

# But we want just the result of the script, not what mymath prints

# That's wy we created mymath2 library and will only print mymath2 print command just whenever you are executing the mymath2 script itself, not from outside.

print("--mymath2--")
print(mymath2.add(50, 50))

# Output
# 100

print(__name__)
# Output: 
# __main__