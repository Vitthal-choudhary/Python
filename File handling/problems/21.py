import csv
old = open("old.csv", 'w+')
w = csv.writer(old)
l = [["name","dan"],["check",1],["size","gigantic"]]
w.writerows(l)
old.flush()
old.seek(0)
r = csv.reader(old)
for i in r:
    print(i)
