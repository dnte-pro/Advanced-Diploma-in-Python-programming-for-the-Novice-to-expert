class Car:
    car_count =0
    def __init__(self, model):
        self.__model = model 
        Car.car_count += 1

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model

    @staticmethod
    def peep():
        print("PEEP!")

    @classmethod
    def countcars(car_class):
        print('We have :', car_class.car_count, 'cars')



car1 = Car("BMW")
print(car1.model)   
car1.model = "Audi"
print(car1.model)
Car.peep()
print(Car.car_count)