contacts = {}

choice = 0

while choice != 0:
	print("What would you like to do?")
	print("(1) Add a phone number.")
	print("(2) Print the full list of contacts.")
	print("(3) Enter a name to retrieve that contact's phone number.")
	print("(0) Exit the Contacts app.")
	choice = int(raw_input())

	if choice == 1:
		print("What is the name of your contact?")
		name = raw_input()
		print("What is their phone number?")
		num = raw_input()
		contacts[name] = num

	if choice == 2:
		print(contacts)

	if choice == 3:
		print("Who's number would you like to see?")
		name = raw_input()
		print("Here is their number")
		print(contacts[name])
