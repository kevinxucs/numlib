# factor.py
# created by Kaiwen Xu
# 
# module for calculating factors

from math import pow, sqrt
from prime import isPrime

def isFactor(num, factor):
	if num % factor == 0:
		return True
	else:
		return False

def getMaxFactorPower(num, factor):
	power = 1
	
	while True:
		if num % pow(factor, power) == 0:
			power += 1
		else:
			return power - 1

# implementation includes brute-force 'brute',
# 'prime' - by calculating prime factors and using the properties of 
# divisor function
# http://en.wikipedia.org/wiki/Divisor_function#Properties
def getFactorNum(num, method='brute'):
	if method == 'brute':
		return len(getFactors(num))
	elif method == 'prime':
		pflist = getFactors(num, prime=True)
		d = 1
		if len(pflist) > 0:
			for pf in pflist:
				d *= getMaxFactorPower(num, pf) + 1
			return d
		else:
			# means the number is a prime, which only has 2 divisors
			return 2
	else:
		raise Exception('No implementation named ' + repr(method) +  ' found.')

# implementation includes brute-force 'brute'
def getFactors(num, prime=False, method='brute'):
	if method == 'brute':
		limit = int(sqrt(num))
		list = []
		i = 1
		while i <= limit:
			if num % i == 0:
				if prime == False or (prime == True and isPrime(i)):
					list.append(i)
			i += 1
		rlist = list[::-1]
		for ri in rlist:
			rfactor = int(num / ri)
			if prime == False or (prime == True and isPrime(rfactor)):
				list.append(rfactor)
		return list
	else:
		raise Exception('No implementation named ' + repr(method) +  ' found.')
