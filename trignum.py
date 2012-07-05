# integer.py
# created by Kaiwen Xu
# 
# module for calculating triangle numbers

from math import sqrt

class TriangleNumber:
	n = 0
	add = 1
	def next(self):
		self.n += self.add
		self.add += 1
		return self.n
	
	def reset(self):
		self.n = 0
		self.add = 1
	

def isTriangleNumber(n):
	delta = sqrt(8 * n + 1)
	if isInt(delta):
		x = (delta / 2) - 0.5
		if isInt(x) and x > 0:
			return int(x)
	else:
		return False
