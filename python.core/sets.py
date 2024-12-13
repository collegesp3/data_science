import sys
print('\n',10*'- ', 's t a r t ',10*'- ', '\n')

x = set('abcde')
y = set('bdxyz')
z = set('ab')

# -------------- Basic operations -------------------------------

print('Original :\n',x, y, z)

print('Difference :\n', x - y) 
print('Union :\n', x | y) 
print('Intersection :\n', x & y, x.intersection(y)) 
print('Symmetric difference :\n', x ^ y) 
print('Superset, subset :\n', x > y , x < y, z < x, z.issubset(y)) 
print('Membership ("c" in x):\n', 'c' in x) 
print('Add :\n', z.add('Solute'), z) 
print('Merge :\n', z.update(set(['!', '?'])), z) 
print('Remove :\n', z.remove('?'), z) 

print('Output set "y" in cycle :') 
for item in y:
    print(item*3)

# --------------- Sets in memory ------------------------

print('Sizes :\n', sys.getsizeof(x), y.__sizeof__(), sys.getsizeof(z), 'bytes') 

w = set()
w = {'a','b','!', 'dasfdasfasdfsfdsds', 's', 'm', 'f', }
print(w, sys.getsizeof(w))


# --------------- Exersizes -------------------------------

list1 = set([10, 20, 30, 40, 50])
list2 = set([20, 25, 30, 35, 40])

print(list(list1 - list2))

# --------------------------------------------

students = {"Tom", "Bob", "Sam"}
employees = {"Tom", "Bob", "Alex", "Mike"}

print('Union:', students | employees)
print('Std & emp:', students & employees)
print('Std only:', employees - students)
print('Std or emp ONLY:', students ^ employees)

# --------------------------------------

set1 = {10, 20, 30}
set2 = {20, 40, 50}

#  set1 = set1 - set2
#  OR
set1.difference_update(set2)
print(set1)

# --------------------------------------

st = {'18', '24', '34', '47', '81', '63'} 
tst1 = '34'
tst2 = ('81', '12', '46')

print (tst1 in st)

for item in tst2:
    print(item, 'in st :', item in st)


print('\n',11*'- ', 'e n d ',11*'- ', '\n')



