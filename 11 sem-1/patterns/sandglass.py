'''
*************
 ***********
  *********
   *******
    *****
     ***
      *
     ***
    *****
   *******
  *********
 ***********
*************
'''
n = int(input("Enter size"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    print()
for i in range(n*2+1):
        print(" ",end="")
print("*")
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()