import random
import time

# Set the variables

health = 20
sword = random.randint(1, 5)
ironfist = random.randint(2, 4)
trollshealth = 6
trollattack = random.randint(1,3)
trolls = random.randint(3, 6)

playagain = "yes"

# Win This One
# The infinite loop of victory


while playagain == "yes" or playagain == "y":

	print("\n\tYour hero enters a room and inside there are", trolls, "trolls")
	time.sleep(1.3)
	print("\n\tYour hero has 2 attacks, help him use them wisely")
	time.sleep(1.3)
	print("\n\tThe Sword deals between 1 and 5 damage")
	time.sleep(1.3)
	print("\n\tThe Iron Fist deals between 2 and 4 damage")
	time.sleep(1.3)
	if trolls > 4:
		health += 5
		print("\n\tAs there are", trolls, "trolls, you have been granted 5 extra health")
		time.sleep(1.3)
	print("\n\tYou have", health, "health\n")
	time.sleep(1.3)
	

	while trolls != 0 and health > 0:
	
		attack = int(input("\nWhat attack should you use? [Enter 1 for Sword or 2 for Iron Fist]\n\n"))
		time.sleep(.75)

		if attack == 1:
			trollshealth -= sword
			print("\nYou attacked with the Sword, causing", sword, "damage.\n")
			time.sleep(.75)
			del sword
			sword = random.randint(1, 5)
			health -= trollattack
			print("The troll dealt", trollattack, "damage in return\n")
			time.sleep(.75)
			del trollattack
			trollattack = random.randint(0,3)
			print("You have", health, "health left\n")	
			time.sleep(.75)	
			print("Your current target has", trollshealth, "health left\n")
			time.sleep(.75)
			if trollshealth <= 0:
				trolls -= 1
				print("One troll down!", trolls, "trolls left!\n")
				time.sleep(.75)
				trollshealth = 6
			else:
				print("There are", trolls, "trolls left\n")
				time.sleep(.75)

		elif attack == 2: 
			trollshealth -= ironfist
			print("\nYou used Iron Fist, causing", ironfist, "damage.\n")
			time.sleep(.75)
			del ironfist
			ironfist = random.randint(2, 4)
			health -= trollattack
			print("The troll dealt", trollattack, " damage in return\n")
			time.sleep(.75)
			del trollattack
			trollattack = random.randint(0,3)
			print("You have", health, "health left\n")
			time.sleep(.75)
			print("Your current target has", trollshealth, "health left\n")
			time.sleep(.75)
			if trollshealth <= 0:
				trolls -= 1
				print("One troll down!", trolls, "trolls left!\n")
				time.sleep(.75)
				trollshealth = 6
			else:
				print("There are", trolls, "trolls left\n")
				time.sleep(.75)

	if trolls == 0 and health <= 0:
		print("You killed the trolls but died in the process!")
		time.sleep(.75)
	elif trolls == 0:
		print("You are victorious! You killed all the trolls!")
		time.sleep(.75)
	else:
		print("You died before killing all the trolls.")
		time.sleep(.75)

	trolls = random.randint(3, 6)
	health = 20
	trollshealth = 6

	playagain = ""

	while not playagain:		
		shallwe = input("\nPlay again? [yes or no] ")

		if shallwe == "yes" or shallwe == "y":
			playagain = "yes"
		elif shallwe == "no" or shallwe == "n":
			playagain = "no"


print ("\nIt has been a pleasure slaughtering with you.")