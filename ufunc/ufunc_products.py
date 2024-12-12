import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# ----------------- Product ----------------

print('Original :', arr1)

print('Product :', np.prod(arr1) )

print('Original :', arr1, arr2)

print('Product of two arrays:', np.prod([arr1, arr2]) )

# ----------------- Product Over an Axis ----------------

print('Original :', arr1, arr2)

print('Product :', np.prod([arr1, arr2], axis=0) )


# ----------------- Cummulative Product ----------------

print('Original :', arr2)

print('Cummulative Product :', np.cumprod(arr2) )


