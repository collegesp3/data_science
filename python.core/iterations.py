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

# ------------ using list comprehensions on files ------------

f_name = 'python.core/tmp/carlsson.txt'

f = open(f_name, encoding="utf-8")
print('\n\n------ using list comprehensions on files :\n', 
      f.readlines())

#  ------- cut the "\n" : ----------

print('\n------ cut the "\\n"  :\n', 
      [line.rstrip() for line in open(f_name, encoding="utf-8")]) 

#  ------- other operations : ----------
import re

print('\n Карлсон ?  :\n', 
      [('Карлсон' in line, re.sub('Карлсон', 'Carlsson', line))
         for line in open(f_name, encoding="utf-8")]) 

#  -------if clause : ----------

print('\n strings with "Карлсон" only  :\n', 
      [ line.rstrip()
        for line in open(f_name, encoding="utf-8")
        if 'Карлсон' in line
      ]) 


#  -------nested "for" : ----------

s1 = 'abc'
s2 = '123'

print('\n all combinations :\n', 
      [ x + y for x in s1 for y in s2]) 

print('\n unique combinations :\n', 
      [ x + y for x in s1 
        for y in s1 
        if x != y
      ]) 



# ------------- The end -----------------
print('\n', ' T h e  e n d '.center(60, '-'),'\n')