def starting_mark(height):
    
    l1 = 9.45
    l2 = 10.67

    h1 = 1.52
    h2 = 1.83

    coeff = (l2-l1)/(h2-h1)

    l0 = l1 - h1*coeff
    
    l = l0 + height*coeff
    
    return round(l*100)/100
    #return round(l)

print(starting_mark(1.22))