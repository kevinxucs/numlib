# fibon.py
# created by Kaiwen Xu
#
# module for calculating Fibonacci number


class FibonNumber():
	"""Fibonacci number generator (non-stop).
	"""
	def __init__(self, seed1=0, seed2=1):
		self.s1 = seed1
		self.s2 = seed2
		self.seed1 = seed1
		self.seed2 = seed2

	def __iter__(self):
		return self

	def next(self):
		s1 = self.s1
		s2 = self.s2
		self.s2 = s1 + s2
		self.s1 = s2
		return s1

	def reset(self, seed1=None, seed2=None):
		if seed1 is None:
			self.s1 = self.seed1
		else:
			self.s1 = seed1
			self.seed1 = seed1

		if seed2 is None:
			self.s2 = self.seed2
		else:
			self.s2 = seed2
			self.seed2 = seed2
