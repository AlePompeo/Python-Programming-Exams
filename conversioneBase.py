def convInt(n, fromBase, toBase):
    #@param n: int; parte intera del numero reale da convertire 
    #@param fromBase: int; base del numero da convertire
    #@param toBase: int; base del numero convertito 
    #@return: int
    power = 0
    newNum = 0
    while n > 0:
        remnant = n % toBase
        newNum += remnant * fromBase ** power
        n //= toBase
        power += 1
    return newNum

def convFraz(f, fromBase, toBase, k):
    #@param fromBase: int; base del numero da convertire
    #@param toBase: int; base del numero convertito 
    #@param f: float; numero in cifre decimali 
    #@param k: int; numero di cifre dopo la virgola 
    #@return: float
    power = 1
    newNum = 0
    while f > 0 and power<=k:
        product = f * toBase
        newNum +=  int(product) * fromBase ** (-power)
        f = (product*1e17 - int(product)*1e17) / 1e17
        power += 1
    return newNum

print(convInt(100, 3, 10))
print(convFraz(0.695, 10, 2, 4))
