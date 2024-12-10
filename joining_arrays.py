import numpy as np

arr0 = np.array(42)                     # 0D - array
arr1 = np.array([1,3,5,7,9,11,13,15])   # 1D - array
arr1_2 = np.array([12,32,52,72,92,112,132,152])

arr2 = np.array([[1,3,5],[7,9,11]])     # 2D - array
arr2_2 = np.array([[12,32,52],[72,92,112]])

arr3 = np.array([[[1,3,5],[7,9,11]],
                [[2,4,6],[8,10,12]]])   # 3D - array


# ----------------- Joining NumPy 1-D Arrays ---------------

arrJoined = np.concatenate((arr1, arr1_2))

print(arrJoined)

# ----------------- Joining NumPy 2_D Arrays ---------------

arrJoined = np.concatenate((arr2, arr2_2), axis=1)

print(arrJoined)


# ----------------- Joining Arrays Using Stack Functions ---------------

print('\n Using np.stack: ')

arrJoined = np.stack((arr1, arr1_2), axis=1)

print(arrJoined)

# ----------------- Stacking Along Columns ---------------

print('\n Stacking along columns: ')

arrJoined = np.vstack((arr1, arr1_2))

print(arrJoined)

# ----------------- Stacking Along Rows ---------------

print('\n Stacking along Rows: ')

arrJoined = np.hstack((arr1, arr1_2))

print(arrJoined)

# ----------------- Stacking Along Height (depth) ---------------

print('\n Stacking along Height (depth): ')

arrJoined = np.dstack((arr1, arr1_2))

print(arrJoined)

arr0 = np.array(42)                     # 0D - array
arr1 = np.array([1,3,5,7,9,11,13,15])   # 1D - array
arr1_2 = np.array([12,32,52,72,92,112,132,152])

arr2 = np.array([[1,3,5],[7,9,11]])     # 2D - array
arr2_2 = np.array([[12,32,52],[72,92,112]])

arr3 = np.array([[[1,3,5],[7,9,11]],
                [[2,4,6],[8,10,12]]])   # 3D - array


# ----------------- Joining NumPy 1-D Arrays ---------------

arrJoined = np.concatenate((arr1, arr1_2))

print(arrJoined)

# ----------------- Joining NumPy 2_D Arrays ---------------

arrJoined = np.concatenate((arr2, arr2_2), axis=1)

print(arrJoined)


# ----------------- Joining Arrays Using Stack Functions ---------------

print('\n Using np.stack: ')

arrJoined = np.stack((arr1, arr1_2), axis=1)

print(arrJoined)

# ----------------- Stacking Along Columns ---------------

print('\n Stacking along columns: ')

arrJoined = np.vstack((arr1, arr1_2))

print(arrJoined)

# ----------------- Stacking Along Rows ---------------

print('\n Stacking along Rows: ')

arrJoined = np.hstack((arr1, arr1_2))

print(arrJoined)

# ----------------- Stacking Along Height (depth) ---------------

print('\n Stacking along Height (depth): ')

arrJoined = np.dstack((arr1, arr1_2))

print(arrJoined)