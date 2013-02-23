# integer.py
# created by Kaiwen Xu
# 
# module related with integers

# Integer generator (non-stop)
class IntegerNumber:

	def __init__(self, start=0):
		"""'start' - the number starts from. 0 by default.
		"""
		if isInt(start):
			self.gen = start
			self.start = start
		else:
			raise ValueError("Start number must be an integer.") 

	def __iter__(self):
		return self

	def next(self):
		"""Get next integer.
		"""
		self.gen += 1
		return (self.gen - 1)

	def reset(self, start=None):
		"""Reset generator.
		'start' - if not set, reset to the start number which initialized with.
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
		"""Get next even integer.
		"""
		self.gen += 2
		if not isEven(self.gen):
			self.gen += 1
		return (self.gen - 2)


class OddNumber(IntegerNumber):

	def next(self):
		"""Get next odd integer.
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
	if isInt(f) and isInt(sqrt(f)):
		return True
	else:
		return False


def isEven(n):
	if n % 2 == 0:
		return True
	else:
		return False


def isOdd(n):
	return not isEven(n)


getBinStr = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

