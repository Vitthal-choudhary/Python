def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


A = [[0 for j in range(4)] for i in range(4)]
first = 0; second = 1
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = first+second
        first = second
        second = A[i][j]
print_matrix(A)