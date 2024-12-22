print('\n',' s t a r t '.center(60, '-'))

# ----------- List iteration and comprehesion ------

print ('\n3 in [1, 2, 3] :', 3 in [1, 2, 3])
for x in [11, 12, 33]: 
    print(x, end = ' ')

print('\n',[ c * 5 for c in 'Python'])

# ------------ Sorting ----------------

L = ['abc', 'ABD', 'aBe']
L.sort()
print('\n Sort :', L)
L.sort(reverse=True)
print('\n Sort reverse :', L)

L.sort(key=str.lower)
print('\n Sort str.lower :', L)




# ------------- The end -----------------
print('\n', ' e n d '.center(60, '-'),'\n')