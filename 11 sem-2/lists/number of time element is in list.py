a = eval(input("enter the list"))
final = []
for i in range(len(a)):
    count = 1
    b=a[i]
    if b not in final:
        for j in range(i+1,len(a)):
            if b == a[j]:
                count += 1
        if b not in final:
            print(str(a[i])+' occurs '+str(count)+' times')
            final.append(b)