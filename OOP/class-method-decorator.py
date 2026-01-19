class Car:
    cars_count = 0 
    def __init__(self, model):
        self.__model = model

        Car.cars_count = Car.cars_count + 1
    @property
    def x(self):
        return self.__model
    
    @x.setter
    def x(self, model):
        self.__model = model

    @classmethod
    def countcars(car_class):
        print('We have :', car_class.cars_count, 'cars')

car1 = Car("BMW")

car1.countcars()
car1.x = "Audi"
print(car1.x)

car2 = Car("Kea")
car2.countcars()
print(car2.x)