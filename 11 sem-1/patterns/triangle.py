x = int(input("Enter a number :"))
for i in range(1,x):
    print(" ",end="")
print("*")    # till here my code printed only first line 1 star
for i in range(2,x+1):
    for j in range(i,x):
        print(" ",end="")
    print("*",end="")
    for k in range(0,i*2-3): # this is giving 1,3,5,7,...
        print(" ",end="")
    print("*")

#     *
#   *   *
#  *     *
# *       *
