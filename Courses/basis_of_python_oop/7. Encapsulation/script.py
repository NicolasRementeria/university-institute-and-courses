class Speed:
    def __init__(self):
        self.speed = 1

s = Speed()
print(s.speed)

# Encapsulation is used to restrict access to methods and variables
# This can prevent the data from being modified by accident

# To prevent modification of methods and variables, private methods and variables has to be used

class Speed2:
    def __init__(self):
        self.speed = 1
        self.__new_speed = 80
        
s2 = Speed2()
print(s2.__new_speed)

# Output:
# AttributeError: 'Speed2' object has no attribute '__new_speed'

# This is due to that __new_speed is private

# Private members can only be accessed inside that Class

# But you can edit this private members, and if you do you'll be able to access those
class Speed3:
    def __init__(self):
        self.speed = 1
        self.__new_speed = 80

s3 = Speed3()
s3.__new_speed = 100
print(s3.__new_speed)

# Output:
# 100

# To overcome this unsecureness, we use getters and setters
# getters are functions we create to retreive data
# setters are functions we create to put data to this function


class Speed4:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 80
    def getNewSpeed(self):
        return self.__new_speed
    def setNewSpeed(self, newSpeed):
        self.__new_speed = newSpeed

s4 = Speed4()
print(s4.speed)
print(s4.getNewSpeed())   
s4.setNewSpeed(9999)
print(s4.getNewSpeed())   

# Output
# 10
# 80
# 9999 