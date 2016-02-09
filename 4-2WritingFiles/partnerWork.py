# we are writing a program that ask a user for each line of haiku 
print("Welcome to the Haiku generator!") 
print("Provide the first line of your haiku:")
# create a list to write to my file
firstL = raw_input() 
print(" ") 
print("Provide the second line of your haiku:") 
secondL = raw_input() 
print(" ") 
print("Provide the third line of your haiku:") 
thirdL = raw_input() 
print(" ") 
print("What file would you like to write your haiku to?")
 
 
# ask the user for raw_input
x = raw_input() 
myProgram = open( x , "w")
 
myProgram.write(firstL +'/n' ) 
myProgram.write(secondL + '/n') 
myProgram.write(thirdL + '/n')
 
print("Done! To view your haiku, type 'cat' and the name of your file at the command line.") 
print("When you run cat and the file name at the terminal, you should get your haiku!")
 
myProgram.close()
