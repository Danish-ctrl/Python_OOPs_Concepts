class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempt = 0

    def describe_user(self):
        print(f"User first name is {self.first_name} and last name is {self.last_name}")

    def greet_user(self):
        print(f"Welcome to our restaurant {self.first_name} {self.last_name}")

    def increment_login_attempt(self, inc):
        self.login_attempt += inc
        print(f"Login attempt is {self.login_attempt}")

    def reset_login_attempt(self):
        self.login_attempt = 0


class Previlage:
    def __init__(self):
        self.previllage = ['First_class', 'Second_class', 'Third_class']

    def show_previllage(self):
        print(self.previllage)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

        self.prev = Previlage()
    # def show_previllage(self):
    #     print(self.previllage)
