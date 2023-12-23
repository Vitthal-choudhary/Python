''''
row of this become column of that

123                         147
456         ----->          258
789                         369

'''

A = [[j for j in range(3)] for i in range(4)]
#print(A)
B = [[0 for j in range(4)] for i in range(3)]
for i in range(4):
    for j in range(3):
        B[j][i] = A[i][j]
#print(B) will give transpose.
