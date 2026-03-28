class Numero:
    def __init__(self, s, B):
        self.string=s
        self.base=B
    
    def getString(self):
        self.count=0
        self.sum=0
        for i in range(self.string):
            if self.string.isdigit() and 0<self.string[i]<self.base-1:
                self.count+=1
                self.sum+=self.string[i]*self.base**(len(self.string)-1-i)
        if self.count == len(self.string):
            return self.sum
        else:
            return 0