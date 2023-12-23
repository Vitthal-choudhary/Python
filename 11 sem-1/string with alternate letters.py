x = input("enter a string")
y=""
for i in range(len(x)):
    if i%2==0:
        y+=x[i]
print(y)