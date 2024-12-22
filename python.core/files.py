f = open('python.core/tmp/data_04.txt', 'w')
f.write('This file is data_04.txt\n')
f.write('Good bye!\n')
f.close()


f = open('data.txt')
text = f.read()

print(text)
f.close()