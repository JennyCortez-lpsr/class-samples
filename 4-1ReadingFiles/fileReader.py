# shows how file reading works in python

# make a file object
myHaiku = open("haiku1.txt", "r")

print(myHaiku.read())

myHaiku.close()

