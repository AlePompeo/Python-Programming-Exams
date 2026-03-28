def foo(lis, x, i):
    if i<int(len(lis)/2):
        x1 = lis[i]+lis[len(lis)-i-1]
        if x != x1:
            return x == x1
        return foo(lis, x1, i+1)
    return True

lis = [1, 5, 3, 6, 4, 8] 
x = 9
print(foo(lis, x, 0))

lis = [1, 5, 2, 6, 4, 8] 
print(foo(lis, x, 0))

lis = [1, 5, 3, 7, 6, 4, 8] 
print(foo(lis, x, 0))

