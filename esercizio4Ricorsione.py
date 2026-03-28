import math

def levaSpazi(string, i):
    if i == len(string):
        return string.lower()
    if string[i].isspace():
        string = string[:i] + string[i+1:]
    return levaSpazi(string, i+1)

def palindrome(str):
    if str[0] != str[-1]:
        return False
    if str[0] == str[-1] and len(str)==2:
        return True
    if str[0] == str[-1] and len(str) % 2 == 0: #pari
        return palindrome(str[:int((len(str)/2)-1)]+str[int((len(str)/2)+1):])
        
    elif str[0] == str[-1] and len(str) % 2 == 1: #dispari
        return palindrome(str[:math.ceil(len(str)/2)-1]+str[math.floor(len(str)/2+1):])


str = "Avida di vita desiai ogni amore vero ma ingoiai sedativi da diva"
str2 = "avan"
str3 = "ingegni"
newStr = (levaSpazi(str, 0))
print(palindrome(newStr))
print(palindrome(str2))
print(palindrome(str3))