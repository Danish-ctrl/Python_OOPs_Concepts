class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Car make is {self.make}, model is {self.model} and year is {self.year}")


c = Car('Audi', 'S-Class', 2018)
c.car_info()