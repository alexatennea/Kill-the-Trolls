import random

from classes.character import Player, Troll
from classes.weapon import Weapon
from classes.utils import write_with_sleep, get_attack

def initialize_game():
    sword = Weapon("Sword", "1d6+2")
    iron_fist = Weapon("Iron Fist", "1d8")
    player = Player(30, [sword, iron_fist])
    num_trolls = random.randint(3, 6)
    trolls = [Troll(random.randint(6, 18)) for _ in range(num_trolls)]

    return sword, iron_fist, player, trolls, num_trolls

def display_intro(write, num_trolls, sword, iron_fist):
    write_with_sleep(write, f"\nYour hero enters a room and inside there are {num_trolls} trolls\n")
    write_with_sleep(write, "\nYour hero has 2 attacks, help him use them wisely\n")
    write_with_sleep(write, f"\nThe Sword deals {sword.dice_roll} damage\n")
    write_with_sleep(write, f"\nThe Iron Fist deals {iron_fist.dice_roll} damage\n")

def boost_health_if_needed(write, player, num_trolls):
    if num_trolls > 4:
        player.health += 5
        write_with_sleep(write, f"\nAs there are {num_trolls} trolls, you have been granted 5 extra health\n")
    write_with_sleep(write, f"\nYou have {player.health} health\n")

def battle_with_troll(write, read, player, troll, trolls, num_trolls):
    while troll.is_alive() and player.is_alive():
        attack = get_attack(player.weapons, write, read)
        damage = attack.get_damage()
        troll.health -= damage
        write_with_sleep(write, f"\nYou attacked with the {attack.name}, causing {damage} damage.\n")
        write_with_sleep(write, f"\nYour current target has {troll.health} health left\n")

        if troll.is_alive():
            troll_attack = random.choice(troll.weapons)
            troll_damage = troll_attack.get_damage()
            player.health -= troll_damage
            write_with_sleep(write, f"\nThe troll attacked with the {troll_attack.name}, causing {troll_damage} damage in return\n")
            write_with_sleep(write, f"\nYou have {player.health} health left\n")
        else:
            write_with_sleep(write, f"\nCurrent troll has died. {trolls.index(troll) + 1} of {num_trolls} trolls defeated.\n")


def play_game(write, read, window):
    play_again = "yes"

    while play_again in ["yes", "y"]:
        sword, iron_fist, player, trolls, num_trolls = initialize_game()

        display_intro(write, num_trolls, sword, iron_fist)
        boost_health_if_needed(write, player, num_trolls)

        for troll in trolls:
            write_with_sleep(write, f"\nCurrent troll health is {troll.health}\n")
            battle_with_troll(write, read, player, troll, trolls, num_trolls)

        trolls_still_alive = sum(1 for troll in trolls if troll.health > 0)

        if player.is_alive():
            outcome = "\nYou are victorious! You killed all the trolls!\n"
        else:            
            outcome = "\nYou killed the trolls but died in the process!\n" if trolls_still_alive == 0 else f"\nYou have died! {trolls_still_alive} trolls are still alive\n"

        write_with_sleep(write, outcome)

        write_with_sleep(write, "Do you want to play again? [yes, no]")

        play_again = read().lower()

        if play_again in ["no", "n"]:
            window.destroy()
