handle = open('poem.txt', 'r')
data = handle.read()
count = 0
for i in data:
    print(i)
    if i.isupper():
        count += 1
print(count)