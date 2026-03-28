def counterDigits(str, cnt, i):
    #@param str: string  
    #@param cnt: int set to 0 
    #@param i: int set to 0 
    #@return: int 
    if i == len(str):
        return cnt
    if str[i].isdigit() and i <= len(str):
        cnt += 1
    return counterDigits(str, cnt, i+1)


def getList(str, list, i):
    #@param str: string 
    #@param list: empty list  
    #@param i: int set to 0 
    #@return: list 
    if i == len(str):
        return list
    if str[i].isdigit() and i <= len(str):
        list.append(str[i])
    return getList(str, list, i+1)



s = 'h9u8j91'
print(counterDigits(s, 0, 0))
print(getList(s, [], 0))

