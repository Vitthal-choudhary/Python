import csv
old = open("old.csv", 'r')
data = csv.reader(old)

new = open("new.csv", 'w+')
wri = csv.writer(new)

for i in data:
    if i[0] == 'check':
        continue
    wri.writerow(i)
    new.flush()


old.close()
new.close()