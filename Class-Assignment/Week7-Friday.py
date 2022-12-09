# If c = Car(2016, 'Toyota', 'Highlander')
# the statement print(c) prints out 'Toyota Highlander 2016'

class Car:
    def __init__(self, year, maker, model):
        self.__year = year
        self.__maker = maker
        self.__model = model
        self.__speed = 0

    def setYear(self, year):
        self.__year = year
    
    def getYear(self):
        return self.__year
    
    def setMaker(self, maker):
        self.__maker = maker

    def getMaker(self):
        return self.__maker
    
    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def __str__(self):
        return f"{self.getMaker()} {self.getModel()} {self.getYear()}"

#2
    def accelerate(self):
        self.__speed += 5

    def getSpeed(self):
        return self.__speed


c = Car(2016, 'Toyota', 'Highlander')
c.accelerate()
print(c.getSpeed())
