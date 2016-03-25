# takes myNum, an integer
# returns True if myNum is prime
# returns False if myNum is not prime
# a list of numbers from 2 to 10000
list = range(2,10001)
# opens the file primes.txt and it writes things inside
file = open("primes.txt", 'w')
# function so it defines prime numbers 
def isPrime(myNum):
# for every number in the range of 2 to any number divide by every number and find remainder
	for n in range(2, myNum):
		if myNum % n == 0:
			# if it = 0 then its false
			return False
		# if not then its true
		else:
 			return True	
# for every prime number in the list then print them in the primes.txt file
for myNum in list:
	 if isPrime(myNum):
		file.write(str(myNum))
# closes the file
file.close()
