class MyClass:
    def __init__(self, age=15):
        self.__private_variable = 42
        self.age = age

    def get_private_variable(self):
        print(self.__private_variable)


# Creating an instance of the class
obj = MyClass()

# Accessing the private variable using a getter method
obj.get_private_variable()
# print(value)  # Output: 42

# Attempting to access the private variable directly (which is not recommended)
# This will raise an AttributeError
# print(obj.__private_variable)  # Uncomment this line to see the error

# Accessing the private variable using the name-mangled version
value = obj._MyClass__private_variable
print(value)  # Output: 42

print()
print(obj.age)
print()

