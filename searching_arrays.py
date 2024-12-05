import numpy as np

arr0 = np.array(42)
arr1 = np.array([1,2,3,4,5,6,7,4])
arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# --------------- Searching Arrays -------------------

x = np.where(arr1 == 4)

print('Indexes are: ', x)
print(x[0][1])

x = np.where(arr1%2 == 0)
print('Even indexes (%2==0) are: ', x)

x = np.where(arr1%2 == 1)
print('Odd indexes (%2==1) are: ', x)


# --------------- Search Sorted -------------------

x = np.searchsorted(arr1, 3, side='right')

print('Original :', arr1)
print('Searchsorted: ', x)

x = np.searchsorted(arr1, [2,4,6]) 
print('Multiple Values: ', x)
