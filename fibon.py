# fibon.py
# created by Kaiwen Xu
# 
# module for calculating Fibonacci number

class FibonNumber():
	def __init__(self, seed1=0, seed2=1):
		self.s1 = seed1
		self.s2 = seed2
	
	def __iter__(self):
		return self
	
	def next(self):
		s1 = self.s1
		s2 = self.s2
		self.s2 = s1 + s2
		self.s1 = s2
		return s1
	
	def reset(self, seed1=0, seed2=1):
		self.s1 = seed1
		self.s2 = seed2
	
