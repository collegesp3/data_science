import numpy as np

arr0 = np.array(42)                     # 0D - array
arr1 = np.array([1,3,5,7,9,11,13,15])   # 1D - array
arr2 = np.array([[1,3,5],[7,9,11]])     # 2D - array
arr3 = np.array([[[1,3,5],[7,9,11]],
                [[2,4,6],[8,10,12]]])   # 3D - array

arr5 = np.array([1,3,5,7,9], ndmin=5)

print(arr0.ndim, 'dim: ', arr0)        # Array dimensions
print(arr1.ndim, 'dim: ', arr1)
print(arr2.ndim, 'dim: ', arr2)
print(arr3.ndim, 'dim: ', arr3)
print(arr5.ndim, 'dim: ', arr5)

# ----------------- Slicing arrays -------------------------

print(arr2[1, -1], ' - last element')   # Print the last element

print(arr1[3:7], '- slice')             # Slice

print(arr1[1:7:2],' - slice with step') # Slice with step


print(type(arr1))
print(np.__version__)


