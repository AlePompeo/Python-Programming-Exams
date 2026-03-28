def matrix(nRows, nColumns):
    mat =[]
    for i in range(nRows):
        row = [0]*nColumns
        mat.append(row)
    return mat

mat = matrix(4, 3)
mat[3][1] = 1
print(mat)
print(len(mat))
print