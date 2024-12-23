# ------ Quick (n choose k) calculator -----

def fact(x):
        return (1 if x == 0 else x*fact(x-1))



def choose(n, k):   
    return ( 0 if n < k else int(fact(n)/(fact(k)*fact(n - k))))

print(choose(146, 25))

#print(fact(6))