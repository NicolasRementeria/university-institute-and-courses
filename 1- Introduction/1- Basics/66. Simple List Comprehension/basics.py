temps = [220, 250, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# Output:
#[22.0, 25.0, 34.0, 23.0]

# Alternative:

temps = [220, 250, 340, 230]
new_temps = [temp / 10 for temp in temps]
print(new_temps)

# Output:
#[22.0, 25.0, 34.0, 23.0]