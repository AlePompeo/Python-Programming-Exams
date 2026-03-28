from math import expm1
from sympy import Matrix
from sympy import *
import numpy as np

x, y, z, t, e = symbols('x, y, z, t, e')
Matrix1 = Matrix([[2, -1, -1], [3,-2,-1], [4, -2, -2]])
Cauchy = Matrix([1, 0, 0])


Autovettori = Matrix1.eigenvects()
identityMatrix = Matrix.eye(3)
Matrix2 = Matrix1 + identityMatrix


lista1 = Autovettori[0]
autovalore1 = lista1[0]
moltAlg1 = lista1[1]
lambdaMatrix1 = Matrix1 - identityMatrix*autovalore1
moltGeom1 = 3 - lambdaMatrix1.rank()


lista2 = Autovettori[1]
autovalore2 = lista2[0]
moltAlg2 = lista2[1]
lambdaMatrix2 = Matrix1 - identityMatrix*autovalore2
moltGeom2 = 3 - lambdaMatrix2.rank()

P, J = Matrix1.jordan_form()
P_inverse = P.inv(method="LU")

expMatrix = Matrix([[0,0,0], [0,0,0], [0,0,0]])
if moltAlg1 == moltGeom1:
    expMatrix = expMatrix + Matrix([[0, 0, 0], [0,0, 0], [0, 0, e**(autovalore1*t)]])
elif moltAlg1 != moltGeom1:
    expMatrix = expMatrix + Matrix([[e**(autovalore1*t), t*e**(autovalore1*t), 0], [0,e**(autovalore1*t), 0], [0, 0, 0]])

if moltAlg2 == moltGeom2:
    expMatrix = expMatrix + Matrix([[0, 0, 0], [0,0, 0], [0, 0, e**(autovalore2*t)]])
elif moltAlg1 != moltGeom1:
    expMatrix = expMatrix + Matrix([[e**(autovalore2*t), t*e**(autovalore2*t), 0], [0,e**(autovalore2*t), 0], [0, 0, 0]])

finalMatrix = P*expMatrix*P_inverse*Cauchy
print("===================================================================================")
print("la matrice P: ", P)
print("===================================================================================")
print("la matrice esponenziale è: ", expMatrix)
print("===================================================================================")
print("la matrice inversa di P: ", P_inverse)
print("==================================================================================================================")
#final moltiplications
print("la soluzione generale del sistema è: ", finalMatrix)
print("==================================================================================================================")