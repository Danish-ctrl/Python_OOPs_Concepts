class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def move(self):
        pass


class Bird(Animals):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def make_sound(self):
        return 'Chirp'

    def move(self):
        return 'Fly'


class Fish(Animals):
    def __init__(self, name, species, habitat):
        super().__init__(name, species)
        self.habitat = habitat

    def make_sound(self):
        return 'No Sound'

    def move(self):
        return 'Swim'


b = Bird("Sparrow", "Passer domesticus", 15)
print('Name: ', b.name)
print('Species: ', b.species)
print('Sound: ', b.make_sound())
print('Move: ', b.move())