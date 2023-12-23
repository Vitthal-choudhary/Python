a = int(input("enter a number"))
decimal=0
position=0
while a > 0:
    decimal += ((a%10)*(8**position))
    position+=1
    a=a//10
list = []
while decimal > 0:
    list.append(decimal % 16)
    decimal = decimal//16
list.reverse()
for i in range(len(list)):
    if list[i]==10:
        print("A")
    elif list[i]==11:
        print("B")
    elif list[i]==12:
        print("C")
    elif list[i]==13:
        print("D")
    elif list[i]==14:
        print("E")
    elif list[i]==15:
        print("F")
    else:
        print(list)