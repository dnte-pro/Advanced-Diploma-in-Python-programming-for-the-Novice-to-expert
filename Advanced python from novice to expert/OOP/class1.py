class Car:
    def __init__(self, color):
        self._color = color  # private attribute
    def setcolor(self, color):
        self._color = color
    def getcolor(self):
        return self._color
    
car1 = Car("blue")
print(car1.getcolor())
car1.setcolor("red")
print(car1.getcolor())

# using property decorator
class Car:
    def __init__(self, color):
        self.__color = color
    def setcolor(self, color):
        self.__color = color
    def getcolor(self):
        return self.__color
    color = property(getcolor, setcolor)
car1 = Car("green")
car1.color = "black"
print(car1.color)