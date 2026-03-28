def foo(list):
    def foo2(list, cnt):
        if not list:
            return cnt
        else:
            newStr = list[0]
        if newStr[0]==newStr[-1]:
            return foo2(list[1:], cnt+1)
        else:
            return foo2(list[1:], cnt)
    return foo2(list, 0)


lista= ["aasdf", "asdftr", "gjag45", "gahg", "1gtdf1"]
print(foo(lista))