'''
1 2 3 4
5 6 7 8
6 7 8 9
4 5 6 7
'''

a = [[1,2,3,4],[5,6,7,8],[6,7,8,9],[4,5,6,7]]
for i in range(4):
    for j in range(4):
        if j>i:
            print(a[i][j],end=' ')
    print()
# for lower triangular matrix
for i in range(4):
    for j in range(4):
        if i>j:
            print(a[i][j],end=' ')
    print()