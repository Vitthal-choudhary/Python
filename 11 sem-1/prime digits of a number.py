x = int(input("Enter a number"))
while x > 0:
    y = x % 10
    x = x//10
    print(y, ' ', x)
    for i in range(2, y//2+1):
        if y % i == 0:
            break
    if i == y//2:
        print(y, "is prime")
    else:
        print(y, "is not prime")
