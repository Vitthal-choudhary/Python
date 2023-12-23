#  62  --------->  110010
a=int(input("enter a number"))
l=[]
while a>0:
    b=a%10
    for i in range(3):
        l.append(b%2)
        b=b//2
    a=a//10
l.reverse()
print(l)