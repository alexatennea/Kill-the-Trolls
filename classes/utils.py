import time

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
