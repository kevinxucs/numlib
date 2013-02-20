# combo.py
# created by Kaiwen Xu
#
# module related with combinatorics

def isPermutations(lst):
	"""Check whether numbers in the given list are permutations.
	'lst' - list of numbers.
	"""
	length = 0
	elements = set()
	for i in xrange(0, len(lst)):
		num = str(lst[i])
		if i == 0:
			length = len(num)
			for digit in num:
				elements.add(digit)
		else:
			if len(num) != length:
				return False
			for digit in num:
				if digit not in elements:
					return False
	else:
		return True
