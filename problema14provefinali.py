class myVehicle:
    def __init__(self, thePassengersCnt, theTyresCnt):
        self.itsPassengersCnt = thePassengersCnt
        self.itsTyresCnt = theTyresCnt
    
    def getPassengersCnt(self):
        print("passeggeri:", self.itsPassengersCnt)
    
    def getTyresCnt(self):
        print("n. ruote:", self.itsTyresCnt)

class myEnginePoweredVehicle(myVehicle):
    def __init__(self, thePassengersCnt, theTyresCnt, theEnginePower):
        super().__init__(thePassengersCnt, theTyresCnt)
        self.itsEnginePower = theEnginePower

    def getEnginePower(self):
        print("Hp:", self.itsEnginePower)

    def setEnginePower(self, xFactor):
        self.itsEnginePower = self.itsEnginePower * xFactor


mclaren = myEnginePoweredVehicle(2, 4, 500)
mclaren.setEnginePower(1.3)
mclaren.getEnginePower()
        

