import numpy as np
import random

data = np.random.normal(size=(2, 3, 5 ))
print('Origin :\n', data)

print('Sum axis = 2 :\n', data.sum(axis=2))
print('Sum axis = 2 shape :\n', data.sum(axis=2).shape)
print('Sum axis = (0, 2):\n', data.sum(axis = (0, 2)))
print('Sum axis = (0, 2) shape :\n', data.sum(axis = (0, 2)).shape)

print('Sum axis = (2, 0):\n', data.sum(axis = (2, 0)))

print('SUM :\n', data.sum())

