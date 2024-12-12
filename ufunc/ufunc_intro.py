import numpy as np

# ------------ Vectrization --------------

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

print (tuple(zip(x,y)))

for i, j in zip(x,y):
    z.append(i + j)
print ('Without ufunc:', z)

print('With ufunc "add()" :', np.add(x, y))

