# 32  ------->  62
a = int(input("enter a hexadecimal number"))
decimal=0
power=0
while a>0:
    decimal +=((a % 10)*(16**power))
    power+=1
    a=a//10
list=[]
while decimal>0:
    list.append(decimal%8)
    decimal=decimal//8
list.reverse()
print(list)