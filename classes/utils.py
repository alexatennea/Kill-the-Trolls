import time

def print_sleep(message, sleep_time=1.3):
    print(message)
    time.sleep(sleep_time)

def get_attack(weapons, write, read):
    while True:
        write("\nWhat attack should you use?")
        for idx, weapon in enumerate(weapons, start=1):
            write(f"{idx}: {weapon.name} ({weapon.dice_roll})")
        user_choice = read()
        if user_choice.isdigit() and 1 <= int(user_choice) <= len(weapons):
            return weapons[int(user_choice) - 1]
        write("\nInvalid input. Please choose a valid attack.")
