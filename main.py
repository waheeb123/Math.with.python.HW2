#1. Write a Python program to compute the eigenvalues and right eigenvectors of a given square array.
from functools import reduce
# Given Square Matrix
A = ([[5, -3],
      [-6, 2]])

print("\nA:")
##
## A:
for m in A:
    print(m)

# Identity
## [5, -3]
## [-6, 2]
I = ([[1, 0], [0, 1]])

print("\nI:")

## I:
for m in I:
    print(m)

# A Transpose A
## [1, 0]
## [0, 1]
AxI = ([[0, 0],
        [0, 0]])

for i in range(len(A)):
    for j in range(len(I[0])):
        for k in range(len(I)):
            AxI[i][j] += A[i][k] * I[k][j]

print("\nAxI:")
##
## AxI:
for m in AxI:
    print(AxI)
## [[5, -3], [-6, 2]]
## [[5, -3], [-6, 2]]
print("\nFactor:")
##
## Factor:
lamda = ([[0, 0],
          [0, 0]])

for i in range(len(AxI)):
    for j in range(len(AxI)):
        # factor[i][j] = AxI[i][j]
        lamda[i][i] = ("x".format(AxI[i][i]))

print('\n= ({0} - {1})({2} - {3}) - ({4})({5})=0'.format(AxI[0][0], lamda[0][0], AxI[1][1], lamda[1][1], AxI[1][0],
                                                         AxI[0][1]))
##
## = (5 - x)(2 - x) - (-6)(-3)=0
print('\n= ({0} - {1})({2} - {3}) - {4} = 0'.format(AxI[0][0], lamda[0][0], AxI[1][1], lamda[1][1],
                                                    AxI[1][0] * AxI[0][1]))
##
## = (5 - x)(2 - x) - 18 = 0
id_count = 0  # number of identities
coeff = 0  # coefficient
for i in range(len(lamda)):
    for j in range(len(lamda)):
        if (lamda[i][j] == "x"):
            id_count = id_count + 1
            coeff = ("x^{0}".format(id_count))

print("\n= {0}{1}{2}+{3} - {4} = 0".format(coeff, -AxI[0][0] - AxI[1][1], lamda[1][1], (-AxI[0][0]) * (-AxI[1][1]),
                                           (-AxI[1][0]) * (-AxI[0][1])))
##
## = x^2-7x+10 - 18 = 0
print("\n= {0}{1}{2}+{3} = 0".format(coeff, -AxI[0][0] - AxI[1][1], lamda[1][1],
                                     ((-AxI[0][0]) * (-AxI[1][1])) - ((-AxI[1][0]) * (-AxI[0][1]))))
##
## = x^2-7x+-8 = 0
factor1 = (-AxI[0][0] - AxI[1][1])

determinant = (((-AxI[0][0]) * (-AxI[1][1])) - ((-AxI[1][0]) * (-AxI[0][1])))

factor1 = determinant - factor1

print(factor1)
## -1
print(determinant)
## -8
print("\nEigen Values:")
##
## Eigen Values:
print("(x + ({0}))(x + ({1}))".format(factor1, determinant))
## (x + (-1))(x + (-8))
print("\nEigen Vector")
##
## Eigen Vector
eval1 = AxI[0][0] - (factor1)
eval2 = AxI[1][1] - (factor1)

print(eval1)
## 6
print(eval2)
## 3
eiganVector1 = AxI[0][1] / eval2

eiganVector2 = AxI[1][0] / eval2

print("Eigan vectors are: {0} and {1}".format(eiganVector1, eiganVector2))
## Eigan vectors are: -1.0 and -2.0


# 2. Write a Python program to compute the factor of a given array by Singular Value Decomposition
from functools import reduce

# Given Square Matrix
A = ([[5, -3],
      [-6, 2]])

print("\nA:")
##
## A:
for m in A:
    print(m)

# Transpose
## [5, -3]
## [-6, 2]
T = ([[0, 0],
      [0, 0]])

