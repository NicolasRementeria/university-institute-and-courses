# Loop over integer colors (E)

# Loop over the colors items and print out the item in every loop only if the item is an integer.

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for c in colors:
    if isinstance(c, int):
        print(c)