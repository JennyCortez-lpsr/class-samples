# opens the file of the instructions
walking_file = open('walking_instructions.txt', 'r')
# reads each line of the walking file
lineToPrint = walking_file.readline()
while lineToPrint != "":
	# prints each line with duh after it on a seperate line
	print(lineToPrint + ", duh")
	lineToPrint = walking_file.readline()
# closes the file
walking_file.close()
