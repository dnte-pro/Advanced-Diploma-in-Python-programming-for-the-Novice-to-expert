class Car:
    def _init_(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    number_of_wheels = 4



# checking instances of the class
class Car:
    def _init_(self, color, year, model):
        self.color = color
        self.year = year
        self.model = model
    
car1 = Car("yellow", 2010, "BMW")
car2 = Car("yellow", 2010, "BMW")
print(car1 == car2)
# the output will be false since they are two different instances of the class Car. 
# even though they have the same attributes. This is because the self attribute points to different memory locations.

print(car1.color)


#Modifying attributes of a class

car1.model = 'Audi'
print(car1.model)

#Using getter and setter methods

class Vehicle:
    def __init__(self, color):
        self._color = color  # private attribute
    def setcolor(self, color):
        self._color = color
    def getcolor(self):
        return self._color
    
car1 = Vehicle("blue")
print(car1.getcolor())
car1.setcolor("red")
print(car1.getcolor())