n=int(input("Enter size"))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
''' till here we got
     *
    **
   ***
  ****
 *****
 '''
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print("*",end=" ")
    print()
'''
this will give
*****
 ****
  ***
   **
    *
'''