import numpy as np
import matplotlib.pyplot as plt



print('Zeros :', np.zeros((2,3)))
print('Ones :', np.ones((2,3)))

arr = np.arange(25).reshape((5,5))
print('Original :\n', arr)
print('Diag :', np.diag(arr, k=1))

print('Linspace : \n', np.linspace(0,100, num = 10))

print('Logspace : \n', np.logspace(1, 2, num = 10))


# ----------- Uninitialized array ----------

print('Empty: \n', np.empty(3, dtype=np.float16))

# ----------- Creating array with properties of other array  --------

def f1(x):
    y = np.ones_like(x)
    return y

print('Original :\n', arr)
print('Ones_like: \n', f1(arr))


# ----------- Creating matrix arrays -------------

print('Identity: \n', np.identity(4))
print('np.eye: \n', np.eye(5, k = -1))

print('diag: \n', np.diag(np.arange(0, 25, 5)) )

# ----------- Slicing -------------

print('Slice backward: \n', np.arange(10)[::-1])

# ----------- Multidimentional arrays -------------

f2 = lambda m, n : n + 10*m

A = np.fromfunction(f2, (5,3), dtype=int)

print('A fromfunction: \n', A)









""" fig = plt.figure(figsize=(5,3))
axes = fig.add_axes([0,0,1,1])


axes.set_xlabel('x') # добавить название оси Х
axes.set_ylabel('y') # добавить название оси Y
axes.plot(np.logspace(0, 2, num = 10), 'o')
axes.plot(np.linspace(1,100, num = 10), 'r*')
plt.show() """




