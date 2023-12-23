a = int(input("Enter a Number"))
lj=0
for i in range(1, a+1):
    if a % i == 0:
        b = 1 #then it is factor
        if i != 1:
            for j in range(2, i//2+1):
                if i % j == 0:
                    b = 0# means not prime
                    break
            if b == 1:
                print(i, "is a prime factor")
                lj += 1
print("there are ", lj, " prime factors")