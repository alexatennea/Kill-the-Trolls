from classes.weapon import Weapon

class Character:
    def __init__(self, health):
        self.health = health

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, health, weapons):
        super().__init__(health)
        self.weapons = weapons

class Troll:
    def __init__(self, health):
        self.health = health
        club = Weapon("Club", "1d4+2")
        fist = Weapon("Fist", "1d4")
        self.weapons = [club, fist]

    def is_alive(self):
        return self.health > 0
