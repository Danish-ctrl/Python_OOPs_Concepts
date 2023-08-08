class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class Car(Vehicle):
    def __init__(self, name, model, mileage):
        super().__init__(name, model)
        self.mileage = mileage

    def car_details(self):
        print(f'Name of the car is: {self.name}\nName of the model is: {self.model}')

    def car_mileage(self):
        print(f'Mileage of the car is {self.mileage} per year')


class Bike(Vehicle):
    def __init__(self, name, model, mileage):
        super().__init__(name, model)
        self.mileage = mileage

    def bike_details(self):
        print(f'Name of the bike is: {self.name}\nName of the model is: {self.model}')

    def bike_mileage(self):
        print(f'Mileage of the bike is {self.mileage} per year')


car = Car('BMW', 'S-Class', 150000)
car.car_details()
car.car_mileage()
print()
bike = Bike('Yamaha', 'MT-15', '50 km/l')
bike.bike_details()
bike.bike_mileage()


