x = input("Enter a string")
for i in range(len(x)):
    for y in range(i+1, len(x)+1):
        z = x[i:y+1]
        if z == z[::-1] and len(z) > 1:
            print(z)
t = input("enter a string")
dd = t[::-1]
if t == dd:
    print("it is palindrome")
else:
    print("it is not palindrome")
b = int(input("Enter a number"))
n = b
r = 0
while b > 0:
    c = b % 10
    b = b//10
    r = r*10+c
    print(c, ' ', b, ' ', r)
if n == r:
    print(n, "is palindrome")
else:
    print(n, "is not palindrome")

# palindrome is when reverse number and original are equal like 1221,3663,6996
