import numpy as np

arr1 = np.array([1, 20, 32, 4])
arr2 = np.array([5, 6, 7, 8])

# ----------------- Discrete difference ----------------

print('Original :', arr1)

print('Discrete difference (n=1) :', np.diff(arr1) )

print('Discrete difference (n=2) :', np.diff(arr1, n=2) )