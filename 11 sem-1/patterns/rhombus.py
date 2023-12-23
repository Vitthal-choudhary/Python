n = int(input("Enter size"))
for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):   # here i bcoz i want 1st line 1 * also
        print("*",end=" ")
    for m in range(i,n):
        print(" ",end=" ")
    print()
'''opposite hill : -'''
for i in range(n):
    for j in range(i):   # if i do i+1 and at up n(n-1) then i get parrallelogram.
        print(" ",end=" ")
    for k in range(i,n):  # n-1 here coz of same reason
        print("*",end=" ")
    for k in range(i,n-1):
        print("*",end=" ")
    print()