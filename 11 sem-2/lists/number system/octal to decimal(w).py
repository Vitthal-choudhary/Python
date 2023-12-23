#  62  --------->  50
a = int(input("enter a number"))
decimal=0
position=0
while a > 0:
    decimal += ((a%10)*(8**position))
    position+=1
    a=a//10
print(decimal)