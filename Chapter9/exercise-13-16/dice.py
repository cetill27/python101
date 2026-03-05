
from random import choice
class Dice:
    def __init__(self):
        self.sides = 6;
    def roll_die(self):
        print(choice(range(1,self.sides)))

new_dice = Dice()

for i in range(1,10):
    new_dice.roll_die()