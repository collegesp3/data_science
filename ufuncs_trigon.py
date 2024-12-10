import numpy as np

# ------------------ Trigonometric Functions ----------------
x = np.pi/2
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

print('Original: ', x)
print('Sin :', np.sin(x))

print('Original: ', arr)
print('Sin :', np.sin(arr))

# ------------------ Convert Degrees Into Radians ----------------

arr2 = np.array([90, 180, 270, 360])

print('Original: ', arr2)
print('Radians :', np.deg2rad(arr2))

print('Original: ', arr)
print('Grad :', np.rad2deg(arr))

# ------------------ Finding Angles ----------------

print('Arcsin :', np.rad2deg(np.arcsin(1.0)))


# ------------------ Angles of Each Value in Arrays ----------------

arr3 = np.array([1, -1, 0.1])

print('Original: ', arr3)
print('Angle (grad) :', np.rad2deg(np.arcsin(arr3)))

# ------------------ Hypotenues ----------------

base = 3
perp = 4

print('Original: ', base, perp)
print('Hypotenues :', np.hypot(base, perp))


