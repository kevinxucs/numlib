from time import clock
from numlib.prime import getPrimesAtkin

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
	r1 = testNonTread(below)
	r2 = testThread(below)
	if r1 == r2:
		print 'same'
	else:
		print 'different'

test(2000000)
test(20000000)