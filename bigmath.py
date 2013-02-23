# bigmath.py
# created by Kaiwen Xu
#
# module for calculating very large numbers

import math
import integer

def numToDigitArray(num):
	"""Return an array of int which represent the number by digit.

	Arguments:
	num -- input number
	"""
	if integer.isInt(num):
		digitArray = []
		strArray = str(num)
		for s in strArray:
			digitArray.append(int(s))
	
		return digitArray
	else:
		raise ValueError("Number must be integer.")


def numToShortDigitArray(num, digitArray):
	"""Parse number into provided digitArray. If the length of digitArray is
	smaller than the length of num, then only last fitable digits will be 
	filled into the array.

	Arguments:
	num			-- input number
	digitArray	-- digit array that needed to be filled
	"""
	if integer.isInt(num):
		strArray = str(num)
		rStrArray = strArray[::-1]
		numLength = len(strArray)
		digitLength = len(digitArray)
		for i in xrange(0, numLength):
			if i < digitLength:
				digitArray[digitLength - i - 1] = int(rStrArray[i])
	else:
		raise ValueError("Number must be integer.")


def digitArrayToNum(digitArray):
	"""Return the number which the digitArray represents.

	Arguments:
	digitArray -- array of digits
	"""
	num = 0
	length = len(digitArray)
	power = length - 1
	for d in digitArray:
		if d > 9 or d < 0:
			raise Exception("Error: digits must be 0, 1, ... , 9.")
		else:
			num += d * pow(10, power)
			power -= 1
	
	return num


def bigpow(x, y):
	"""Return x ^ y.
	"""
	total = 1
	for c in xrange(0, y):
		total *= x
	
	return total


def digFromFractGenerator(numerator, denominator):
	"""Return a generator of digits from a fraction, only digits after decimal
	point are generated.

	Arguments:
	numerator	-- numerator of fraction
	denominator	-- denominator of fraction
	"""
	if numerator > denominator:
		numerator = numerator % denominator
	
	while numerator != 0:
		numerator = numerator * 10
		yield int(numerator/denominator)
		numerator = numerator % denominator

