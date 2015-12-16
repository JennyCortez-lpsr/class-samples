print("Welcome to PumaPix!")
print("What are your top 5 favorite TV shows")

myList = []
shows = 0
while shows < 5:
	print("Enter a show:")
	shows = shows + 1
	myList.append(raw_input())
print("OK, here's what you entered:")
print(myList)

print("We added two shows to your list")

myList.append('Breaking Bad')
myList.append('The Wire')

a = 1
for aa in myList:
	print(str(a) + "." + aa)
	a = a + 1

