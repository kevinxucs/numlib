import math
from time import clock
from numlib.prime import getPrimesAtkin

def testEmpty(below):
	st = clock()
	print 'Test Empty Loop below', below
	listlen = below + 1
	mask = listlen * [False]
	mask[2] = True
	mask[3] = True
	sqrtlimit = int(math.sqrt(below)) + 1
	for x in xrange(1, sqrtlimit):
		for y in xrange(1, sqrtlimit):
			pass
	for n in xrange(5, sqrtlimit):
		pass
	print 'Total Time:', clock() - st


def testNonTread(below):
	st = clock()
	print 'Testing Non-Thread below ' + repr(below)
	result = getPrimesAtkin(below, thread=False)
	print 'Total Time: ' + str(clock() - st) + 's'
	return result


def testThread(below):
	st = clock()
	print 'Testing Thread below ' + repr(below)
	result = getPrimesAtkin(below, thread=True)
	print 'Total Time: ' + str(clock() - st) + 's'
	return result


def test(below):
	testEmpty(below)
	r1 = testNonTread(below)
	r2 = testThread(below)
	if r1 == r2:
		print 'same'
	else:
		print 'different'


if __name__ == '__main__':
	test(2000000)
	test(20000000)