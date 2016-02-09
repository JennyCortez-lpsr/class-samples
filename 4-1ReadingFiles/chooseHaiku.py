# opens the file object of the third and fourth haiku
myThirdHaiku = open('haiku3.txt', 'r') 
myFourthHaiku = open('haiku4.txt', 'r')
# prints user choices
print("Hi, welcome to the Haiku Reader!") 
print("Choose...") 
print("(3) For a haiku about a silly person.") 
print("(4) For a haiku about writing haikus.") 
# user gets to pick their option
choice = int(raw_input())
# if the choice is three then print the third haiku
if choice == 3:
	print(myThirdHaiku.read())
# if the choice is 4 then print the fourth haiku
elif choice == 4:
	print(myFourthHaiku.read())
