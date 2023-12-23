handle = open('lines.txt', 'r')
data = handle.readlines()
count = 0
for i in data:
    if i[0] == 'A':
        count += 1

print(count)
