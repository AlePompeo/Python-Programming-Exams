class Quadrato:
    def __init__(self, theLength):
        self.itsLength = theLength

    def getArea(self):
        return self.itsLength**2
    
    def getPerimetro(self):
        return self.itsLength*4


q1 = Quadrato(24)
print(q1.getArea())
print(q1.getPerimetro())