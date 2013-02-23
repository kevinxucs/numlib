# factor.py
# created by Kaiwen Xu
# 
# module for calculating factors

import math
import prime, integer

def isFactor(num, factor):
	"""Determine whether the factor given is the proper factor of the number.
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
		pflist = getFactors(num, primeFactor=True, proper=False)
		d = 1
		if pflist:
			for pf in pflist:
				d *= getMaxFactorPower(num, pf) + 1
			return d
		else:
			# means the number is a prime, which only has 2 divisors
			return 2
	else:
		raise Exception('No implementation named ' + repr(method) +  \
		' found.')


def getFactors(num, primeFactor=False, proper=False, nontrivial=False, method='brute'):
	"""Return a list of factors for the number given.
	'num' - number.
	(optional) 'primeFactor' - whether return prime factor only. 
	False by default.
	(optional) 'proper' - proper divisor. False by default.
	(optional) 'method' - implementation, which includes brute-force 'brute'.
	'brute' by default.
	"""
	if method == 'brute':
		limit = int(math.sqrt(num))
		lst = []
		i = 1
		
		while i <= limit:
			if num % i == 0:
				lst.append(i)
			i += 1
		
		rlst = lst[::-1]
		for ri in rlst:
			rfactor = int(num / ri)
			lst.append(rfactor)
		
		# proper divisors and non-trivial divisors do not include the number itself
		if proper or nontrivial:
			lst.pop()

		# non-trivial divisors do not include 1
		if nontrivial and lst[0] == 1:
			del lst[0]

		# delete non-prime factors
		if primeFactor:
			lst = filter(prime.isPrime, lst)
		
		return lst
	else:
		raise Exception('No implementation named ' + repr(method) +  \
		' found.')


def getAmicableNumbers(below, above=220, method='brute'):
	"""Return a list of amicable numbers.
	http://en.wikipedia.org/wiki/Amicable_numbers
	
	'below' - smaller or equal to.
	(optional) 'above' - greater or equal to. 220 default.
	(optional) 'method' - implementation, which includes brute-force 'brute'.
	'brute' by default.
	"""
	if above < 0:
		raise Exception('Perfect numbers must be positive integer.')
	if above > below:
		raise Exception("Error: 'above' is greater than 'below'.")
	
	if method == 'brute':
		list = []
		for num in xrange(above, below + 1):
			if num not in list:
				numb = sum(getFactors(num, primeFactor=False, proper=True))
				numa = sum(getFactors(numb, primeFactor=False, proper=True))
				if numa == num and numa != numb:
					list.append(numa)
					list.append(numb)
		
		return list
	
	else:
		raise Exception('No implementation named ' + repr(method) + ' found.')

