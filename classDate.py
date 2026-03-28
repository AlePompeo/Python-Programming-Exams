class date :
  def __init__(self) :
    self.day = 1
    self.month = 1
    self.year = 0
  
  def printDate(self) :
    print('day:', self.day, ', month:',self.month,', year:', self.year)
 
  def set(self,d,m,y) :
  #@param d, m, y: int
    if (m>=1 and m<=12 and d>=1 and d<=31):
       self.day = d
       self.month = m
       self.year = y
    else :
       print('non compatible values')
       
  def __eq__(self,otherDate):
      #@param otherDate: date
      #questo metodo rende possibile l'uso dell'operatore == per confrontare
      #valori della classe date in accordo a un criterio 'personalizzato'
      #come definito sotto
      return self.day==otherDate.day and self.month==otherDate.month and self.year==otherDate.year