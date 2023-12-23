'''
take 16 elements and store them in a matrix both row wise and column wise.
'''

list = [v for v in range(1,17)]
v = 0
A = [[0 for j in range(4)] for i in range(4)]
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = list[v]
        v+=1
print(A)

'''# column wise

for i in range(len(A)):
    for j in range(len(A[0])):
        A[j][i] = list[v]
        v+=1
print(A)'''