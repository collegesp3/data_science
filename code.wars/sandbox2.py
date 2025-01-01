import os

def karlsson():
   ...
#  pass

print(karlsson())

dir_curr = os.getcwd()

for (offset, item) in enumerate(dir_curr):
    print(offset, ' - ', item )

#print('Current directory :', dir_curr)

for line in open('code.wars/folder_01/data_03.txt'):
    print('--- ', line.rstrip())

#print('___systeminfo :', os.system('systeminfo'))
for line in os.popen('systeminfo'):
    print(line.rstrip())

