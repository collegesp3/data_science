import numpy as np

num1 = 4
num2 = 6
arr1 = np.array([3, 6, 9])
arr2 = np.arange(1, 11)

# -------------- Finding LCM (Lowest Common Multiple) ---------

print('Original :', num1, num2)

print('Lowest Common Multiple :', np.lcm(num1, num2))


# -------------- Finding LCM in Arrays ---------

print('Original :', arr1)

print('Array Lowest Common Multiple :', np.lcm.reduce(arr1))

print('Original :', arr2)

print('Array Lowest Common Multiple :', np.lcm.reduce(arr2))



