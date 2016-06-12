# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher 
#
# Author: rc.cortez.jennifer [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
import string

def createDictionary(key):
	# creates a lower case and upper case alphabet
	lowAlph = string.ascii_lowercase
	upAlph = string.ascii_uppercase
	# makes a dictionary
	order = {}
	# creates a count
	c = 0
	# for every letter in the alphabet put it in the dictionary and adds the count by 1
	for l in lowAlph:
		order[l] = lowAlph[(key + c) % 26]
		c = c + 1
	for l in upAlph:
		order[l] = upAlph[(key + c) % 26]
		c = c + 1
	# placeholder
	return order
	
# asks user for encoded message with raw input
# arguments: none
# returns: encoded message
def getMessage(message):
	return message

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	new = ''
	# for very message look into dictionary
	for m in message:
		x = dictionary[m]
		new = new + x
	return new

# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(message):
	print(message)

# execution starts here
try:
	# ask user for key
	print("What key would you like to use to decode?")

	key = int(raw_input())
	# finds the key in the dictionary
	dictionary = createDictionary(key)
	print("Which message would you like to decode?")
	choice = raw_input()
	# gets the users message
	encodedMessage = getMessage(choice)
	# decodes the message
	decodedMessage = decodeMessage(encodedMessage, dictionary)
	print("Here's the decoding of your message:")
	# prints the decoded message
	printMessage(decodedMessage)
# if user input doesnt run print the following
except:
	print("This code can't be run. Try again")
