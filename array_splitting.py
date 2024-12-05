import numpy as np

arr0 = np.array(42)
arr1 = np.array([1,2,3,4,5,6,7])
arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# --------------- Splitting --------------------

newArr = np.array_split(arr1, 3)
print('Original: \n',arr1)
print('After splitting: \n',newArr)

print(newArr[1])

# --------------- Splitting 2-D Arrays --------------------

newArr = np.array_split(arr2, 3, axis=1)
print('Original: \n',arr2)
print('After splitting: \n',newArr)

print('newArr[1]: \n',newArr[1])

# ------------- vsplit() and dsplit() ------------
# ------------- work as vstack() and dstack() ----





# -------------- Converting of seconds ----------
""" sec = 3661
h = sec//3600
m = (sec - h*3600)//60
m2 = (sec//60)%60
print(sec//3600,':',m,':', sec%60)
print(sec - h*3600)
print (m2) """
 
