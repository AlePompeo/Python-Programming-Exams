def reverse(list):
    reverseList = []
    for i in range(len(list)-1, -1, -1):
        reverseList.append(list[i])
    return reverseList

ciao = ["canne", "cannoni", "cannoli", "motoschifi"]
print(reverse(ciao))

def countList(list):
    count = 0
    for i in range(0, len(list)):
        count += 1
    return count

print(countList(ciao))
