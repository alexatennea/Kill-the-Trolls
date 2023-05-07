class Character:
    def __init__(self, health):
        self.health = health

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def __init__(self, health, weapons):
        super().__init__(health)
        self.weapons = weapons

class Troll(Character):
    def __init__(self, health):
        super().__init__(health)
