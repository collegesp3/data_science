print('\n',11*'- ', 's t a r t ',11*'- ', '\n')
# -------------- s t a r t ------------------------

def fn(a):
    a = 52

b = 42
fn(b)
print('b :',b)


def changer(a, b):
    a = 2
    b[0] = 'sky'

X = 1
L = [1, 2]
changer(X, L)
print('X, L :', X, L)


M = [5, 6]
changer(X, M[:])
print('X, M :', X, M)




# -------------- e n d ------------------------
print('\n',11*'- ', 'e n d ',11*'- ', '\n')