print('\n',11*'- ', 's t a r t ',11*'- ', '\n')
# -------------- s t a r t ------------------------


def mySum(L):
    return 0 if not L else L[0] + mySum(L[1:])
        

M = [1,5,9]
print('mySum : ', mySum(M))

C = [1,15]
if C[1:]:
    print('C[1:] True')

print(C[1:])

first, *rest = M

print('first : ', first, ' ; rest : ', rest )


# ---------- nested sublists -----------------

def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot +=sumtree(x)
    return tot

L = [1, [2, [3,4], 5], 6, [7,8]]
print ('sumtree :',sumtree(L)) 

print(' ------- sumtree_2 --------------')


def sumtree_2(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        print('front :', front)
        print('after pop(0) :', items)

        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)   
            print('items :',items) 
    return tot

#print ('sumtree_2 :',sumtree_2(L)) 



print(' ------- sumtree_3 --------------')

def sumtree_3(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        print('front :', front)
        print('after pop(0) :', items)

        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front   
            print('items :',items) 
    return tot


#print ('sumtree_3 :',sumtree_3(L))   

li1 = [1,2,3]
li1[:0] = [11]

print(li1)

# -------------- e n d ------------------------
print('\n',11*'- ', 'e n d ',11*'- ', '\n')