temps = [220, 250, 340, -9999, 230]

new_temps = [temp / 10 for temp in temps if temp != -9999]

print(new_temps)

# Output:
# [22.0, 25.0, 34.0, 23.0]