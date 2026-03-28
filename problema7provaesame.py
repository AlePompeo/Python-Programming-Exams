class MyTuple:
    def __init__(self, theValuesCnt):
        self.itsValues = tuple([0]*theValuesCnt)

    def print(self):
        print(self.itsValues)

    def setValue(self, k, i):
        self.aList = list(self.itsValues)
        self.aValue = self.aList[i] 
        self.aList[i] = self.aValue + k
        self.itsValues = tuple(self.aList)

class MyChildTuple(MyTuple):
    def __init__(self, theValue, theValuesCnt):
        self.itsValues = tuple([theValue]*theValuesCnt)

tupla = MyTuple(5)
tupla.print() 

tupla1 = MyChildTuple(6,4)
tupla1.print()
    



    