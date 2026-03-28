def numStr():
    dim = int(input("inserire il numero di stringhe: "))
    return dim

def insertStr():
    list = []
    newStr = ""
    listDim = numStr()
    for i in range(0, listDim):
        newStr = input("inserisci una parola: ")
        list.insert(i, newStr)
    return list

def checkLen():
    list = insertStr()
    newStr = ""
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if j!=i and len(list[j])>len(list[i]) and len(newStr)<len(list[j]):
                newStr = list[j]            
    return newStr

print(checkLen())


    







