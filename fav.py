print("What's your favorite number?")

fav_number = input()

if int(fav_number) == 14:
	print("Great choice that's the best number in the world!")

while int(fav_number) > 14 or int(fav_number) < 14:
	print("I don't like that number-try another")
