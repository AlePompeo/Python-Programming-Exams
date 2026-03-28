def timer(t):
    print(t)
    if t > 0:
        timer(t-1)

a = 10
timer(a)
