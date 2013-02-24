# prime.py
# created by Kaiwen Xu
# 
# module for calculating primes

import math
import integer

# Prime number generator (non-stop)
class PrimeNumber:

	def __init__(self, start=2):
		"""Arguments:
		start -- the number starts from (default 2)
		"""
		if integer.isInt(start) and start >= 2:
			self.gen = start
			self.start = start
		else:
			raise ValueError('Start number must be an integer and not less than 2.')
	
	def __iter__(self):
		return self
	
	def next(self):
		"""Return next prime number.
		"""
		while not isPrime(self.gen):
			self.gen += 1
		else:
			self.gen += 1
			return (self.gen - 1)
	
	def reset(self, start=None):
		"""Reset generator.

		Arguments:
		start -- if not set, reset to the start number which initialized with
				 (default None)
		"""
		if start is None:
			self.gen = self.start
		else:
			if integer.isInt(start) and start >= 2:
				self.gen = start
				self.start = start
			else:
				raise ValueError('Start number must be an integer and not less than 2.')


def isPrime(n):
	"""Checking whether the number is prime.

	Arguments:
	n -- input number
	"""
	if n > 1:
		sqrtN = int(math.sqrt(n))
		for i in xrange(2, sqrtN + 1):
			if n % i == 0:
				return False
		return True
	else:
		return False


def isCircularPrime(n):
	"""Checking whether the number is circular prime.

	Arguments:
	n -- input number
	"""
	strnum = str(n)
	strlen = len(strnum)
	for st in xrange(1, strlen + 1):
		num = int(strnum[st:] + strnum[:st])
		if not isPrime(num):
			return False
	else:
		return True


def getNumPrimes(num):
	"""Return a list which contains specific amount of primes.

	Arguments:
	num -- amount of primes
	"""
	i = 0
	p = PrimeNumber()
	list = []
	
	while i < num:
		list.append(p.next())
		i += 1
	else:
		return list


def getPrimes(below, above=2, method='erato'):
	"""Return a list of primes.

	Arguments:
	below	-- less than or equal to
	above	-- greater or equal to (default 2)
	method	-- implementation, which includes brute-force 'brute', 
			   sieve of eratosthenes 'erato', sieve of atkin 'atkin'
			   (default 'erato')
	
	Suitable cases:
	'brute'	-- small prime list start from large number
	'erato'	-- small and medium prime list
	'atkin'	-- large prime list
	"""
	if above < 2:
		raise ValueError('Prime numbers must be greater or equal to 2.')
	elif above > below:
		raise ValueError("'above' is greater than 'below'.")
	
	if method == 'brute':
		return filter(isPrime, range(above, below + 1))
	
	elif method == 'erato':
		result = []
		listlen = below + 1
		mask = listlen * [True]
		mask[0] = False
		mask[1] = False
		for i in xrange(0, listlen):
			if mask[i]:
				rm = 2 * i
				while rm <= below:
					if mask[rm]:
						mask[rm] = False
					rm += i
		for i in xrange(above, listlen):
			if mask[i]:
				result.append(i)
		return result
	
	elif method == 'atkin':
		return getPrimesAtkin(below, above, False)
	
	else:
		raise RuntimeError(''.join(['No implementation named ', str(method), ' found.']))


def getPrimesAtkin(below, above=2, thread=False):
	"""Sieve of atkin implementation of getPrimes.

	Arguments:
	below	-- less than or equal to
	above	-- greater or equal to (default 2)
	thread	-- enable thread (default False)

	NOTICE:
	Threading has been removed. This function will do exactly the same thing,
	no matter what thread argument is.
	"""
	result = []
	listlen = below + 1
	sqrtlimit = int(math.sqrt(below)) + 1
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
		if mask[n]:
			for k in xrange(n * n, listlen, n * n):
				mask[k] = False
	for i in xrange(above, listlen):
		if mask[i]:
			result.append(i)
	return result

