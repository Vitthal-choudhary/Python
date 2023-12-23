a = int(input("Enter a Number"))
list = []
for i in range(1, a//2+1):
    if a % i == 0:
        list.append(i)
print(list)