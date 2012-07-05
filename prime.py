# prime.py
# created by Kaiwen Xu
# 
# module for calculating primes

from math import sqrt

class PrimeNumber:
	gen = 2
	def next(self):
		while not isPrime(self.gen):
			self.gen += 1
		else:
			self.gen += 1
			return (self.gen - 1)
	
	def reset(self):
		self.gen = 2
	

def isPrime(n):
	if n > 1:
		sqrtN = int(sqrt(n))
		for i in xrange(2, sqrtN + 1):
			if n % i == 0:
				return False
		return True
	else:
		return False

def genNumPrimeList(num):
	i = 0
	p = PrimeNumber()
	list = []
	while i < num:
		list.append(p.next())
		i += 1
	else:
		return list

# 'below' means less than or equal to.
# 'above' means greater or equal to.
# implementation includes brute-force 'brute', sieve of eratosthenes 'erato',
# sieve of atkin 'atkin'.
# suitable cases:
# small prime list start from large number - brute
# small and medium prime list - erato
# large prime list - atkin
# 
# uses sieve of eratosthenes by default.
def getPrimes(below, above=2, method='erato'):
	if above < 2:
		raise Exception('Prime numbers must be greater or equal to 2.')
	elif above >= below:
		raise Exception("Error: 'above' is greater or equal to 'below'.")
	
	if method == 'brute':
		return filter(isPrime, range(above, below + 1))
	elif method == 'erato':
		result = []
		listlen = below + 1
		mask = listlen * [True]
		mask[0] = False
		mask[1] = False
		for i in xrange(0, listlen):
			if mask[i] == True:
				rm = 2 * i
				while rm <= below:
					if mask[rm] == True:
						mask[rm] = False
					rm += i
		for i in xrange(above, listlen):
			if mask[i] == True:
				result.append(i)
		return result
	elif method == 'atkin':
		result = []
		listlen = below + 1
		sqrtlimit = int(sqrt(below)) + 1
		mask = listlen * [False]
		mask[2] = True
		mask[3] = True
		for x in xrange(1, sqrtlimit):
			for y in xrange(1, sqrtlimit):
				n = 4 * x * x + y * y
				if n <= below and (n % 12 == 1 or n % 12 == 5):
					mask[n] = not mask[n]
				n = 3 * x * x + y * y
				if n <= below and (n % 12 == 7):
					mask[n] = not mask[n]
				n = 3 * x * x - y * y
				if x > y and n <= below and n % 12 == 11:
					mask[n] = not mask[n]
		for n in xrange(5, sqrtlimit):
			if mask[n] == True:
				for k in xrange(n * n, listlen, n * n):
					mask[k] = False
		for i in xrange(above, listlen):
			if mask[i] == True:
				result.append(i)
		return result
	else:
		raise Exception('No implementation named ' + repr(method) +  ' found.')
