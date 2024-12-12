import numpy as np

# ------------- Truncation ---------------

arr = [-3.1666, 3.6667]

print ('Origimnal:', arr)

print('Truncated: ', np.trunc(arr))
print('Fix: ', np.fix(arr))


# ------------- Rounding ---------------

arr = [-3.1666, 3.6667]

print ('Origimnal:', arr)
print('Rounded: ', np.around(arr, 2))

# ------------- Floor ---------------

arr = [-3.1666, 3.6667]

print ('Origimnal:', arr)
print('Floor: ', np.floor(arr))

# ------------- Ceil ---------------

arr = [-3.1666, 3.6667]

print ('Origimnal:', arr)
print('Ceil: ', np.ceil(arr))


