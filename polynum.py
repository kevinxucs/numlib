# integer.py
# created by Kaiwen Xu
# 
# module for calculating polygonal numbers

import math
import integer

class TriangleNumber:
	def __init__(self):
		self.n = 0
		self.add = 1
	
	def __iter__(self):
		return self
	
	def next(self):
		self.n += self.add
		self.add += 1
		return self.n
	
	def reset(self):
		self.n = 0
		self.add = 1
	

def getTriangleNumber(n):
	"""Get n-th triangle number.
	"""
	return int(n * (n + 1) / 2)


def isTriangleNumber(n):
	"""Determine whether is triangle number.
	'n' - number.
	"""
	delta = math.sqrt(8 * n + 1)
	if integer.isInt(delta):
		x = (delta / 2) - 0.5
		if integer.isInt(x) and x > 0:
			return int(x)
	else:
		return False
