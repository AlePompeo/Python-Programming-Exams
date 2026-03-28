def inserisci(L, n1, n2):
    for i in range(0, len(L)):
        if L[i] == n1:
            L.insert(i+1, n2)
    L.append(n2)
    return L
    
l = [3, 12, 4, 3, 10, 3]
print(inserisci(l, 3, 0))
