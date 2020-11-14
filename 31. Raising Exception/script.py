# With "raise" we can create our own exception

class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature
    
    def drinkTea(self):
        if self.__temperature > 85:
            #print("Hot to drink")
            raise ValueError("Tea too hot")
        elif self.__temperature < 65:
            raise ValueError("Tea too cold")
        else:
            print("Tea OK to drink")

cup = Tea(temperature=0)
cup.drinkTea()

# Output:
# ValueError: Tea too hot