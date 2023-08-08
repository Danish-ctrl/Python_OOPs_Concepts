class Person:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def set_value(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_value(self):
        print(self.__name, self.__phone)


p = Person('Danish', '123')
p.get_value()
print()
p.set_value('abc', '456')
p.get_value()

