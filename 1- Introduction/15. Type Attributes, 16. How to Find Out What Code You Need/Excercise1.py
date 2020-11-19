# Calculate Maximum (E)

# Find out the appropriate function or method that returns the maximum value of a list and store it on max_value

student_grades = [9.1, 8.8, 7.5]
student_grades.sort(reverse=True)
max_value = student_grades[0]
print(max_value)

# Best way:
# max_value = max(student_grades)
# print(max_value)