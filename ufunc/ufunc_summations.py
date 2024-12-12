import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)

# ------------- Summation --------------

print('Original :', arr1, arr2)

print('Sum :', np.sum([arr1, arr2]) )
print('Sum :', np.sum([arr1]) )


# ------------- Summation Over an Axis --------------

print('Original :', arr1, arr2)

print('Sum Over an Axe 0:', np.sum([arr1, arr2], axis=0) )
print('Sum Over an Axe 1:', np.sum([arr1, arr2], axis=1) )


# ------------- Cummulative Sum --------------

print('Original :', arr1)

print('Cummulative Sum:', np.cumsum(arr1) )