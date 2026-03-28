"""
list1 = [0]*3
list1[1] = 20
list1[2] = 7

list2  = [None]*3
print(list2)
list2[0] = list1

list = ["bzs", "opr", "jcs"]



c = "ciaoof"

print(c[-1])

A = [[1,2,3,10], [3,5,7,2], [4,9,2,5]]
print(A[0][3])
print(len(A))
print(len(A[0]))

x = 1.25
i = int(x)
f = (x*1e17 - i*1e17) / 1e17
print(f)


x = 50
print(type(x))
print(type(x)==float)


x = (1, 1)
print(len(x))

import math
str = "ingegni"
print(int((len(str)/2)-1))
#str = str[:int((len(str)/2)-1)]+str[int((len(str)/2)+1):]
str = str[:math.ceil(len(str)/2)-1]+str[math.floor(len(str)/2+1):]
print(str)
"""

list = [1.3, 1.6, 1.3]

newList = int(list)
print(newList)


     
