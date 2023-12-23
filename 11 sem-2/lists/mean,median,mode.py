a = eval(input("enter a list"))
sum = 0
for i in range(len(a)):
    sum += a[i]
print("mean is ", sum/len(a))
if (len(a)) % 2 != 0:
    b = len(a)//2
    print("median is ", a[b])
elif len(a) % 2 == 0:
    b = (len(a)+1)/2
    print('median is ', b)
max_rep = 0
for i in range(len(a)):
    #print(l.count(l[i]))
    if a.count(a[i])>max_rep:
        max_rep=a.count(a[i])
        continue
print(max_rep, " occurs most of the times")