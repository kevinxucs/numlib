from time import clock
from numlib.prime import getPrimes

def diff(a, b):
	b = set(b)
	return [aa for aa in a if aa not in b]

def testBrute(num, above=2):
	st = clock()
	pl = getPrimes(num, above, method='brute')
	print repr(num) + ' brute time: ' + repr(clock() - st)
	return pl

def testErato(num, above=2):
	st = clock()
	pl = getPrimes(num, above, method='erato')
	print repr(num) + ' erato time: ' + repr(clock() - st)
	return pl

def testAtkin(num, above=2):
	st = clock()
	pl = getPrimes(num, above, method='atkin')
	print repr(num) + ' atkin time: ' + repr(clock() - st)
	return pl

def test(num, above=2):
	print 'Test above ' + repr(above) + ' below ' + repr(num)
	p1 = testBrute(num, above)
	p2 = testErato(num, above)
	p3 = testAtkin(num, above)
	if p1 == p2 and p2 == p3:
		print 'Same'
	else:
		print 'Different'
		#print 'p1 - p2 = ' + repr(diff(p1, p2))
		#print 'p2 - p1 = ' + repr(diff(p2, p1))

#test(20000)
#test(200000)
#test(2000000)
#test(4000000, 2000000)
#test(4000000)
testErato(20000000)
testAtkin(20000000)