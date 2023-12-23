l = list(input("enter the list"))
for i in range(len(l)):
    min = l[i]
    position = i
    for j in range(i, len(l)):
        if l[j] < min:      # for descending we can do l[j] > max
            min = l[j]
            position = j
    t=l[i]
    l[i]=l[position]
    l[position]=t
print(l)