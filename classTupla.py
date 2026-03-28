class Tupla:
    def __init__(self, N):
        self.tupla=(0,)*N

    def showTupla(self):
        print(self.tupla)
    
    def setTupla(self, k, i):
        if i>=0 and i<len(self.tupla):
            self.tupla = self.tupla[:i] + (self.tupla[i]+k,) + self.tupla[i+1:]

class TuplaPlus(Tupla):
    def __init__(self, N, val):
        Tupla.__init__(N) 
        self.tupla=(val,)*N

nuovat = Tupla(5)
nuovat.showTupla()
nuovat.setTupla(8, 2)
nuovat.setTupla(5, 1)
nuovat.setTupla(7, 0)
nuovat.setTupla(9, 3)
nuovat.showTupla()