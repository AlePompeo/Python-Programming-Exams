def restZ(str1, str2):
    newStr = ""
    for i in range(0, len(str1)):
        if not str1[i] == str2[-1]:
            newStr += str1[i]
    return newStr

z= "beta"
j= "a3aaf8&2eoa?"
print(restZ(j, z))
