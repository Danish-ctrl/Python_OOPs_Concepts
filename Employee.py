class Employee:
    def __init__(self, f_name, l_name, salary, increment=1000):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.increment = increment

    def give_raise(self):
        self.salary = self.salary + self.increment
        return self.salary

# emp = Employee('Dan', 'Reza', 1000)
# emp2 = Employee('Dssan', 'Rsseza', 2000, 500)
#
# x = emp.give_raise()
# y = emp2.give_raise()
# print(x)
# print(y)

