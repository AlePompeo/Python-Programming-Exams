class Angolo:
    def __init__(self, a):
        self.ampiezza = a
    
    def compl(self):
        return 90-self.ampiezza
    
    def suppl(self):
        return 180-self.ampiezza

    def valore(self):
        return self.ampiezza

nuovoAngolo = Angolo(30)
x = nuovoAngolo.compl()
print(x)