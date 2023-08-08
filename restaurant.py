from restaurant_module import Restaurant
from admin_module import User, Previlage, Admin

restaurant = Restaurant('Dani_rest', 'Barfi')
restaurant.describe_rest()
print()

res1 = Restaurant('Reza_rest', 'Cus_1')
res2 = Restaurant('Omi_rest', 'Cus_2')
res3 = Restaurant('Ozi_rest', 'Cus_3')
res1.describe_rest()
res2.describe_rest()
res3.describe_rest()
Restaurant.open_rest()

print('+++++++++++++')





user_1 = User('Danish', 'Reza')
user_2 = User('Omi', 'abc')
user_3 = User('Ozi', 'def')

user_1.describe_user()
user_1.greet_user()
print()
user_2.describe_user()
user_2.greet_user()
print()
user_3.describe_user()
user_3.greet_user()
print('++++++++++++++++++++++++++')
print()

print(restaurant.number_served)
restaurant.number_served = 10
restaurant.set_number_served()

restaurant.increment_number_served(500)
restaurant.set_number_served()
print('+++++++++++++++++++++++++++')
print()

user_login_attempt = User('Abc', 'Def')
user_login_attempt.increment_login_attempt(1)
print()
user_login_attempt.increment_login_attempt(1)
print()
user_login_attempt.increment_login_attempt(1)
print()
user_login_attempt.reset_login_attempt()
print()
user_login_attempt.increment_login_attempt(1)
print('++++++++++++++++++++++++++')
print()


class IceCreamStand(Restaurant):
    def __init__(self, rest_name, cusine_type, flavour):
        super().__init__(rest_name, cusine_type)
        self.flavour = flavour

    def disp_flavour(self):
        print(self.flavour)


ice_cream_stand = IceCreamStand('Chemnitz_bakery', 'gulab_jamun', flavour=['strawberry', 'kaju', 'mango'])
ice_cream_stand.disp_flavour()

print('++++++++++++++++++++++++++')
print()


previllag_list = ['First_class', 'second_class', 'third_class']
admin = Admin('Mohammed', 'Danish')
# admin.show_previllage()

admin.prev.show_previllage()











