from numpy import random as rnd
import numpy as np

#------------ Random Distribution -------------

x = rnd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
#x = rnd.choice([3, 5, 7, 9], size=(100))
print('Random Distribution: \n', x)

x = rnd.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(5, 7))
print('Random 2-D Distribution: \n', x)

#------------ Shuffling Arrays -------------

arr1 = np.array([1, 2, 3, 4, 5])

print('Original:', arr1 )

rnd.shuffle(arr1)

print('Shuffled arr1: ', arr1)

#------------ Generating Permutation of Arrays -------------

arr1 = np.array([1, 2, 3, 4, 5])

print('Original:', arr1 )

rnd.shuffle(arr1)

print('Permutation arr1: ', rnd.permutation(arr1))
