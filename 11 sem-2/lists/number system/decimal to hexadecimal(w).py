# 47802 --------> BABA
a = int(input("Enter a number"))
list = []
while a > 0:
    list.append(a % 16)
    a = a//16
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