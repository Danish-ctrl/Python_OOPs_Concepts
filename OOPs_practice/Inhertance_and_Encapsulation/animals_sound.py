class Animals:
    def sound(self):
        pass


class Dog(Animals):
    def sound(self):
        print('Sound of a dog is Woof')


class Cat(Animals):
    def sound(self):
        print('Sound of a cat is Meow')


d = Dog()
d.sound()
print()
c = Cat()
c.sound()
