def numAlpha(str):
    count=0
    for i in range(0, len(str)):
        if not str[i].isdigit():
            count +=1
    return count

s="lf35eo4"
print(numAlpha(s))