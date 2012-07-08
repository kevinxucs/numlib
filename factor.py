# factor.py
# created by Kaiwen Xu
# 
# module for calculating factors

import math
import prime

def isFactor(num, factor):
	"""Judge whether the factor given is the proper factor of the number.
	'num' - number.
	'factor' - factor.
	"""
	if num % factor == 0:
		return True
	else:
		return False

def getMaxFactorPower(num, factor):
	"""For given number and factor, returns the maximum power the factor can 
	have to divide the number.
	'num' - number.
	'factor' - factor of the number.
	"""
	power = 1
	
	while True:
		if num % math.pow(factor, power) == 0:
			power += 1
		else:
			return power - 1

def getFactorNum(num, method='brute'):
	"""Return the amount of factors for the number given.
	'num' - number.
	(optional) 'method' - implementation, which includes 
	brute-force 'brute', 'prime' - by calculating prime factors 
	and using the properties of divisor function.
	http://en.wikipedia.org/wiki/Divisor_function#Properties
	"""
	if method == 'brute':
		return len(getFactors(num))
	elif method == 'prime':
		pflist = getFactors(num, primeFactor=True)
		d = 1
		if len(pflist) > 0:
			for pf in pflist:
				d *= getMaxFactorPower(num, pf) + 1
			return d
		else:
			# means the number is a prime, which only has 2 divisors
			return 2
	else:
		raise Exception('No implementation named ' + repr(method) +  \
		' found.')

def getFactors(num, primeFactor=False, method='brute'):
	"""Return a list of factors for the number given.
	'num' - number.
	(optional) 'primeFactor' - whether return prime factor only.
	(optional) 'method' - implementation, which includes brute-force 'brute'.
	"""
	if method == 'brute':
		limit = int(math.sqrt(num))
		list = []
		i = 1
		while i <= limit:
			if num % i == 0:
				if primeFactor == False or (primeFactor == True and \
				prime.isPrime(i)):
					list.append(i)
			i += 1
		rlist = list[::-1]
		for ri in rlist:
			rfactor = int(num / ri)
			if primeFactor == False or (primeFactor == True and \
			prime.isPrime(rfactor)):
				list.append(rfactor)
		return list
	else:
		raise Exception('No implementation named ' + repr(method) +  \
		' found.')
