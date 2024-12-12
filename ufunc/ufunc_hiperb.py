import numpy as np

# ------------------ Hyperbolic Functions ----------------
x = np.pi/2
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
arr1 = np.array([0.1, 0.2, 0.5])

print('Original: ', x)
print('Sinh :', np.sinh(x))

print('Original: ', arr)
print('Cosh :', np.cosh(arr))

print('Arcsinh(1.0) :', np.arcsinh(1.0))

