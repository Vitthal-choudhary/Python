# 1st two elements will add to give 3rd element of row
a = [[1,2,3,4],[1,2,3,4],[0,0,0,0]]
for i in range(4):
    a[2][i] = a[0][i] + a[1][i]
print(a[2])

'''
1 2 3 4
1 2 3 4

2 4 6 8
'''

# 1st two elements of column will add to give 3rd element
a = [[1,2,3,4,0],[1,2,3,4,0]]
'''for i in range(4):
    a[0][4] = a[0][i]+a[0][i]
print(a[0][4])'''
a[0][4] = a[0][0]+a[0][1]+a[0][2]+a[0][3]
print(a[0][4])
a[1][4] = a[1][0]+a[1][1]+a[1][2]+a[1][3]
print(a[1][4])

'''
1 2 3 4     10
1 2 3 4     10
'''