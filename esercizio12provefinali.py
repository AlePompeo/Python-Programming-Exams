def foo(s):
    if len(s)%2==1:
        s = s[:len(s)/2]+s[len(s)/2+1:]
    if len(s)==0:
        return True
    else:
        s1=s[:len(s)/2]
        s2=s[len(s)/2:]
        new_s = s1[1:]+s2[1:]
        return s1[0]==s2[0] and foo(new_s)