import numpy as np
from math import log

# ------------- Log at Base 2 ---------------

arr = np.arange(1, 10)

print ('Original:', arr)
print ('Log 2:', np.log2(arr))

# ------------- Log at Base 10 ---------------

arr = np.arange(1, 10)

print ('Original:', arr)
print ('Log 10:', np.log10(arr))

# ------------- Log at Base e ---------------

arr = np.arange(1, 10)

print ('Original:', arr)
print ('Log e:', np.log(arr))

# ------------- Log at Any Base  ---------------

nplog = np.frompyfunc(log, 2, 1)

#print ('Original:', arr)
print ('Log at Any Base:', nplog(100, 10))
print(np.log(100)/np.log(10))