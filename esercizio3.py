
#
# Calcolo media
#

def media(num1,num2,num3):
    return (num1+num2+num3)/3

#
# Calcolo volume del cono
#

def volumeCono(r,h):
    myPi=3.14
    return (h*myPi*r**2)/3

# MAIN

#esercizio sulla media:
a=1
b=2
c=3
print("media aritmetica :",media(a,b,c))

#esercizio volume cono
raggio=10
altezza=10
print("volume cono 1 :",volumeCono(raggio,altezza))

raggio=5
altezza=5
print("volume cono 2 :",volumeCono(raggio,altezza))

