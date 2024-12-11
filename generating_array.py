import numpy as np
import matplotlib.pyplot as plt

print('Zeros :', np.zeros((2,3)))
print('Ones :', np.ones((2,3)))

arr = np.arange(25).reshape((5,5))
print('Original :\n', arr)
print('Diag :', np.diag(arr, k=1))

print('Linspace : \n', np.linspace(0,100, num = 10))

print('Logspace : \n', np.logspace(1, 2, num = 10))

fig = plt.figure(figsize=(5,3))
axes = fig.add_axes([0,0,1,1])


axes.set_xlabel('x') # добавить название оси Х
axes.set_ylabel('y') # добавить название оси Y
axes.plot(np.logspace(0, 2, num = 10), 'o')
axes.plot(np.linspace(1,100, num = 10), 'r*')
plt.show()


