def foo(s, k, i):
    if k == 0:
        return True
    if i < len(s):
        if s[i].isdigit():
            return foo(s, k-1, i+1)
        return foo(s, k, i+1)
    return False

x = "1235"
print(foo(x, 5, 0))

