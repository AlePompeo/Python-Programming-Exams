def stampaPosPari(lista) :
    for x in [0,2,4,6]:
        print("posPari", lista[x])

def stampaPosDispari(lista) :
    for x in [1,3,5]:
        print("posDispari", lista[x])

sequenza = [3, 5, 12, 31, 43, 7, 11]

stampaPosPari(sequenza)
stampaPosDispari(sequenza)