class BankAccount:
    def __init__(self, name, age, address, account_number):
        self.name = name
        self.age = age
        self.address = address
        self.account_number = account_number

    def account_info(self):
        print(f"Name of the account holder is: {self.name}\nHis age is: {self.age}\nHis address is: {self.address}\nHis"
              f"account number is: {self.account_number}")


customer = BankAccount('Danish', 28, 'V72/604', 123456)
customer.account_info()