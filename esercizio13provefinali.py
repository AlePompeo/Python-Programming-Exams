def foo(s, k):
    def foo2(s, k, h):
        if len(s)==0:
            return k==h
        elif s[0].isdigit():
            return foo2(s[1:], k, h+1)
        elif s[0].isalpha():
            return foo2(s[1:], k, h)
    return foo2(s, k, 0)
x="abga1234"
print(foo(x, 4))
        
