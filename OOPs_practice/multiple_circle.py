class Circle:
    def __init__(self, radius, pi=3.17):
        self.radius = radius
        self.pi = pi

    def area_of_circle(self):
        area = self.pi * self.radius * self.radius
        print(f'Area of circle is {area}')

    def peri_of_circle(self):
        perimeter = 2 * self.pi * self.radius
        print(f"Perimeter of cicle is {perimeter}")


c = Circle(3)
c1 = Circle(4)
c.area_of_circle()
c.peri_of_circle()
print()
c1.area_of_circle()
c1.peri_of_circle()