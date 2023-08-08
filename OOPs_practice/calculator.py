class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        summ = self.a + self.b
        print(summ)

    def subs(self):
        difference = self.a - self.b
        print(difference)

    def mult(self):
        mul = self.a * self.b
        print(mul)


cal = Calculator(5, 4)
cal.addition()
cal.subs()
cal.mult()