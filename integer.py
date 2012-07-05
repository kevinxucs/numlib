# integer.py
# created by Kaiwen Xu
# 
# module for calculating integers

def isInt(f):
	i = int(f)
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