from common_func import *
printStart()
# -------------- s t a r t ------------------------

flam = lambda x,y,z : x + y + z
print('flam :', flam(5,19,33))

# ------- jump tables -----------------

L = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

for f in L:
    print('f : ', f(5))

print(L[0](7))


key = 'got'
X ={'already': (lambda: 1 + 3),
    'got':     (lambda: 5 + 7),
    'one':     (lambda: 52 + 47)}[key]()

print('X : ',X)



lower = (lambda x, y: x if x<y else y)

print('lower :', lower('d','c'))

# ---------------- e n d ------------------------
printEnd()