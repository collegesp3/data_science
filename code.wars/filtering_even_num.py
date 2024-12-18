def kata_13_december(lst): 
    # Fix this code
    odds = []
    for x in lst: 
        if x%2!=0: 
            odds.append(x)
    print(odds)
 #  lst.remove(evens)        
    return odds

l = [1, 2, 2, 2, 4, 3, 4, 5, 6, 7]
print(kata_13_december(l)) 