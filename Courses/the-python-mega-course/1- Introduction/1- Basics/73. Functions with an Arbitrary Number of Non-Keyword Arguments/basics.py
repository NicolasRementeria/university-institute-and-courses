# Putting an * as prefix over a parameter, will make that an indefinite quantity of parameters of that type can be input

def mean(*args):
    return sum(args) / len(args)

print(mean(1, 10, 99, 5, 3))

# Output:
# 23.6