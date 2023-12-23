c = int(input("Enter the no. of columns: "))
r = int(input("Enter the no. of rows: "))
x = int(input("Enter the size of rhombus: "))
if c<1 or r<1 or x<1 :
    print("Invalid")
else:
    for q in range(1,r+1):
        for p in range(1,c+1):
            for i in range(1,x):
                print(" ",end="")
            for j in range(1,x-1):
                print(" ",end="")
        print()
        for i in range(1,x-1):
            for p in range(1,c+1):
                for j in range(i,x-1):
                    print(" ",end="")
                print("*",end="")
                for k in range(1,i*2):
                    print(" ",end="")
                print("*",end="")
                for l in range(i+1,x-1):
                    print(" ",end="")
            print()
        for p in range(1,c+1):
            print("*",end="")
            for i in range(1,x*2-2):
                print(" ",end="")
        print("*")
        for i in range(x-2,0,-1):
            for p in range(1,c+1):
                for j in range(x-1,i,-1):
                    print(" ",end="")
                print("*",end="")
                for k in range(1,i*2):
                    print(" ",end="")
                print("*",end="")
                for l in range(x-2,i,-1):
                    print(" ",end="")
            print()
    for p in range(1,c+1):
        for i in range(1,x):
            print(" ",end="")
        print("*",end="")
        for j in range(1,x-1):
            print(" ",end="")