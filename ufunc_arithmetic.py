import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# ------------- Addition -----------------

newarr = np.add(arr1, arr2)

print('Addition :', newarr)

# ------------- Subtraction -----------------

newarr = np.subtract(arr1, arr2)

print('Subtraction :', newarr)

# ------------- Multiplication -----------------

newarr = np.multiply(arr2, arr1)

print('Multiplication :', newarr)

# ------------- Division -----------------

newarr = np.divide(arr1, arr2)

print('Division :', newarr)

# ------------- Power -----------------

newarr = np.power(arr1, arr2)

print('Power :', newarr)


# ------------- Remainder -----------------

newarr = np.mod(arr2, arr1)

print('Remainder :', newarr)

# ------------- Quotient and Mod -----------------

newarr = np.divmod(arr2, arr1)

print('Quotient and Mod :', newarr)

# ------------- Absolute Values -----------------

newarr = np.absolute([-1, -2, 1, 2, 3, -4])

print('Absolute Values :', newarr)