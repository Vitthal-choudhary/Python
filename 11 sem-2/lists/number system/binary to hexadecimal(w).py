# 110010 ------> 32
a = int(input("enter a binary number"))
b = a % 10000
hexadecimal = 0
power = 0
while a > 0:
    hexadecimal += (b+(2**power))
    power += 1
    a = a//10000
f = str(hexadecimal)
g=list(f)
g.reverse()
print(g)