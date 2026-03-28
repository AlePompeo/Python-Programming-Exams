def listGenerator(str):
    space = " "
    newStr = ""
    arr = []
    for i in range(0, len(str)):
        if str[i]!= space:
            newStr += str[i]
        elif str[i] == space:
            arr.append(newStr)
            newStr = ""
    arr.append(newStr)
    return arr

            

ciao = "welcome, to favelas con la 104 fratelli"
print(listGenerator(ciao))