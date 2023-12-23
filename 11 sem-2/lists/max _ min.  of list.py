a = eval(input("enter the list"))
max = a[0]
pos = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        pos=i
print(max, " is largest at index", pos)
a = eval(input("enter the list"))
min = a[0]
pos = 0
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        pos=i
print(min, " is smallest at index ", pos)