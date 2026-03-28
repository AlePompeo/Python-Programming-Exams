def evenSum(list, i , sum):
    if i == len(list):
        return sum
    if list[i] % 2 == 0:
        return evenSum(list, i+1 , sum+list[i])
    elif list[i] % 2 == 1:
        return evenSum(list, i+1 , sum)

x = [1, 3 , 3, 3]
print(evenSum(x, 0, 0))

    