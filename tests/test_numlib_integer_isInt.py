from numlib.integer import isInt

print("1: " + repr(isInt(1)))
print("12341234123423512351236512351234213412512351234123412341: " + repr(isInt(12341234123423512351236512351234213412512351234123412341)))
print("1.1: " + repr(isInt(1.1)))
print("3.1231231231242341235235123512345234123512351235123412: " + repr(isInt(3.1231231231242341235235123512345234123512351235123412)))
print("'123123123131231231231231231': " + repr(isInt('123123123131231231231231231')))
print("'1312321312safsdfsafasdfa': " + repr(isInt('1312321312safsdfsafasdfa')))
print("[1]: " + repr(isInt([1])))
print("[1, 1213123, 'asdfas']: " + repr(isInt([1, 1213123, 'asdfas'])))
print("{1}: " + repr(isInt({1})))
print("{1: 1}: " + repr(isInt({1: 1})))
