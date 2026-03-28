def restLettere(str, list):
    newList = []
    newStr = ""
    for i in range(0, len(list)):
        newList = list[i]
        if list[i] <= len(str):
            newStr += str[newList]
    return newStr

s="alfeo" 
L=[2, 8, 0]
print(restLettere(s, L))