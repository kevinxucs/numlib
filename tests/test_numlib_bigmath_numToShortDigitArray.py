from numlib.bigmath import numToShortDigitArray

da = 5 * [0]
print da
numToShortDigitArray(123456789, da)
print da