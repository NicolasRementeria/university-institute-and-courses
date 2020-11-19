# Loop over Dictionary and Format

# Make the code print out the following output using a for loop:

# John Smith: +37682929928
# Mary Simpons: +423998200919

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))