# combo.py
# created by Kaiwen Xu
#
# module related with combinatorics
import operator


def isPermutations(lst):
	"""Check whether numbers in the given list are permutations.

	Arguments:
	lst -- list of numbers
	"""
	length = 0
	elements = {}
	for i in xrange(0, len(lst)):
		num = str(lst[i])
		if i == 0:
			length = len(num)
			for digit in num:
				if digit not in elements:
					elements[digit] = 1
				else:
					elements[digit] += 1
		else:
			if len(num) != length:
				return False
			else:
				e = {}
				for digit in num:
					if digit not in e:
						e[digit] = 1
					else:
						e[digit] += 1
				else:
					if e != elements:
						return False
	else:
		return True


def nCk(n, k):
	"""n choose k.
	"""
	return int(round(reduce(operator.mul, (float(n - i) / (i + 1) for i in xrange(k)), 1)))
