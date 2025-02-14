print('\n',11*'- ', 's t a r t ',11*'- ', '\n')
# -------------- s t a r t ------------------------

#   --- method 1 ---

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

print('min1 :', min1(3, 4, 1, 2))        


#   --- method 2 ---

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

print('min2 :', min2('ccc', 'aaa', 'bbb'))  


#   --- method 3 ---

def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print('min3 :', min3([2,2], [1,1], [3,3]))  


#   --- universal method minmax ---

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x,y): return x < y
def grtrthan(x,y): return x > y

print('minmax min:', minmax(lessthan,[2,2], [1,1], [3,3]))  
print('minmax max:', minmax(grtrthan,[2,2], [1,1], [3,3]))  

print('minmax lambda min:', minmax(lambda x, y : x < y ,[2,2], [1,1], [3,3])) 


#   --- intersection method ---

print('\n------ intersect ---------\n')

def intersect(*args):
    res = []
    for x in args[0]:
        print(' looking for "', x , '" in', res, ' : ')
        if x in res: 
            print(' finded ')
            continue
        for other in args[1:]:
            print(' other : ', other)
            if x not in other: 
                break
        else:
            res.append(x)
            print(x,' + : ', 'res :', res )
    return res

#print('intersect :', intersect('guns', 'saturn', 'mars'))

def ints(*args):
    res = []

    for x in args[0]:
        if x in res:
            print('...')
            continue

        for othr in args[1:]:
            if x not in othr:
                break
            print('x, othr :', x, ' ', othr)
        else:
            print('append ', x )
            
    return res

#print('ints :', ints('guns', 'saturn', 'mars'))

for y in range(10):
    if y>8:
        print('\nBREAK !') 
        break
    print(y, end=' ')
else:
    print("\ncycle wasn't breaked")
    
print(y)

# -------------- e n d ------------------------
print('\n',11*'- ', 'e n d ',11*'- ', '\n')