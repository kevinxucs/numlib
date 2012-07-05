# turns out checking prime by generating a list of prime is impractical

from time import clock
from numlib.prime import getPrimes, isPrime

def diff(a, b):
	b = set(b)
	return [aa for aa in a if aa not in b]

def testBrute(num):
	st = clock()
	r = isPrime(num)
	print repr(num) + ' brute time: ' + repr(clock() - st)
	return r

def testErato(num):
	st = clock()
	pl = getPrimes(num + 1, method='erato')
	print repr(num) + ' erato time: ' + repr(clock() - st)
	if num in pl:
		return True
	else:
		return False

def test(num):
	p1 = testBrute(num)
	print p1
	p2 = testErato(num)
	print p2
	if p1 == p2:
		print 'Same'
	else:
		print 'Different'

test(9999991)