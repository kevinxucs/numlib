# prime.py
# created by Kaiwen Xu
# 
# module for calculating primes

import math

class PrimeNumber:
	def __init__(self, start=2):
		if start >= 2:
			self.gen = start
		else:
			raise Exception('Prime number must be greater than 2.')
	
	def __iter__(self):
		return self
	
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
		sqrtN = int(math.sqrt(n))
		for i in xrange(2, sqrtN + 1):
			if n % i == 0:
				return False
		return True
	else:
		return False

def getNumPrimeList(num):
	i = 0
	p = PrimeNumber()
	list = []
	
	while i < num:
		list.append(p.next())
		i += 1
	else:
		return list

def getPrimes(below, above=2, method='erato'):
	"""return a list of primes.
	'below' means less than or equal to.
	(optional) 'above' means greater or equal to. 'above' is 2 by default.
	(optional) 'method' means implementation, which includes 
	brute-force 'brute', sieve of eratosthenes 'erato', 
	sieve of atkin 'atkin'.
	
	suitable cases:
	small prime list start from large number - brute
	small and medium prime list - erato
	large prime list - atkin
	 
	uses sieve of eratosthenes if no parameter for 'method' provided.
	"""
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
		return getPrimesAtkin(below, above, False)
	
	else:
		raise Exception('No implementation named ' + repr(method) + ' found.')

def getPrimesAtkin(below, above=2, thread=False):
	"""sieve of atkin implementation of getPrimes.
	'below' means less than or equal to.
	(optional) 'above' means greater or equal to. 'above' is 2 by default.
	(optional) 'thread' means enable thread or not. It's disable by default. 
	NOTICE: threading support is totally experimental.
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
