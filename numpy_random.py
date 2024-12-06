from numpy import random as rnd

#------------ Generate Random Number and Float -------------

x = rnd.randint(100)
y = rnd.rand()

print(x)
print(y)

#------------ Generate Random Array -------------

x = rnd.randint(100, size=(7))

print('Random Array: ', x)

x = rnd.randint(100, size=(3, 5))

print('Random 2-D Array: ', x)

x = rnd.rand(2, 4)

print('Random 2-D Float array: ', x)


#------------ Generate Random Number From Array -------------

x = rnd.choice([3, 5, 7, 9])
print('Choice Array: ', x)

print('Choice Array: ', rnd.choice([3, 5, 7, 9]))
print('Choice Array: ', rnd.choice([3, 5, 7, 9]))

print('Choice 2-D Array: ', rnd.choice([3, 5, 7, 9], size=(3, 5)))









