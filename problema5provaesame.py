#the e a/any sono allocate nello stack (LIFO) (spazio temporaneo che sparisce alla fine della funzione membro)
#its allocato dentro la heap (garbage collector che dealloca) (memoria utilizzata dalla app, fissa per la app)
class RegularPoly:
    #constructor
    def __init__(self, theSideNum, theSideLen):
        self.itsSideNum = theSideNum
        self.itsSideLen = theSideLen

    #accessors
    def getSideNum(self):
        return self.itsSideNum

    def getSideLen(self):
        return self.itsSideLen

    def setSideNum(self, theSideNum):
        self.itsSideNum = theSideNum

    def setSideLen(self, theSideLen):
        self.itsSideLen = theSideLen

    #public member functions
    def print(self):
        print("N of sides:", self.itsSideNum, "side lenght:", self.itsSideLen)

    def getPerimeter(self):
        aPerimeter = 0
        for i in range(self.itsSideNum):
            aPerimeter += self.itsSideLen
        return aPerimeter

#derived class
class Square(RegularPoly):
    def __init__(self, theSideLen, theColor):
        super().__init__(4, theSideLen)
        self.itsColor = theColor

    def print(self):
        RegularPoly.print(self)
        print("color:", self.itsColor)

    def getArea(self):
        return self.itsSideLen**2

    def getColor(self):
        return self.itsColor
    
    def setColor(self, theColor):
        self.itsColor = theColor
        
#main
x = RegularPoly(3, 5)
x.print()
x.setSideNum(4)
x.print()
y = x.getPerimeter()
print("poly perimeter: ", y)

z = Square(10, "blue")
z.print() #method overriding (polimorfismo)
p = z.getPerimeter()
print("square perimeter: ", p)

area = z.getArea()
print("square area:", area)



"""
class PoligonoRegolare:
    # Costruttore pubblico
    def __init__(self):    
        itsSideLenght=0
        itsSideCnt=0

    # Funzioni membro private


    # Accessors pubbliche
    def setLenght(self,theLenght):
        self.itsSideLenght=theLenght

    def getLenght(self):
        return self.itsSideLenght

    def setCount(self,theCount):
        self.itsSideCnt=theCount

    def getCount(self):
        return self.itsSideCnt

    # Funzione membro pubbliche

    def getPerimeter(self):
        return self.itsSideCnt * self.itsSideLenght

"""

