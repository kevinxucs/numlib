from numlib.factor import getFactors

print("284: " + str(getFactors(284, primeFactor=False, proper=True, nontrivial=False)))
print("644: " + str(getFactors(644, primeFactor=True, proper=False, nontrivial=False)))
print("645: " + str(getFactors(645, primeFactor=True, proper=False, nontrivial=False)))
print("646: " + str(getFactors(646, primeFactor=True, proper=False, nontrivial=False)))