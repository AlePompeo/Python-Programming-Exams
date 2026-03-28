class matrix :
  def __init__(self, numrows, numcolumns) :
    # @param numrows : int; number of rows 
    # @param numcolumns: int; number of columns
    # builds a matrix and initializes to 0 all its entries
     self.rows = numrows
     self.cols = numcolumns
     self.mat = []
     for i in range(0, numrows) :
       self.mat.append([])
       for j in range(0, numcolumns) :
          self.mat[i].append(0)
          
  def val(self, i, j) :
  # @param i : int; row index
  # @param j : int; column index
  # @return  float; 
     return self.mat[i][j] 

  def modif(self, i, j, y) :
  # @param i : int; row index
  # @param j : int; column index
  # @param y: float
     self.mat[i][j] = y 

  def add(self,other) :
  # @param otherMat : matrix
  # @return  matrix ; a class matrix instance that contains the result of the sum
  # adds the matrix to the other matrix provided as parameter and returns the result as a new matrix
  # the function checks whether the matrix dimensions are compatible; in the negative case, it returns an empty matrix
    if self.rows!=other.rows or self.cols!=other.cols:
       print("non compatible dimensions")
       return matrix(0,0) #return a "null" matrix
  # the actual code starts here
    s = matrix(self.rows,self.cols) #build a new matrix
    for i in range(0,self.rows) :
      for j in range(0,self.cols) :
         s.mat[i][j] = self.mat[i][j]+other.mat[i][j]
    return s
    
  def mul(self,otherMat) :
  # @param otherMat : matrix
  # @return  matrix ; a class matrix instance that contains the result of the product
       if self.cols != otherMat.rows :
            print("non compatible dimensions")
            return matrix(0,0) #return a "null" matrix
  # the actual code starts here
       s = matrix(self.rows,otherMat.cols) # build a new matrix
       for i in range(0, self.rows) :
          for j in range(0, otherMat.cols) :
               s.mat[i][j] = 0
               for k in range(0, self.cols) :
                    s.mat[i][j] = s.mat[i][j] + self.mat[i][k]*otherMat.mat[k][j]
       return s

  def printmat(self) :
    for i in range(0,self.rows) :
          print(self.mat[i])
             
 
     
