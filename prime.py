# prime.py
# created by Kaiwen Xu
# 
# module for calculating primes

import math

# Prime number generator
class PrimeNumber:
	def __init__(self, start=2):
		"""'start' - the number start from. 2 by default.
		"""
		if start >= 2:
			self.gen = start
		else:
			raise Exception('Prime number must be greater than 2.')
	
	def __iter__(self):
		return self
	
	def next(self):
		"""Get next prime number.
		"""
		while not isPrime(self.gen):
			self.gen += 1
		else:
			self.gen += 1
			return (self.gen - 1)
	
	def reset(self, start=2):
		"""Reset generator.
		'start' - the number start from. 2 by default.
		"""
		if start >= 2:
			self.gen = start
		else:
			raise Exception('Prime number must be greater than 2.')
	

def isPrime(n):
	"""Checking whether the number is prime or not.
	'n' - number.
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
	"""Checking whether the number is circular prime or not.
	'n' - number.
	"""
	strnum = str(n)
	strlen = len(strnum)
	for st in xrange(1, strlen + 1):
		num = int(strnum[st:] + strnum[:st])
		if isPrime(num) == False:
			return False
	else:
		return True


def getNumPrimes(num):
	"""Return a list which contains specific amount of primes.
	'num' - amount of primes.
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
	'below' - less than or equal to.
	(optional) 'above' - greater or equal to. 'above' is 2 by default.
	(optional) 'method' - implementation, which includes 
	brute-force 'brute', sieve of eratosthenes 'erato', 
	sieve of atkin 'atkin'.
	
	Suitable cases:
	small prime list start from large number - brute
	small and medium prime list - erato
	large prime list - atkin
	 
	Uses sieve of eratosthenes if no parameter for 'method' provided.
	"""
	if above < 2:
		raise Exception('Prime numbers must be greater or equal to 2.')
	elif above > below:
		raise Exception("Error: 'above' is greater than 'below'.")
	
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
		return getPrimesAtkin(below, above, False)
	
	else:
		raise Exception('No implementation named ' + repr(method) + ' found.')

def getPrimesAtkin(below, above=2, thread=False):
	"""Sieve of atkin implementation of getPrimes.
	'below' - less than or equal to.
	(optional) 'above' - greater or equal to. 'above' is 2 by default.
	(optional) 'thread' - enable thread or not. It's disable by default. 
	NOTICE: Threading support is totally experimental. And it seems like 
	slower than non-threaded version.
	"""
	result = []
	listlen = below + 1
	sqrtlimit = int(math.sqrt(below)) + 1
	mask = listlen * [False]
	mask[2] = True
	mask[3] = True
	
	if thread == False:
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
	
	else:
		import threading
		class Thread1(threading.Thread):
			def __init__(self, mask, sqrtlimit):
				threading.Thread.__init__(self)
				self.mask = mask
				self.sqrtlimit = sqrtlimit
			
			def run(self):
				for x in xrange(1, self.sqrtlimit):
					for y in xrange(1, self.sqrtlimit):
						n = 4 * x * x + y * y
						if n <= below and (n % 12 == 1 or n % 12 == 5):
							self.mask[n] = not self.mask[n]
			
		
		class Thread2(threading.Thread):
			def __init__(self, mask, sqrtlimit):
				threading.Thread.__init__(self)
				self.mask = mask
				self.sqrtlimit = sqrtlimit

			def run(self):
				for x in xrange(1, self.sqrtlimit):
					for y in xrange(1, self.sqrtlimit):
						n = 3 * x * x + y * y
						if n <= below and (n % 12 == 7):
							self.mask[n] = not self.mask[n]
			
		
		class Thread3(threading.Thread):
			def __init__(self, mask, sqrtlimit):
				threading.Thread.__init__(self)
				self.mask = mask
				self.sqrtlimit = sqrtlimit

			def run(self):
				for x in xrange(1, self.sqrtlimit):
					for y in xrange(1, self.sqrtlimit):
						n = 3 * x * x - y * y
						if x > y and n <= below and n % 12 == 11:
							self.mask[n] = not self.mask[n]
			
		
		t1 = Thread1(mask, sqrtlimit)
		t2 = Thread2(mask, sqrtlimit)
		t3 = Thread3(mask, sqrtlimit)
		t1.start()
		t2.start()
		t3.start()
		t1.join()
		t2.join()
		t3.join()
	
	for n in xrange(5, sqrtlimit):
		if mask[n] == True:
			for k in xrange(n * n, listlen, n * n):
				mask[k] = False
	for i in xrange(above, listlen):
		if mask[i] == True:
			result.append(i)
	return result
