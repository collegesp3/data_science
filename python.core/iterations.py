""" import os
cwd = os.getcwd()
print('_____Curr dir : \n', cwd) """
print('\n',' s t a r t '.center(60, '-'))
# ------------- s t a r t -----------------




file01 = open('python.core/files.py')

print('~~~ ', file01.__next__())
print('~~~ ', file01.__next__())
print('~~~ ', file01.__next__())
print('~~~ ', file01.__next__())
print('~~~ ', file01.__next__())


for line in open('python.core/tmp/carlsson.txt', encoding="utf-8"):
    print(line.upper(), end='')

# ------------ convert to iterable ------------

lst = 'Freken Bok'
lst_iter = iter(lst)

for l in lst:
    print(lst_iter.__next__(), end='.')

""" print('lst_iter.__next__ :', lst_iter.__next__())
print('lst_iter.__next__ :', lst_iter.__next__())
print('lst_iter.__next__ :', lst_iter.__next__()) """



# ------------- The end -----------------
print('\n', ' e n d '.center(60, '-'),'\n')