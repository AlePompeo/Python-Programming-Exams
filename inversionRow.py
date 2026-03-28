#metodo prof
def matrix(nRows, nColumns):
    mat =[]
    for i in range(nRows):
        row = [0]*nColumns
        mat.append(row)
    return mat
#metodo stack overflow
def mat(width, height):
    mat = [[0 for x in range(width)] for y in range(height)]
    return mat

def inversion(matrix, x):
#          height         width
    if len(matrix) == len(matrix[0]) and x < len(matrix) and x < len(matrix[0]) and x > 0:
        for i in range(len(matrix)): #pre-selected row
            oldRow = matrix[x][i]
            oldCol = matrix[i][x]

            matrix[i][x] = oldRow
            matrix[x][i] = oldCol
        return matrix
    return matrix

newMatrix = matrix(3,3)
for i in range(len(newMatrix)):
    newMatrix[i][1] = 4
    newMatrix[1][i] = 7
print(newMatrix)

print(inversion(newMatrix, 1))
