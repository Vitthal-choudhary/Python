a = open('other.txt', 'r')
x = a.readlines()
for i in x:
    for j in range(len(i)):
        if i[j] != '$':
            print(i[j])
        else:
            break
