from typing import NewType

def alphaStr(str):
    newStr = ""
    for i in range(len(str)):
        if str[i].isalpha():
            newStr += str[i]
    return newStr

def composePrev(str, l1):
    getPrev = ""
    for i in range(len(str)):
        if str[i] == l1:
            getPrev = str[:i] + str[i-1:i] + str[i+1:]
            return getPrev
    return str

def composePrev1(str, l1):
    newStr=""
    for i in range(len(str)):
        if i>0 and str[i] == l1:
            newStr+=str[i-1]
        else:
            newStr+=str[i]
    return newStr

def composeOccurr(str, l2):
    newStr = ""
    for i in range(len(str)):
        newStr += str[i]
        if str[i] == l2:
            newStr += str[i]
    return newStr

s ="v4tt3l4p3sc4"
a = "p"
t = "t"

print(alphaStr(s))
str = alphaStr(s)
print(composePrev(str, a))
print(composePrev1(str, a))
str2 = composePrev(str, a)
print(composeOccurr(str2, t))
