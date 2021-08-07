# Aggregation:
# Will be defining a relationship about "has a"

# Bank has an Employee
# Employee has a Salary
# Library has a book

# Instead of inheritance or composition, the Employee to be created will need that Salary object be created as well

# Salary object will be passed to Employee object as a parameter

# Both entities can survive individually

# Aggregation is a weak connection

class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward
    
    def annualSalary(self):
        return (self.pay*12) + self.reward

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.finalSalary = salary
    def finalSalary_Method(self):
        return self.finalSalary.annualSalary()


# Here we create Salary object
sal = Salary(pay=500, reward=1500)

# Here we pass Salary object to Employee
emp = Employee(name="Nico", position="SRE", salary=sal)

print(emp.finalSalary.annualSalary())

print(emp.finalSalary_Method())

# Output:
# 7500
# 7500