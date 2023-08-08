class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def info(self):
        pass


class Car(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)

    def info(self):
        print(f'Name of the car is: {self.name}\nName of the model is: {self.model}\nRelease year is: {self.year}')


class Bike(Vehicle):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)

    def info(self):
        print(f'Name of the Bike is: {self.name}\nName of the model is: {self.model}\nRelease year is: {self.year}')


c = Car('Audi', 'S-Class', 2014)
c.info()