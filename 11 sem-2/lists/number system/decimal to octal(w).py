a = int(input("Enter a number"))
list=[]
while a>0:
    list.append(a%8)
    a=a//8
list.reverse()
print(list)