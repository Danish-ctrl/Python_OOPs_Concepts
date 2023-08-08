class Restaurant:
    def __init__(self, rest_name, cusine_type):
        self.rest_name = rest_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_rest(self):
        print(f"Name of the restaurant is {self.rest_name}")
        print(f"Cusine type is {self.cusine_type}")

    @staticmethod
    def open_rest():
        print("Restaurant is open !")

    def set_number_served(self):
        print(f"Number of customers served are {self.number_served}")

    def increment_number_served(self, inc):
        self.number_served += inc
