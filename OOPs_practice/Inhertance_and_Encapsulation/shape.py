class Shape:
    def __init__(self, radius, sides, pi=3.17):
        self.radius = radius
        self.sides = sides
        self.pi = pi


class Circle(Shape):
    def __init__(self, radius, pi=3.17):
        super().__init__(radius, pi)

    def area(self):
        area = self.pi * self.radius * self.radius
        print(f'Area of circle is: {area}')

    def perimeter(self):
        peri = 2 * self.pi * self.radius
        print(f'Perimeter of circle is: {peri}')


class Rectangle(Shape):
    def __init__(self, sides):
        super().__init__(sides)

    def area(self):
        area = self.sides * self.sides
        print(f'Area of rectangle is: {area}')

    def perimeter(self):
        peri = 4 * self.sides
        print(f'Perimeter of rectangle is: {peri}')


s = Circle(3)
s.area()
s.perimeter()