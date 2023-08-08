from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        random_number = 0
        for i in range(1, 11):
            random_number = randint(1, self.sides)

        print(random_number)

die_6 = Die()
die_6.roll_die()

die_10 = Die(10)
die_10.roll_die()

die_20 = Die(20)
die_20.roll_die()

