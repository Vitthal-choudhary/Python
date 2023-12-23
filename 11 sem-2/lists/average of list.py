a = eval(input("enter the list"))
sum = 0
for i in range(len(a)):
    sum += a[i]
print("average is ", sum/len(a))