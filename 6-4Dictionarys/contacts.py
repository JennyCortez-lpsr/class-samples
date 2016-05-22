# makes an empty dictionary
contacts = {}

choice = 1
# while loop is not 0 ask the following questions
while choice != 0:
	print("What would you like to do?")
	print("(1) Add a phone number.")
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(0) Exit the Contacts app.")
	# lets user choose one of the options
	choice = int(raw_input())
	# if there choice is when the ask the following questions and let user answer them
	if choice == 1:
		print("What is the name of your contact?")
		name = raw_input()
		print("What is their phone number?")
		num = raw_input()
		# will print the name and num they choose into the contacts dictionary
		contacts[name] = num
	# if the choice is 2 then print everything inside contacts
	if choice == 2:
		print(contacts)
	# if there choice is 3 then ask question they answer
	if choice == 3:
		print("Who's number would you like to see?")
		name = raw_input()
		print("Here is their number")
		# will print the information of name user input
		print(contacts[name])
