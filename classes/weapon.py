import random

class Weapon:
    def __init__(self, name, dice_roll):
        self.name = name
        self.dice_roll = dice_roll

    def get_damage(self):
        num_dice, sides = self.dice_roll.split('d')
        if '+' in sides:
            sides, bonus = sides.split('+')
            bonus = int(bonus)
        else:
            bonus = 0
        return sum(random.randint(1, int(sides)) for _ in range(int(num_dice))) + bonus
