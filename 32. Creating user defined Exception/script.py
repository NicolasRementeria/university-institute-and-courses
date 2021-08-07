class TeaHotException(Exception):
    def __init__(self, argument):
        self.msg = argument

class TeaColdException(Exception):
    def __init__(self, argument):
        self.msg = argument

class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature
    
    def drinkTea(self):
        if self.__temperature > 85:
            raise TeaHotException("Tea too hot")
        elif self.__temperature < 65:
            raise TeaColdException("Tea too cold")
        else:
            print("Tea OK to drink")

cup = Tea(temperature=0)
cup.drinkTea()
