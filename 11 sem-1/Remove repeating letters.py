a = input("Enter a string")
bd=0
ac=""
for i in range(len(a)):
        if a[i-1]!=a[i]:
            ac+=a[i]
print(ac)