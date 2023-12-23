# 32  --------->  50
a = int(input("enter a hexadecimal number"))
decimal=0
power=0
while a>0:
    decimal +=((a % 10)*(16**power))
    power+=1
    a=a//10
print(decimal)