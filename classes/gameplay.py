import random

from classes.character import Player, Troll
from classes.weapon import Weapon
from classes.utils import print_sleep, get_attack

def initialize_game():
    sword = Weapon("Sword", 1, 5)
    iron_fist = Weapon("Iron Fist", 2, 4)
    player = Player(30, [sword, iron_fist])
    num_trolls = random.randint(3, 6)
    trolls = [Troll(6) for _ in range(num_trolls)]

    return sword, iron_fist, player, trolls, num_trolls

def display_intro(num_trolls):
    print_sleep(f"\n\tYour hero enters a room and inside there are {num_trolls} trolls")
    print_sleep("\n\tYour hero has 2 attacks, help him use them wisely")
    print_sleep(f"\n\tThe Sword deals between 1 and 5 damage")
    print_sleep(f"\n\tThe Iron Fist deals between 2 and 4 damage")

def boost_health_if_needed(player, num_trolls):
    if num_trolls > 4:
        player.health += 5
        print_sleep(f"\n\tAs there are {num_trolls} trolls, you have been granted 5 extra health")
    print_sleep(f"\n\tYou have {player.health} health\n")

def battle_with_troll(player, troll):
    while troll.is_alive() and player.is_alive():
        attack = get_attack(player.weapons)
        damage = attack.get_damage()
        troll.health -= damage
        print_sleep(f"\nYou attacked with the {attack.name}, causing {damage} damage.")

        if troll.is_alive():
            troll_attack = random.randint(0, 3)
            player.health -= troll_attack
            print_sleep(f"The troll dealt {troll_attack} damage in return")
            print_sleep(f"You have {player.health} health left")
            print_sleep(f"Your current target has {troll.health} health left")
        else:
            print_sleep(f"Current troll has died. {trolls.index(troll) + 1} of {num_trolls} trolls defeated.")

def play_game():
    play_again = "yes"

    while play_again in ["yes", "y"]:
        sword, iron_fist, player, trolls, num_trolls = initialize_game()

        display_intro(num_trolls)
        boost_health_if_needed(player, num_trolls)

        for troll in trolls:
            battle_with_troll(player, troll)

        outcome = "You are victorious! You killed all the trolls!" if player.is_alive() else "You killed the trolls but died in the process!"
        print_sleep(outcome)

        play_again = input("\nPlay again? [yes or no] ").lower()
