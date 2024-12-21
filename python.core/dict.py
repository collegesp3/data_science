print('\n',' s t a r t '.center(60, '-'))



dict_01= {'name': 'Don',
        'job':  'President',
        'home': ['Washington','White House'],
        'address':{'state':'USA', 'zip':12345}       
        }

print('dict_01 :', dict_01)
print('name :', dict_01['name'])
print('home :', dict_01['home'])
print('home [0] :', dict_01['home'][0])
print('address :', dict_01['address'])
print('address zip :', dict_01['address']['zip'])


list1 = ['one', 'two', 'three']
list2 = [11, 22, 33]


dict2 = dict.fromkeys(list1, list2)
print('dict2 fromkeys :', dict2)

dict3 = dict(zip(list1, list2))
print('dict3 dict zip :', dict3)


dict4= {x : x**2 for x in range(10)}
print('dict4 comprehens. :', dict4)


# ------------- The end -----------------
print('\n', ' e n d '.center(60, '-'),'\n')
