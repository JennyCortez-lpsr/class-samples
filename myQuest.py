print("Welcome to Jenny's quest!")

print("Enter the name of your character:")

name = raw_input()
print("Your points must add up to the maximum of 15 points")

print("Enter strength (1-10):")
strength = int(raw_input())

print("Enter health (1-10):")
health = int(raw_input())

print("Enterr luck (1=10):")
luck = int(raw_input())

total_points = strength + health + luck
print("Your total points are " + str(total_points))

if total_points > 15:
	print("You have given your character to many points")
	health = 5
	strength = 5
	luck = 5
	print("Your points now " + str(health) + " for health " + str(strength) + " for strength and " + str(luck) + " for luck")
print(name + ",you've come to a fork in the road. Would you like to go left or right. Enter left or right")

direction = raw_input()

if direction == "left":
	if health <= 7:
		print(name + " you have fallen into a hole, your health was to low to survive the fall")
		print("Game Over, try again")
	else:
		print(name + " you have fallen into a hole")
		print("You survived the fall")
		print("Congrats on surving, you win!!")
else:
	if strength >= 7:
		print(name + " a tree fell on you")
		print("You were able to push the tree off yourself")
		print("Congrats on surviving, you win!!")
	else:
		print(name + " a tree fell on you")
		print("Sorry you didn't have enough strength, Game Over, try again")
