# Loop over dictionary and replace (E)

# Loop over the phone_numbers values and in each loop print out the phone number, but with "00" instead of "+"

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for phone in phone_numbers.values():
    print(phone.replace("+", "00"))