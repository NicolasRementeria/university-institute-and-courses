result = None
x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y
except Exception as e:
    print("Error within our code", e)
    print(type(e))
else:
    print("Inside Else")
finally:
    print("Inside Finally")

print("---new line---")
print("Result = ", result)

# If no errors, you'll be inside Else and then Finally

# Output: 
# Number 1: 10
# Number 2: 10
# Inside Else
# Inside Finally
# ---new line---
# Result =  None

# If any error is catched, you'll skip Else but you'll end over Finally

# Output:
# Number 1: 50
# Number 2: 0
# Error within our code division by zero
 #<class 'ZeroDivisionError'>
# Inside Finally
# ---new line---
# Result =  None