# Transpose Matrix
for i in range(len(A)):
    for j in range(len(T)):
        T[i][j] += A[j][i]

print("\nT:")
##
## T:
for m in T:
    print(m)

# A Transpose A
## [5, -6]
## [-3, 2]
ATA = ([[0, 0],
        [0, 0]])

for i in range(len(A)):
    for j in range(len(T[0])):
        for k in range(len(T)):
            ATA[i][j] += A[i][k] * T[k][j]

print("\nATA - A Transpose A:")
##
## ATA - A Transpose A:
for m in ATA:
    print(ATA)
## [[34, -36], [-36, 40]]
## [[34, -36], [-36, 40]]
print("factor:")
## factor:
lamda = ([[0, 0],
          [0, 0]])

for i in range(len(ATA)):
    for j in range(len(ATA)):
        # factor[i][j] = AxI[i][j]
        lamda[i][i] = ("x".format(ATA[i][i]))

print('\n= ({0} - {1})({2} - {3}) - ({4})({5})=0'.format(ATA[0][0], lamda[0][0], ATA[1][1], lamda[1][1], ATA[1][0],
                                                         ATA[0][1]))
##
## = (34 - x)(40 - x) - (-36)(-36)=0
print('\n= ({0} - {1})({2} - {3}) - {4} = 0'.format(ATA[0][0], lamda[0][0], ATA[1][1], lamda[1][1],
                                                    ATA[1][0] * ATA[0][1]))
##
## = (34 - x)(40 - x) - 1296 = 0
id_count = 0  # number of identities
coeff = 0  # coefficient
for i in range(len(lamda)):
    for j in range(len(lamda)):
        if (lamda[i][j] == "x"):
            id_count = id_count + 1
            coeff = ("x^{0}".format(id_count))

print("\n= {0}{1}{2}+{3} - {4} = 0".format(coeff, -ATA[0][0] - ATA[1][1], lamda[1][1], (-ATA[0][0]) * (-ATA[1][1]),
                                           (-ATA[1][0]) * (-ATA[0][1])))
##
## = x^2-74x+1360 - 1296 = 0
print("\n= {0}{1}{2}+{3} = 0".format(coeff, -ATA[0][0] - ATA[1][1], lamda[1][1],
                                     ((-ATA[0][0]) * (-ATA[1][1])) - ((-ATA[1][0]) * (-ATA[0][1]))))
##
## = x^2-74x+64 = 0
factor1 = (-ATA[0][0] - ATA[1][1])

determinant = (((-ATA[0][0]) * (-ATA[1][1])) - ((-ATA[1][0]) * (-ATA[0][1])))

factor1 = determinant - factor1

print(factor1)
## 138
print(determinant)
## 64
print("\nEigen Values:")
##
## Eigen Values:
print("(x + ({0}))(x + ({1}))".format(factor1, determinant))
## (x + (138))(x + (64))
print("\nEigen Vector")
##
## Eigen Vector
eval1 = ATA[0][0] - (factor1)
eval2 = ATA[1][1] - (factor1)

print(eval1)
## -104
print(eval2)
## -98
eiganVector1 = ATA[0][1] / eval2

eiganVector2 = ATA[1][0] / eval2

print("Eigan vectors are: {0} and {1}".format(eiganVector1, eiganVector2))

## Eigan vectors are: 0.3673469387755102 and 0.3673469387755102


# 3. Write a Python program to compute the determinant of an array.
# Given Square Matrix

A = ([[5, -3],
      [-6, 2]])

# Identity Matrix
I = ([[1, 0],
      [0, 1]])

# A * Identity Matrix
AxI = ([[0, 0, ],
        [0, 0]])

for i in range(len(A)):
    for j in range(len(I[0])):
        for k in range(len(I)):
            AxI[i][j] += A[i][k] * I[k][j]

determinant = (AxI[0][0] * AxI[1][1] - AxI[1][0] * AxI[0][1])

print("Determinant: {0}".format(determinant))
## Determinant: -8