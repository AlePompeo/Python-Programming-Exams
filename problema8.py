def password(str):
    newStr = ""
    for i in range (0, len(str)):
        if str[i].isalpha():
            newStr += "*"
    return newStr

s="@lf35eo4$"
print(password(s))