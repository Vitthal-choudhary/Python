l = [1, 2, 3, 4, 3, 2] #list(input("enter the list"))
max_rep = 0
for i in range(len(l)):
    #print(l.count(l[i]))
    if l.count(l[i])>max_rep:
        max_rep=l.count(l[i])
        continue
print(max_rep, " occurs most of the times")