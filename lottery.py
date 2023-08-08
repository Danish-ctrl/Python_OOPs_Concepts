from random import choice
lottery_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e']


class Ticket:
    def __init__(self, random_list):
        self.lottery_list_2 = random_list
        self.matching_list = []
        self.chance_list = []
        # self.counter = 1
        self.i = 1

    def prize_winner(self):
        for i in range(4):
            random_number = choice(self.lottery_list_2)
            # print(list(random_number))
            self.matching_list.append(random_number)

        print(self.matching_list)
        print("Any ticket matching the above numbers wins a prize")

    def my_chance(self):
        # for i in range(self.counter)
        while self.i>=1:
            for j in range(4):
                random_number = choice(self.lottery_list_2)
                # print(list(random_number))
                self.chance_list.append(random_number)
                print(self.chance_list)

            if self.matching_list == self.chance_list:
                print(f"For a winning ticket to match , the loop had to run {self.i} times")
                break
            else:
                self.i += self.i
                # print(f"{self.i} time unmatch")








numbers = Ticket(lottery_list)
numbers.prize_winner()
numbers.my_chance()
