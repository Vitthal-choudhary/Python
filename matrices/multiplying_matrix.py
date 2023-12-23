# pre-condition :- M x N to multiply N x P . N same. resultant will be M x P.
# multiplication always gives a square matrix, i.e. no. of rows = no. of columns.
A = [[j for j in range(4)] for i in range(3)]   # 3 x 4
B = [[j for j in range(3)] for i in range(4)]   # 4 x 3
print(A)
print(B)

C = [[0 for j in range(3)] for i in range(3)] # 3 x 3

for i in range(3):
    for j in range(3):
        for k in range(4):
            C[i][j] += A[i][k] * B[k][j]

print(C)

'''
A ->  0 1 2 3
      0 1 2 3  
      0 1 2 3
      0 1 2 3
B ->  0 1 2
      0 1 2
      0 1 2

resultant C -> 0 6 12
               0 6 12
               0 6 12
'''