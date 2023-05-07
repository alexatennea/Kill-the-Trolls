import time

def print_sleep(message, sleep_time=1.3):
    print(message)
    time.sleep(sleep_time)

def get_attack(weapons):
    while True:
        try:
            attack = int(input(f"\nWhat attack should you use? [{' or '.join([f'Enter {i+1} for {weapon.name}' for i, weapon in enumerate(weapons)])}]\n\n"))
            if 1 <= attack <= len(weapons):
                return weapons[attack - 1]
        except ValueError:
            pass
