# integer.py
# created by Kaiwen Xu
#
# module related with integers

import math


class IntegerNumber:
	"""Integer number generator (non-stop).
	"""
	def __init__(self, start=0):
		"""Arguments:
		start -- the number starts from (default 0)
		"""
		if isInt(start):
			self.gen = start
			self.start = start
		else:
			raise ValueError("Start number must be an integer.")

	def __iter__(self):
		return self

	def next(self):
		"""Return next integer.
		"""
		self.gen += 1
		return (self.gen - 1)

	def reset(self, start=None):
		"""Reset generator.

		Arguments:
		start -- if not set, reset to the start number which initialized with
				(default None)
		"""
		if start is None:
			self.gen = self.start
		else:
			if isInt(start):
				self.gen = start
				self.start = start
			else:
				raise ValueError("Start number must be an integer.")


class EvenNumber(IntegerNumber):

	def next(self):
		"""Return next even integer.
		"""
		self.gen += 2
		if not isEven(self.gen):
			self.gen += 1
		return (self.gen - 2)


class OddNumber(IntegerNumber):

	def next(self):
		"""Return next odd integer.
		"""
		self.gen += 2
		if not isOdd(self.gen):
			self.gen += 1
		return (self.gen - 2)


def isInt(f):
	try:
		i = int(f)
	except:
		return False
	if i == f:
		return True
	else:
		return False


def isSqrtInt(f):
	if isInt(f) and isInt(math.sqrt(f)):
		return True
	else:
		return False


def isEven(n):
	return n % 2 == 0


def isOdd(n):
	return n & 2 != 0


getBinStr = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]
