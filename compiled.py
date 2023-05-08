import tkinter as tk
from tkinter import ttk
import random
import time

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

class Dragon:
    def __init__(self, health):
        self.health = health
        fire_breath = Weapon("Fire Breath", "1d12+4")
        self.weapons = [fire_breath]

    def is_alive(self):
        return self.health > 0
    
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

def print_sleep(message, sleep_time=1.3):
    print(message)
    time.sleep(sleep_time)

def write_with_sleep(write, message, sleep_time=0.7):
    write(message)
    time.sleep(sleep_time)

def get_attack(weapons, write, read):
    while True:
        write_with_sleep(write, "\nWhat attack should you use?\n", 0.2)
        for idx, weapon in enumerate(weapons, start=1):
            write_with_sleep(write, f"{idx}: {weapon.name} ({weapon.dice_roll})\n", 0)
        user_choice = read()
        if user_choice.isdigit() and 1 <= int(user_choice) <= len(weapons):
            return weapons[int(user_choice) - 1]
        write_with_sleep(write, "\nInvalid input. Please choose a valid attack.\n", 0)
    
def initialize_game():
    sword = Weapon("Sword", "1d6+2")
    iron_fist = Weapon("Iron Fist", "1d8")
    player = Player(30, [sword, iron_fist])
    num_trolls = random.randint(3, 6)
    trolls = [Troll(random.randint(6, 18)) for _ in range(num_trolls)]
    dragon = Dragon(50)

    return sword, iron_fist, player, trolls, num_trolls, dragon

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

def battle_with_dragon(write, read, player, dragon):
    while dragon.is_alive() and player.is_alive():
        attack = get_attack(player.weapons, write, read)
        damage = attack.get_damage()
        dragon.health -= damage
        write_with_sleep(write, f"\nYou attacked with the {attack.name}, causing {damage} damage.\n")
        write_with_sleep(write, f"\nYour current target has {dragon.health} health left\n")

        if dragon.is_alive():
            dragon_attack = random.choice(dragon.weapons)
            dragon_damage = dragon_attack.get_damage()
            player.health -= dragon_damage
            write_with_sleep(write, f"\nThe Dragon attacked with the {dragon_attack.name}, causing {dragon_damage} damage in return\n")
            write_with_sleep(write, f"\nYou have {player.health} health left\n")
        else:
            write_with_sleep(write, f"\nThe dragon has been defeated!.\n")

def play_game(write, read, window):
    play_again = "yes"

    while play_again in ["yes", "y"]:
        sword, iron_fist, player, trolls, num_trolls, dragon = initialize_game()

        display_intro(write, num_trolls, sword, iron_fist)
        boost_health_if_needed(write, player, num_trolls)

        for troll in trolls:
            write_with_sleep(write, f"\nCurrent troll health is {troll.health}\n")
            battle_with_troll(write, read, player, troll, trolls, num_trolls)

        trolls_still_alive = sum(1 for troll in trolls if troll.health > 0)

        dragon_active = False

        if trolls_still_alive == 0 and player.health > 10:
            dragon_active = True
            write_with_sleep(write, f"\nA Dragon has appeared with {dragon.health} health\n")
            battle_with_dragon(write, read, player, dragon)

        if player.is_alive():
            outcome = "\nYou are victorious! You killed all the trolls!\n" if dragon_active == False else "\nYou defeated the trolls and the dragon!\n"
        elif dragon_active:
            outcome = "\nYou were slayed by the Dragon!\n"
        else:            
            outcome = "\nYou killed the trolls but died in the process!\n" if trolls_still_alive == 0 else f"\nYou have died! {trolls_still_alive} trolls are still alive\n"

        write_with_sleep(write, outcome)

        write_with_sleep(write, "Do you want to play again? [yes, no]")

        play_again = read().lower()

        if play_again in ["no", "n"]:
            window.destroy()

class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Troll Slayer")
        self.geometry("600x400")

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(pady=20)

        self.text_widget = tk.Text(self.main_frame, wrap=tk.WORD, width=60, height=15)
        self.text_widget.pack()

        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=10)

        self.entry = ttk.Entry(self.input_frame, width=30)
        self.entry.pack(side=tk.LEFT)
        self.entry.bind('<Return>', lambda event: self.process_input())

        self.submit_button = ttk.Button(self.input_frame, text="Submit", command=self.process_input)
        self.submit_button.pack(side=tk.LEFT)

        self.current_input = ""

    def process_input(self):
        self.current_input = self.entry.get().strip().lower()
        self.entry.delete(0, tk.END)

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)
        self.text_widget.update()

    def read(self):
        self.current_input = ""
        while not self.current_input:
            self.update()
        return self.current_input

def main():
    game_window = GameWindow()
    game_window.write("Welcome to Troll Slayer!\n\n")
    play_game(game_window.write, game_window.read, game_window)
    game_window.mainloop()

if __name__ == "__main__":
    main()