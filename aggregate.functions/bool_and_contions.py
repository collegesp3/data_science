import numpy as np

a = np.arange(1, 10)
b = np.arange(9, 0, -1)

print('Original : \n', 'a:',a,'\n', 'b:', b)

print('a < b : \n', a < b)
print('Convert (a < b) to numbers : \n', 1*(a < b))

print('All (a < b) : \n', np.all(a < b))
print('Any (a < b) : \n', np.any(a < b))

# ----------------- Example (pulse) --------------

x = np.linspace(-5, 5, 11)

print('x: \n', x)

def pulse(x, pos, height, width):
    return height * (x >= pos) * (x <= (pos + width))

def pulse_logic(x, pos, height, width):
    return height * np.logical_and(x >= pos, x <= (pos + width))

print('Pulse 1 :\n',pulse(x, -2, 1, 5))
print('Pulse 2 :\n',pulse(x, 1, 1, 3))

print('The same with "logical_and" :\n', pulse_logic(x, 1, 1, 3) )

# ------------- Where, Select and Choose -----------------

print('x: \n', x)

print('Where (x < 0, x**2, x**3) :\n', np.where(x < 0, x**2, x**3))

print('Select [x < -1, x < 2, x >= 2] :\n', np.select([x < -1, x < 2, x >= 2],
                                                       [x**2, x**3, x**4] ))

print('Choose [0,0,1,0,0,0,1,1,1,2,2] :\n', np.choose([0,0,1,0,0,0,1,1,1,2,2],
                                                       [x**2, x**3, x**4] ))

print('Indexes of (nonzero abs(x) > 2) :\n', np.nonzero(abs(x) > 2))
print('Values of (nonzero abs(x) > 2) :\n', x[np.nonzero(abs(x) > 2)])