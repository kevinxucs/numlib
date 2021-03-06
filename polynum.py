# polynum.py
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

	@classmethod
	def getTriangleNumber(self, n):
		"""Return n-th triangle number.

		Arguments:
		n -- input number
		"""
		return int(n * (n + 1) / 2)

	@classmethod
	def isTriangleNumber(self, n):
		"""Determine whether is triangle number.
		Return False if 'n' is not triangle number,
		else return the position of
		'n' in the triangle number sequence.

		Arguments:
		n -- input number
		"""
		delta = math.sqrt(8 * n + 1)
		if integer.isInt(delta):
			x = (delta / 2) - 0.5
			if integer.isInt(x) and x > 0:
				return int(x)
		else:
			return False


class PentagonalNumber:

	def __init__(self):
		self.n = 0
		self.add = 1

	def __iter__(self):
		return self

	def next(self):
		self.n += self.add
		self.add += 3
		return self.n

	def reset(self):
		self.n = 0
		self.add = 1

	@classmethod
	def getPentagonalNumber(self, n):
		"""Return n-th pentagonal number.

		Arguments:
		n -- input number
		"""
		return int(n * (3 * n - 1) / 2)

	@classmethod
	def isPentagonalNumber(self, n):
		"""Determine whether n is pentagonal number.
		Return False if 'n' is not pentagonal number,
		else return the position of
		'n' in the pentagonal number sequence.

		Arguments:
		n -- input number
		"""
		delta = math.sqrt(24 * n + 1)
		if integer.isInt(delta):
			x = (delta + 1) / 6
			if integer.isInt(x) and x > 0:
				return int(x)
		else:
			return False


class HexagonalNumber:

	def __init__(self):
		self.n = 0
		self.add = 1

	def __iter__(self):
		return self

	def next(self):
		self.n += self.add
		self.add += 4
		return self.n

	def reset(self):
		self.n = 0
		self.add = 1

	@classmethod
	def getHexagonalNumber(self, n):
		"""Return n-th hexagonal number.

		Arguments:
		n -- input number
		"""
		return int(n * (2 * n - 1))

	@classmethod
	def isHexagonalNumber(self, n):
		"""Determine whether n is hexagonal number.
		Return False if 'n' is not hexagonal number,
		else return the position of 'n' in the hexagonal number sequence.

		Arguments:
		n -- input number
		"""
		delta = math.sqrt(8 * n + 1)
		if integer.isInt(delta):
			x = (delta + 1) / 4
			if integer.isInt(x) and x > 0:
				return int(x)
		else:
			return False
