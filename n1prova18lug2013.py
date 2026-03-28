def spacedStr(string, i, newStr):  
    if i == len(string):
        return newStr
    newVal = string[i] + " "
    return spacedStr(string, i+1, newStr+newVal)


x = "abcd"
print(spacedStr(x, 0, ""))
