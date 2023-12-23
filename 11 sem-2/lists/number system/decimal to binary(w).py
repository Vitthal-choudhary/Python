# 50 ---------> 110010
a = int(input("Enter a number"))
list=[]
while a>0:
    list.append(a%2)
    a=a//2
list.reverse()
print(list)