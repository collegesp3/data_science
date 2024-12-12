import numpy as np

# ------------------ Create Sets ----------------

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

print('Original: ', arr)
print('Set :', np.unique(arr))

# ------------------ Finding Union ----------------

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print('Original: ', arr1, arr2)
print('Union :', np.union1d(arr1, arr2))

# ------------------ Finding Intersection ----------------

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print('Original: ', arr1, arr2)
print('Intersection :', np.intersect1d(arr1, arr2, assume_unique=True))


# ------------------ Finding Symmetric Difference ----------------

print('Original: ', arr1, arr2)
print('Symmetric Difference :', np.setxor1d(arr1, arr2, assume_unique=True))

