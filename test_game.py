import unittest
from classes.weapon import Weapon
from classes.character import Player, Troll

class TestWeapon(unittest.TestCase):
    def test_weapon_damage_range(self):
        sword = Weapon("Sword", "1d6+2")
        for _ in range(100):
            damage = sword.get_damage()
            self.assertTrue(3 <= damage <= 8)

class TestCharacter(unittest.TestCase):
    def test_player_is_alive(self):
        player = Player(30, [])
        self.assertTrue(player.is_alive())

    def test_troll_is_alive(self):
        troll = Troll(10)
        self.assertTrue(troll.is_alive())

    def test_player_is_dead(self):
        player = Player(-1, [])
        self.assertFalse(player.is_alive())

    def test_troll_is_dead(self):
        troll = Troll(-1)
        self.assertFalse(troll.is_alive())

if __name__ == "__main__":
    unittest.main()
