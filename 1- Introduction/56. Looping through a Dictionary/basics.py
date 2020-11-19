student_grades = {"Nico": 10, "Martin": 5, "Javier": 8}

for grades in student_grades.items():
    print(grades)

# Output:
# ('Nico', 10)
# ('Martin', 5)
# ('Javier', 8)

for grades in student_grades.keys():
    print(grades)

# Output:
# Nico
# Martin
# Javier

for grades in student_grades.values():
    print(grades)

# Output:
# 10
# 5
# 8

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

# Output:
# John Smith has as phone number +37682929928
# Marry Simpons has as phone number +423998200919  