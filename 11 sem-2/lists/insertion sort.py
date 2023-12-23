l = eval(input("enter the list"))
for i in range(len(l)):
    j = i-1
    n = l[i]
    while l[j] > n and j >= 0:
        l[j+1] = l[j]
        j -= 1
    else:
        l[j+1] = n
print(l)