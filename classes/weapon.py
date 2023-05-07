import random

class Weapon:
    def __init__(self, name, min_damage, max_damage):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)
