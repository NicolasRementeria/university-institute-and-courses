# There are cases that inheritance does not cover your needs, but you still need to utilize parametersor methods from different clases that don't have relationship with your current class

# Composition:
# When two entities or classes are highly dependent on eachother. 
# We can use a relationship of "Part of"
# Both entities are dependent on eachother
# We also divide class as Content and Container 
# With this, we will build a Strong Relationship between them

# Here, Salary is part of Employee
# Content is part of Container

# Employee is my Container
# Salary is my Content

# Check that Employee Constructor calls the Salary Constructor, creating a Salary object inside Employee object

class Salary:
    def __init__(self, pay, reward):
        self.pay = pay
        self.reward = reward
    
    def annualSalary(self):
        return (self.pay*12) + self.reward

class Employee:
    def __init__(self, name, position, pay, reward):
        self.name = name
        self.position = position
        # The next line is the relationship of Container/Content
        self.finalSalary = Salary(pay, reward)
    def finalSalary_Method(self):
        return self.finalSalary.annualSalary()

emp = Employee(name="Nico", position="SRE", pay=500, reward=1500)

print(emp.finalSalary.annualSalary())

# Output:
# 7500

# (500 * 12) + 1500 = 7500 

print(emp.finalSalary_Method())

# Output:
# 7500

# As a side note, if the Container is destroyed, the Content will be no use, as both are dependent of eachother 