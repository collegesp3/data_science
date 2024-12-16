print('C:\new\text.dat') # Opriginal

print(r'C:\new\text.dat') # Raw string

print('C:\\new\\text.dat') # Backslashes

print('Using "for" r:\n')

str = r'C:\new\text.dat'
for c in str:
    print (c, end='')

print('\n length :', len(str))

print('\nUsing "for" \\:\n')

str2 = 'C:\\new\\text.dat'
for c in str:
    print (c, end='')

print('\n length :', len(str2))