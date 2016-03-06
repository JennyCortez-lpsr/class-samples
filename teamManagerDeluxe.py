# creates class 
class Player(object):
	# defines the class
	def __init__(self, name, age, num_goals, jersey, position):
		self.name = name
		self.age = age
		self.num_goals = num_goals
		self.jersey = jersey
		self.position = position

	# defines the stats of the players(name, age and number of goals)
	def playerStats(self):
		print("Name: " + self.name)
		print("Age: " + str(self.age))
		print("Goals: " + str(self.num_goals))
		print("Jersey number: " + str(self.jersey))
		print("Position: " + str(self.position))
# saves the team
def saveTeam(myPlayer, filename):
	# opens file and appends it
	file = open(filename, 'a')
	# for every player in the list write the name, age etc on seperate lines
	for p in myPlayer:
		file.write(p.name + " " + str(p.age) + " " + str(p.num_goals) + " " +  str(p.jersey) + " " + p.position + '\n')
	# close file
	file.close()
# loads team
def loadTeam(filename):
	# empty list
	myPlayer = []
	# opens file and reads it
	myFile = open(filename, 'r')
	# reads line from file
	player = myFile.readline()
	# while theres something in the file then run the following code
	while player != "":
		# splits all the elements of every player on seperate lines
		splitplayer = player.split()
		# appends every player name, age etc.
		myPlayer.append(Player(splitplayer[0], splitplayer[1], splitplayer[2], splitplayer[3], splitplayer[4]))
		# reads the line again
		player = myFile.readline()
	# close the file
	myFile.close()
	# returns the player
	return myPlayer	
# prints what's in the parenthesis
print("Welcome to teamManagerDeluxe.py!") 
print("Pick and enter your choice.") 
print("(1) Start with a new team") 
print("(2) Open a file for an existing file")
# lets user choose their choice 
choice = int(raw_input())
# if the user chooses 2 then the following will run
if choice == 2:
	print("What's the filename for your existing team? Enter the whole name, including its .tmd extension.")
	# the user writes their filename 
	filename = raw_input()
	# the team will load and show the player stats on seperate lines
	myPlayer = loadTeam(filename)
	# lets user choose their next choice
	print("Pick your choice:")
	print("(1) Add a player (2) View players (3) Save Team (0) exit")
	choice = int(raw_input())

else:
# my list is empty
	myPlayer = []
# while the user choice is not 0 then do the following if it is 0 then exit the program
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
		print("What is your player's jersey number?")
		num = int(raw_input())
		print("What position does your player play?")
		position = raw_input()
		# adds the player you add to the list
		myPlayer.append(Player(name, age, goals, num, position))
		# lets user choose their next choice
		print("What do you want to do now?")
		print("(1) Add a player (2) View players (3) Save Team (0) exit")
		choice = int(raw_input())
		c = c + 1
# if the choice is 2 then print the player stats and ask them to choose
	if choice == (2):
		# for every person in the list print their stats
		myPlayer = loadTeam(filename)
		for p in myPlayer:
		        p.playerStats()
		# lets user choose their next choice
		print("What do you want to do now?")
		print("(1) Add a player (2) View players (3) Save Team (0) exit")
		choice = int(raw_input())
	# if the users choice is 3 then do the following
	if choice == (3):
		print("What is your team file name?")
                userfile = raw_input()
		# saves team 
                myPlayer = saveTeam(myPlayer, filename)
		# asks user what their next choice is
                print("What do you want to do know?")
	        print("(1) Add a player (2) View players (3) Save Team (0) exit")
                choice = int(raw_input())
               
