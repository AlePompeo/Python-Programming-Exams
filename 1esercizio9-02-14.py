def foo(L, v, k):
    def foo2(L, v, k, i, multiples, non):
        if i==len(L):
            return multiples>=non
        if i%k==0 and L[i]==v:
            return foo2(L, v, k, i+1, multiples+1, non)
        else:
            return foo2(L, v, k, i+1, multiples, non+1)
    return foo2(L, v, k, 0, 0, 0)


v="5"
x="gaga"
L=[v, x, v, x, v, x]
print(foo(L,v,2))
