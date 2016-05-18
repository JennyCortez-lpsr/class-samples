# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher 
#
# Author: rc.cortez.jennifer [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	# placeholder
	return {}

# asks user for encoded message with raw input
# arguments: none
# returns: encoded message
def getMessage():
	pass

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
	pass

# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(message):
	pass

# execution starts here

# ask user for key
print("What key would you like to use to decode?")

key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)
printMessage(decodedMessage)
