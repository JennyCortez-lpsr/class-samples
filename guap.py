# for every roll of paper towels, you get a $0.25 rebate
# but if you buy more than 10 rolls, you get a $0.35 rebate for each one

# but if you're a value club member,
# you get a $2 rebate for buying at least one roll

# find out if user is a value club member
print("Are you a value club member? Respond yes or no.")
club = raw_input()

# find out how many rolls of paper towels user bought 
print("How many rolls of paper towels did you buy?")
rolls = int(raw_input())

if club == "yes":
	print("in the club")
	if rolls > 10:
	   rebate = rolls * .35 + 2
	else:
	   rebate = rolls * .25 + 2
else:
	print("not in the club")
	if rolls > 10:
	   rebate = rolls * .35
	else:
	   rebate = rolls * .25
# print  rebate 
print("Your rebate is $" + str(rebate))
