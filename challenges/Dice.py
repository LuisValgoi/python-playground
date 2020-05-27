import random


class Dice:
    @staticmethod
    def roll():
        value_one = random.randint(1, 6)
        value_two = random.randint(1, 6)
        return value_one, value_two


print(Dice().roll())
print(Dice().roll())
