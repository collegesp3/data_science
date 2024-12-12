import numpy as np

a = np.unique([1, 3, 5, 7, 5])
b = np.unique([2, 3, 4, 4, 5, 6, 5])

print('Original : \n', 'a:',a,'\n', 'b:', b)

print('In1d (a, b) : \n', np.isin(a, b))
print('Intersect (a, b) : \n', np.intersect1d(a, b))
print('Setdiff (a, b) : \n', np.setdiff1d(a, b))
print('Union (a, b) : \n', np.union1d(a, b))

print('1 in a : \n', 1 in a)
print('1 in b : \n', 1 in b)