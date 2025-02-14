from common_func import *
printStart()
# -------------- s t a r t ------------------------
count = [1,5,11,17]
k = [2,5,3,10]

#print(f'{k:.2f}')

def div3(x):
    return x/3

print('str(div3) :', str(div3) )

print('list(map(div3)) :', [f'{x:.3f}' for x in list(map(div3, count))])
#print([f'{x:.2f}' for x in list(map(div3, count))])

div4 = lambda x: x/4
print('list(map(div4)) :', list(map(div4, count)))
print('str(div4) :', str(div4) )

pro =  lambda x, y: x * y
print('list(map(prod1)) :', list(map(pro, count, k)))

print('list(filter) :', list(filter((lambda x: x > 10), count)))


# ---------------------- reduce -------------------------
from functools import reduce
import timeit

print('reduce :', reduce((pro), count, 0.001))

#print('factorial (use reduce) :', reduce(pro, list(range(6))[1:]))


#print(timeit.timeit('from functools import reduce','reduce((lambda x, y: x * y), list(range(6))[1:])', globals=globals()))
#print(timeit.timeit('list(map(lambda x, y: x * y, [1,5,11,17], [2,5,3,10]))', number = 1000)) # works
#print(timeit.timeit('list(map(lambda x, y: x * y, count, k))', number = 1000, globals=globals())) # works

num = 200

code = reduce(pro, list(range(num))[1:])
#print('str(code) :', str(code))

print(f'(use reduce) {num}! = ', code)
print(f'timing (use reduce) of {num}! = ', 
       timeit.timeit(f'reduce(pro, list(range({num}))[1:])', number = 1, globals=globals()))









# ---------------- e n d ------------------------
printEnd()