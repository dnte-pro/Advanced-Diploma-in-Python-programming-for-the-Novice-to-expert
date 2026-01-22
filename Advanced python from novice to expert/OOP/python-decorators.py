def outer_fun():
    print("Outer function")

    def inner_fun():
        print("Inner function")
    inner_fun()

outer_fun()


# second trial 

def decorator_function(inner_function):
    def wrapper_function():
        print(" This is the first line")
        inner_function
        print(" This is the last line")
    return wrapper_function


@decorator_function
def magic_print():
    print(" This is MAGICAL !")

magic = magic_print()
print(magic)
#print(magic())




#Advanced python decorators

class Car:
    def __init__(self, model):
        self.__model = model
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model

car1 = Car("BMW")
print(car1.model)

car1.model = "Audi"
print(car1.model)