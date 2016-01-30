# creates class
class Player(object):
	# defines the class
	def __init__(self, name, age, num_goals):

		self.name = name
		self.age = age
		self.num_goals = num_goals
	# defines the stats of the players(name, age and number of goals)
	def playerStats(self):
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.num_goals))

# prints questions below
print("Welcome to teamManager.py!")
print("Would you like to choose 0, 1 or 2?")
print("(0) Exit program")
print("(1) Add players")
print("(2) Print players")

choice = int(raw_input())
# my list is empty
myPlayer = []

# while the user choice is not 0 then do the following 
# if it is 0 then exit the program
c = 0
while choice != (0):
#if the choice is one then print the following questions 
	if choice == (1):
		print("What is the name of your player?")
		# lets the user insert their choice of their desired player
		name = raw_input()
		print("What is your player's age?")
		age = int(raw_input())
		print("How many goals has your player scored?")
		goals = int(raw_input())
		# adds the player you add to the list
		myPlayer.append(Player(name, age, goals))
		print("Now would you like to choose 0, 1 or 2?")
		choice = int(raw_input())
		c = c + 1
# if the choice is 2 then print the player stats and ask them to choose	
	elif choice == (2):
		# for every person in the list print their stats
		for p in myPlayer:
		        p.playerStats()
		print("Now would you like to choose 0, 1 or 2?")
		c = c + 1	
		choice = int(raw_input())

