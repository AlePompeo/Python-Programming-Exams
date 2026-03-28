class Persona:
    def __init__(self, theName, theAge, theFriends):
        self.itsName = theName
        self.itsAge = theAge
        self.itsFriends = theFriends

    def getName(self):
        print("nome:", self.itsName)
    
    def getAge(self):
        print("età:", self.itsAge)

    def getFriends(self):
        print("amici:", self.itsFriends)
    
    def setFriends(self, theCount):
        self.itsFriends = theCount

class Insegnante(Persona):
    def __init__(self, theName, theAge, theFriends, theSubject, theSalary):
        super().__init__(theName, theAge, theFriends)
        self.itsSubject = theSubject
        self.itsSalary = theSalary

    def getSubject(self):
        print("materia:", self.itsSubject)

    def getSalary(self):
        print("stipendio:", self.itsSalary)

    def setSubject(self, theAnotherSubject):
        self.itsSubject = theAnotherSubject



p1 = Persona("pippo", 19, 0)
p1.getName()
p1.getAge()
p1.getFriends()
p1.setFriends(1000)
p1.getFriends()

p2 = Insegnante("ciccio", 50, 0, "informatica", 1200)
p2.getName()
p2.getSalary()
p2.getFriends()
p2.getSubject()
p2.setSubject("scienza delle merendine")
p2.getSubject()
