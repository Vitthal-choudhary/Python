'''a = [[1,2,3],[2,3,4]]
# print(a[0][0])  # will give 1 they are indexed that way
b = [[2,3,5],[1,2,3]]

for i in range(3):
    for j in range(3):
        #print(b[i][j])
'''
A = [[j for j in range(3)] for i in range(2)]   # will give a matrix of 2 rows and 3 columns. 2X3
print(A)
B = [[j for j in range(4)] for i in range(3)]   # 3 rows 4 columns 3X4
print(B)

# Addition of matrices. for add size should be same.
# A + C = D matrix
C = [[j for j in range(3)] for i in range(2)]
D = [[j for j in range(3)] for i in range(2)]
for i in range(2):
    for j in range(3):
        D[i][j] = A[i][j] + C[i][j]

print(D)    # [[0, 2, 4], [0, 2, 4]]

# displaying diagonal elements.

matrix = [[j for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        if i==j:
            print(matrix[i][j]) # will give diagonal elements 0,1,2.

for i in range(3):
    for j in range(3):
        if i+j == 2:
            print(matrix[i][j]) # will give other diagonal 2,1,0


# adding elements of a matrix along column and row
a = [[j for j in range(3)] for i in range(2)]
for i in range(3):
    print(a[0][i] + a[1][i])