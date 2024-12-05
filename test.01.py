#import numpy as np
#print(np.random.random())
#import re
#match = re.match('Hello[ \t]*(.*)world', 'Hello    Python world')
#match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
#print(match.groups())
"""   ------------------ File operations -------------------
f = open('data.txt', 'w')
f.write('This file was created by Python code')
f.close()

f = open('data.txt')
text = f.read()

print(text.split())
f.close()
"""

""" --------------------- Fractions ---------------------------
from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(3 ,4)
z = Fraction ('1.25')

print(x + y)
print(z)
"""

""" --------------------- Decimals ---------------------------
"""
#from decimal import Decimal
""" import decimal

x =  decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3')

decimal.getcontext().prec = 3
y =  decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) -decimal.Decimal(0.3)

print(x)
print(y) """

# --------------------- NumPy data types ---------------------
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)

arrChar = np.array(['apple', 'banana', 'cherry'])
print(arrChar.dtype)

arrS = np.array([1,2,3,4], dtype = 'S')
print(arrS.dtype)

arrI4 = np.array([1, 2, 3, 4], dtype='i4')

print(arrI4)
print(arrI4.dtype)

arrFloat = np.array([1.1, 2.1, 3.1])
newarrInt = arrFloat.astype('i')

print(newarrInt)
print(newarrInt.dtype)


xCopy = arr.copy()
xView = arr.view()
arr[0] = 42
xView[1] = 31

print(arr)
print('Copy: ',xCopy, ', base: ', xCopy.base)
print('View: ',xView, ', base: ', xView.base)

arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr2d)
print('Array shape: ',arr2d.shape)

arr5d = np.array([1, 2, 3, 4], ndmin = 5)
print('arr5d shape: ', arr5d.shape)

print(type(arr5d.shape))

# -------------------- reshaping arrays -------------------------

arrLong = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arrLongReshaped = arrLong.reshape(4, 3)

print('arrLong: ', arrLong)
print('arrLongReshaped :', arrLongReshaped)
print('arrLongReshaped base: ', arrLongReshaped.base)

arrLongReshapedUnknownDim = arrLong.reshape(2, 3, -1)
print('arrLongReshapedUnknownDim :', arrLongReshapedUnknownDim)


print('Flattered arrLongReshaped: ', arrLongReshaped.reshape(-1))

