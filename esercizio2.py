import math
# @param cat1 : float (primo cateto) 
# @param cat2 : float (secondo cateto) 
def pitagora(cat1, cat2) : 
    cat1 = cat1**2 
    cat2 = cat2**2 
    ipo = math.sqrt(cat1+cat2) 
    print('valore primo cateto: ', cat1 ) 
    print('valore secondo cateto: ', cat2 ) 
    print('valore ipotenusa: ', ipo ) 
    return ipo

a = 4 
b = 3  
print(pitagora(a, b)) 