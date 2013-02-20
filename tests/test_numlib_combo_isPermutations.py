from numlib.combo import isPermutations

lst1 = ['123', '321', '132', '213']
lst2 = [123, 321, 132, 213]
lst3 = ['123', '321', '132', 213]
lst4 = ['123', '321', '132', '213', 412]
lst5 = ['123', '321', '132', '213', '412']
lst6 = [123, 321, 132, 213, 412]
lst7 = [123, 321, 132, 213, '412']
lst8 = [123, 321, 132, '213']
lst9 = ["123", "321", "132", "213"]

print(repr(lst1) + ": " + repr(isPermutations(lst1)))
print(repr(lst2) + ": " + repr(isPermutations(lst2)))
print(repr(lst3) + ": " + repr(isPermutations(lst3)))
print(repr(lst4) + ": " + repr(isPermutations(lst4)))
print(repr(lst5) + ": " + repr(isPermutations(lst5)))
print(repr(lst6) + ": " + repr(isPermutations(lst6)))
print(repr(lst7) + ": " + repr(isPermutations(lst7)))
print(repr(lst8) + ": " + repr(isPermutations(lst8)))
print(repr(lst9) + ": " + repr(isPermutations(lst9)))