result = None
x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y
except ZeroDivisionError as e:
    print("Error within our code", e)
    print(type(e))
except TypeError as e:
    print("Error within our code", e)
    print(type(e))
except ValueError as e:
    print("Error within our code", e)
    print(type(e))
except Exception as e:
    print("Error within our code", e)
    print(type(e))

print("Result = ", result)