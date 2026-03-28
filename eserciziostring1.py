from typing import NewType


def noLetters(str):
    newStr = ""
    for n in range(0, len(str)):
        if not str[n].isalpha():
            newStr +=str[n]
    return newStr

def noNumbers(str):
    newStr = ""
    for n in range(0,len(str)):
        if not str[n].isnumeric():
            newStr +=str[n]
    return newStr


def noLetters1(str):
    n=0
    newStr = ""
    while n<len(str):
        n+=1
        if not str[n].isalpha():
            newStr +=str[n]
    return newStr




riga1="123a"
riga2="123"
riga3="abcdefg"
print(noNumbers(riga1))

    