class Medico:
    def __init__(self, n, spec):
        self.nome=n
        self.specializzazione=spec
        self.colleghi=[]
    
    def getNome(self):
        print("nome: ", self.nome)

    def getSpecializzazione(self):
        print("specializzazione: ", self.specializzazione)
    
    def setColleghi(self, collega):
        self.colleghi.append(collega)

    def getColleghi(self):
        print("colleghi: ")
        for i in range(len(self.colleghi)):
            print(self.colleghi[i])

pippo= Medico("pippo", "tuttologo")
pippo.setColleghi("ciccio")
pippo.setColleghi("pluto")
pippo.setColleghi("ciccio")
pippo.setColleghi("pluto")
pippo.setColleghi("ciccio")
pippo.setColleghi("pluto")
pippo.setColleghi("ciccio")
pippo.setColleghi("pluto")
pippo.getColleghi()