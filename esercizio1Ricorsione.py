def sum(num):
    sum = 0
    num = str(num)
    for i in range(len(num)):
        sum += int(num[i])
    return sum

def divForThree(num):
    num=num-3
    if num < 3:
        return False
    elif 3 == num:
        return True
    if 3 != num:
        divForThree(num)


x = sum(3333)
print(divForThree(x))

