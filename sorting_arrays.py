import numpy as np

arr0 = np.array(42)                             # 0D - array
arr1 = np.array([1,387,5,7,0,11,23,15])         # 1D - array
arr2 = np.array([[12,3,57],[7,90,11]])             # 2D - array
arr3 = np.array([[[1,3,5],[7,9,11]],
                [[2,4,6],[8,10,12]]])           # 3D - array

arrStr = np.array(['banana', 'cherry', 'apple']) # Strings array

# ---------------- Sort 1-D array -------------------

print('\n Origin: ', arr1)

x = np.sort(arr1)

print('\n Sorted:', x )

# -------------------------------------

print('\n Origin: ', arrStr)

x = np.sort(arrStr)

print('\n Sorted:', x )

# ---------------- Sort 2-D array -------------------

print('\n Origin: ', arr2)

x = np.sort(arr2)

print('\n Sorted:', x )

# ---------------- Filtering arrays -------------------

print('\n Origin: ', arr1)

filter = [True, False, True, False, True, True, True, False]

x = arr1[filter]

print('\n Filtered:', x )

# ---------------- Creating the Filter Array -------------------

filter = []

for element in arr1:
    if element > 10:
        filter.append(True)
    else:
        filter.append(False)

x = arr1[filter]

print('\n Origin: ', arr1)

print('\n Filtered (>10):', x )

# ---------------- Creating Filter Directly From Array -------------------

filter = arr1 > 15

print('\n Origin: ', arr1)
print('Filter > 15: ', filter)
print('Filter > 0: ',arr1 > 0)
print('Filter % 5: ',arr1 % 5 == 0)





""" sec = 7623
print (sec//3600, ' ', (sec%3600)//60, ' ', sec%60) """