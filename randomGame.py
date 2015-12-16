import random

print("I'm thinking of a number between 1 and 1000. Enter your guess!")

myNum = random.randint(1, 1000)
guess = int(input())
myNums = int(myNum)
while guess > myNums:
	print("Nope your guess is too high. Guess again.")
	guess = int(input())		        
	while guess < myNums:
                print("Nope your guess is too low. Guess again.")
		guess = int(input())
if guess == myNums:
	print("Your guess is correct. You Win!")


	
