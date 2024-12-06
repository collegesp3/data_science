import numpy as np

arr0 = np.array(42)                     # 0D - array
arr1 = np.array([1,3,5,7,9,11,13,15])   # 1D - array
arr2 = np.array([[1,3,5],[7,9,11]])     # 2D - array
arr3 = np.array([[[1,3,5],[7,9,11]],
                [[2,4,6],[8,10,12]]])   # 3D - array

# --------------- Iterating arrays -------------------------

print('Iterating 1-D array:')

for x in arr1:   
    print(x)


print('Iterating 2-D array:')

for x in arr2:   
    print(x)

print('Actuals scalars of 2-D array:')

for x in arr2:  
    print('')
    for y in x: 
     print(y, end=' - ')


print('Iterating array using nditer():')

for x in np.nditer(arr3):   
    print(x)


# ------------------ Iterating Array With Different Data Types --------------

print('Iterating Array With Different Data Types:')

for x in np.nditer(arr1, flags=['buffered'], op_dtypes=['S']):
   print(x)


# ------------------ Iterating With Different Step Size --------------

print('Iterating Array With Different Data Types:')

for x in np.nditer(arr2[:, ::2]):
   print(x)


# ------------------ Enumerated Iteration Using ndenumerate() --------------

print('Iterating Array With Different Data Types:')

for idx, x in np.ndenumerate(arr2):
  print(idx, x)


import numpy as np

arr0 = np.array(42)                     # 0D - array
arr1 = np.array([1,3,5,7,9,11,13,15])   # 1D - array
arr2 = np.array([[1,3,5],[7,9,11]])     # 2D - array
arr3 = np.array([[[1,3,5],[7,9,11]],
                [[2,4,6],[8,10,12]]])   # 3D - array

# --------------- Iterating arrays -------------------------

print('Iterating 1-D array:')

for x in arr1:   
    print(x)


print('Iterating 2-D array:')

for x in arr2:   
    print(x)

print('Actuals scalars of 2-D array:')

for x in arr2:  
    print('')
    for y in x: 
     print(y, end=' - ')


print('Iterating array using nditer():')

for x in np.nditer(arr3):   
    print(x)


# ------------------ Iterating Array With Different Data Types --------------

print('Iterating Array With Different Data Types:')

for x in np.nditer(arr1, flags=['buffered'], op_dtypes=['S']):
   print(x)


# ------------------ Iterating With Different Step Size --------------

print('Iterating Array With Different Data Types:')

for x in np.nditer(arr2[:, ::2]):
   print(x)


# ------------------ Enumerated Iteration Using ndenumerate() --------------

print('Iterating Array With Different Data Types:')

for idx, x in np.ndenumerate(arr2):
  print(idx, x)


