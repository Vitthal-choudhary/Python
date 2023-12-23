'''
********
      *
     *
    *
   *
  *
 *
********
'''
n = int(input("Enter a no."))
for i in range(n):
    print("*",end="")
print("*"*2)
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    print("*")
for i in range(n):
    print("*",end="")
print("*"*2)