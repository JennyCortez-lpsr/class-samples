# asks user to write their first line of their haiku
print("Welcome to the Haiku generator!")
print("Provide the first line of your haiku:")
# allows user to enter their first line
choice = raw_input()
# asks for second line and user can enter it
print("Provide the second line of your haiku:")
choice2 = raw_input()
# asks and allows the third line for the haiku
print("Provide the third line of your haiku:")
choice3 = raw_input()
# asks user what file they want to put their haiku in
print("What file would you like to write your haiku to?")
file = raw_input()
# opens the file
myFile = open((file), "a")
# write in the file
myFile.write(str(choice + '\n' + choice2 + '\n' + choice3 + '\n'))

print("Done! To view your haiku, type 'cat' and the name of your file at the command line.") 
print("When you run cat and the filename at the terminal, you should get your haiku!")
# closes the file
myFile.close()
