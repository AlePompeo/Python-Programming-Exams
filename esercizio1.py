
# @param tempCels: float (temperatura in gradi Celsius)  

def celsToFahr(tempCels) : 
    x = tempCels*9/5.0 
    y = x+32 
    print('valore temperatura in gradi Celsius: ', tempCels ) 
    print('valore temperatura in gradi Fahrenheit: ', y ) 
    return y
 

c = 20 
f=celsToFahr(c) 
print("gradi Fahrenheit",f)