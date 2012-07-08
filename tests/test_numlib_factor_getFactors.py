from numlib.factor import getFactors

def testProper(n):
	return getFactors(n, primeFactor=False, proper=True)

print testProper(284)