from common_func import *
printStart()
# -------------- s t a r t ------------------------

print('ord("s") : ', ord('s'))

print('ord ("Carlsson") :', list(map(ord, 'Carlsson')))

print('nested: ', [x*y for x in [3, 4, 2] for y in ['a', 5]])

# ---------------- e n d ------------------------
printEnd()