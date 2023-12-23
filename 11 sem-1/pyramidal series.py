terms = int(input("enter the number"))
for i in range(terms+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()
for i in range(terms+1):
    for j in range(65,+65+i):
        print(chr(j), end=' ')
    print()
x = int(input("Enter the no."))
for i in range(x+1):  #this is giving to print 3
    for j in range(1,i+1):  # this is giving to print it 3 times
        print('$', end=' ')
    print()

