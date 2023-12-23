handle = open('poem.txt', 'r')
dat = handle.readlines()

for i in dat:
    i = i.strip('\n')
    k = i.split()
    if len(k) == 5:
        print(i)
    else:
        continue
