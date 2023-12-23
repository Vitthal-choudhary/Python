kod = 1
for i in range(1, 11):
    kod = kod*i
    print(i, ' ', kod)
print(kod)
for i in range(2, 51, 2):
    kod = kod*i
    print(i, ' ', kod)
print(kod)
a = int(input("Enter a Number"))
d = 0
for i in range(1, a+1):
    if a % i == 0:
        print(i)
        d= d+i # this will give me sum of  all the factors
print("Sum of factors is",d)
# break  is used to stop loop