# factor.py
# created by Kaiwen Xu
# 
# module for calculating factors

import math
import prime
import integer

def isFactor(num, factor):
	"""Determine whether the factor given is the proper factor of the number.

	Arguments:
	num		-- input number
	factor	-- factor
	"""
	if num % factor == 0:
		return True
	else:
		return False


def getMaxFactorPower(num, factor):
	"""For given number and factor, returns the maximum power the factor can 
	have to divide the number.

	Arguments:
	num		-- input number
	factor	-- factor of the number
	"""
	power = 1
	
	while True:
		if num % math.pow(factor, power) == 0:
			power += 1
		else:
			return power - 1


def getFactorNum(num, method='brute'):
	"""Return the amount of factors for the number given.

	Arguments:
	num		-- intput number
	method	-- implementation, which includes 
			   brute-force 'brute' and 'prime' - by calculating prime factors 
			   and using the properties of divisor function
		       http://en.wikipedia.org/wiki/Divisor_function#Properties
		       (default 'brute')
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
		raise RuntimeError(''.join(['No implementation named ', str(method), 
		' found.']))


def getFactors(num, 
			   primeFactor=False, 
			   proper=False, 
			   nontrivial=False, 
			   method='brute'):
	"""Return a list of factors for the number given.

	Arguments:
	num 		-- intput number
	primeFactor	-- only return prime factors (default False)
	proper		-- only return proper divisors (default False)
	nontrivial	-- only return non-trivial divisors (default False)
	method		-- implementation, which includes brute-force 'brute' 
			 	   (default 'brute')
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
		raise RuntimeError(''.join(['No implementation named ', str(method), 
		' found.']))


def getAmicableNumbers(below, above=220, method='brute'):
	"""Return a list of amicable numbers.
	http://en.wikipedia.org/wiki/Amicable_numbers
	
	Arguments:
	below	-- smaller or equal to
	above	-- greater or equal to (default 220)
	method	-- implementation, which includes brute-force 'brute'
			   (default 'brute')
	"""
	if above < 0:
		raise ValueError('Perfect numbers must be positive integer.')
	if above > below:
		raise ValueError("'above' is greater than 'below'.")
	
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
		raise RuntimeError(''.join(['No implementation named ', str(method), 
		' found.']))

