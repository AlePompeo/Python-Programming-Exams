def matrix(nRows, nColumns):
    mat =[]
    for i in range(nRows):
        row = [0]*nColumns
        mat.append(row)
    return mat

def croce(A, i, j):
    # @param A : matrix 
    # @param i : coordinate 
    # @param j : coordinate 
    # @return bool 
    assert i<len(A) and j<len(A[0]) and i>=0 and j>=0
    
    if i+1<len(A) and A[i][j] < A[i+1][j]:  
        return False
        
    if i-1 >=0 and A[i][j] < A[i-1][j]:
        return False
    
    if j+1<len(A[0]) and A[i][j] < A[i][j+1]:
        return False
    
    if j-1 >=0 and A[i][j] < A[j-1][j]:
        return False
    
    return True


A = [[1,2,3,10], [3,5,7,2], [4,9,2,5]]

print(croce(A, 0, 0))
print(croce(A, 1, 2))
print(croce(A, 2, 1))
print(croce(A, 0, 2))