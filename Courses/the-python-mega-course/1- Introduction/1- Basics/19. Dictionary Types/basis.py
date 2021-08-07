student_grades = {"Nico": 1.0, "Martin": 10.0, "Pepe": 7.0}

mysum = sum(student_grades.values())

# > student_grades.values()
# Output:
# dict_values([1.0, 10.0, 7.0])

length = len(student_grades)
mean = mysum / length
print(mean)