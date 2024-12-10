import numpy as np

num1 = 9
num2 = 6
arr1 = np.array([20, 8, 32, 36, 16])
arr2 = np.arange(1, 11)

# -------------- Finding GCD (Greatest Common Denominator) ---------

print('Original :', num1, num2)

print('Greatest Common Denominator :', np.gcd(num1, num2))

print('Original :', arr1)

print('Greatest Common Denominator :', np.gcd.reduce(arr1))

