# bigmath.py
# created by Kaiwen Xu
#
# module for calculating very large numbers

import math
import integer

def numToDigitArray(num):
	"""Return an array of int which represent the number by digit.
	'num' - number.
	"""
	if integer.isInt(num):
		digitArray = []
		strArray = str(num)
		for s in strArray:
			digitArray.append(int(s))
	
		return digitArray
	else:
		raise Exception("Error: number must be integer.")

def numToShortDigitArray(num, digitArray):
	length = len(digitArray)
	

def digitArrayToNum(digitArray):
	"""Return the number which the digitArray represents.
	'digitArray' - array of digits.
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

def bigpow(x, y, digits):
	rd = digits * [0]
	
