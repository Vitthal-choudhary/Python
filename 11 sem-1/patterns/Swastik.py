x = int(input("Enter an integer"))
if x>=3:
    for i in range(1,x+1):
        print("*",end=" ")
    for i in range(1,x-1):
        print(" ",end=" ")
    print("*")  #This gives me first line if x=4, then ****     * (5 spaces)
    for i in range(1,x-1):
        for j in range(1,x):
            print(" ",end=" ")
        print("*",end=" ")
        for k in range(1,x-1):
            print(" ",end=" ")
        print("*")  #This gave me next 3 lines.
    for i in range(1,x*2):
        print("*",end=" ")
    print() #This give me next line in which only ************ are there.
    for i in range(1,x-1):
        print("*",end=" ")
        for j in range(1,x-1):
            print(" ",end=" ")
        print("*")
    print("*",end=" ")  #This gives mme next 3 lines
    for i in range(1,x-1):
        print(" ",end=" ")
    for i in range(1,x+1):
        print("*",end=" ")
else:
    print("Enter a Number bigger than 2")